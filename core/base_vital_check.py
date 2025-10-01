import sys
from abc import ABC, abstractmethod
from time import sleep


class VitalCheck(ABC):
    """Abstract base class for vital checks."""

    def __init__(self, value: int, age: int):
        self.value = value
        self.age = age

    @abstractmethod
    def is_ok(self) -> bool:
        """Return True if the vital is within range, else False."""
        pass

    @abstractmethod
    def error_message(self) -> str:
        """Return error message for this vital if out of range."""
        pass

    @staticmethod
    def blink_alarm(times: int = 6, delay: float = 0.5) -> None:
        """Blink an alarm symbol back and forth to indicate critical
        condition."""
        for _ in range(times):
            print("\r* ", end="")
            sys.stdout.flush()
            sleep(delay)
            print("\r *", end="")
            sys.stdout.flush()
            sleep(delay)

    def validate(self) -> str:
        """Run validation, trigger alarm if invalid."""
        if not self.is_ok():
            self.blink_alarm()
            return self.error_message()
        return None
