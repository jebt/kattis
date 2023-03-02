from abc import ABC, abstractmethod
from typing import TextIO


class Problem(ABC):
    @abstractmethod
    def title(self) -> str: ...

    @abstractmethod
    def solve(self, problem_input: TextIO) -> str:
        ...
