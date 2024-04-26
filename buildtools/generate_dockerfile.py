import os
from pathlib import Path
import time
from buildtools.paths import PROJECT_ROOT
from buildtools.structs import CopyFile

# Input Docker Image Params
DOCKER_BASE = "fluent/fluent-bit:3.0.2"

# Output Docker Image Params
DOCKERHUB_USERNAME = "flipbit03"
# Get a timestamp of seconds from epoch
DOCKERHUB_IMAGE = f"{DOCKER_BASE.replace("/", "-")}-{int(time.time())}-cogram"
DOCKERHUB_IMAGE_TO_PUSH = f"{DOCKERHUB_USERNAME}/{DOCKERHUB_IMAGE}"


def build_docker(base_image: str, files: list[CopyFile]) -> str:
    out = [f"FROM {base_image}\n"]
    for file in files:
        out.extend(file.render())

    return "\n".join(out).strip()

if __name__ == "__main__":
    print("Generating Dockerfile...")

    # List all files in ./fluent-bit/etc/ and create CopyFile instances for them
    copyfiles = []
    for f in Path(PROJECT_ROOT / "fluent-bit" / "etc").glob("**/*"):
        if f.is_file():
            fp = f.relative_to(PROJECT_ROOT)
            copyfiles.append(CopyFile(fp, fp))

    tpl = build_docker(DOCKER_BASE, copyfiles)

    DOCKERFILE_PATH = PROJECT_ROOT / "Dockerfile"
    DOCKERFILE_PATH.write_text(tpl)
    print(f"Written to {DOCKERFILE_PATH}")


    os.system(f"docker build . -t {DOCKERHUB_IMAGE_TO_PUSH}")
    print(f"Built Docker image {DOCKERHUB_IMAGE_TO_PUSH}")

    # Push the Docker image
    os.system(f"docker push {DOCKERHUB_IMAGE_TO_PUSH}")
    print("======")
    print(f"Pushed Docker image \"{DOCKERHUB_IMAGE_TO_PUSH}\"")
    