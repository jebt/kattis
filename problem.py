from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def title(self) -> str: ...

    @abstractmethod
    def solve(self, problem_input: list[str]) -> str:
        ...
