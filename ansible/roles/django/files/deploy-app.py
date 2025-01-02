#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

VOLUME_NAME = "/var/simple_drf"
ENVIRONMENT_PATH = "/etc/simple_drf/appconfig.env"


def get_image_id(output):
    pattern = re.compile(r".*Loaded image ID:.+")
    found = pattern.findall(output)[0]
    image_id = found.split("sha256:")[1].strip()
    return image_id


def main():
    for path in Path("/var/docker-exports").iterdir():
        image_name, image_tag = path.stem.rstrip("__").split("__")
        load_result = subprocess.run(
            ["docker", "image", "load", "-i", str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output = load_result.stdout.decode("utf-8")
        if load_result.returncode != 0:
            raise Exception(output)
        image_id = get_image_id(output)

        subprocess.run(
            ["docker", "image", "tag", image_id, f"{image_name}:{image_tag}"]
        )

        subprocess.run(["docker", "container", "stop", "simple_drf_app"])

        subprocess.run(["docker", "container", "rm", "simple_drf_app"])

        subprocess.run(
            [
                "docker",
                "container",
                "run",
                "--detach",
                "--volume",
                f"{VOLUME_NAME}:/data",
                "--env-file",
                ENVIRONMENT_PATH,
                "--publish",
                "127.0.0.1:8000:8000",
                "--name",
                "simple_drf_app",
                "--restart",
                "unless-stopped",
                f"simple_drf:{image_tag}",
                "./gunicorn-docker-cmd",
            ]
        )

        path.unlink()


if __name__ == "__main__":
    main()
