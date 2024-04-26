from abc import ABC, abstractmethod
from dataclasses import dataclass

class RenderableList(ABC):
    """A list of items that can be rendered as Dockerfile lines."""
    @abstractmethod
    def render(self) -> list[str]:
        """Render this list as a list of Dockerfile lines."""


@dataclass
class CopyFile(RenderableList):
    """A file to be copied to the Docker image."""
    src: str
    dst: str
    comment: str = None

    def render(self) -> list[str]:
        """Render this file as a COPY directive."""
        if self.comment:
            return [f"# {self.comment}", f"COPY {self.src} {self.dst}"]
        return [f"COPY {self.src} {self.dst}"]