from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def title(self): ...

    @abstractmethod
    def solve(self): ...
