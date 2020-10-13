from enum import Enum


class ExecutionSpeed(Enum):
    # number of times main loop of algorithm runs per frame.
    VERY_FAST = 1_000_000_000_000
    FAST = 21
    INTERMEDIATE = 12
    SLOW = 4
    VERY_SLOW = 2

    def __str__(self):
        return self.name.replace("_", " ").title()

    @staticmethod
    def from_str(speed: str):
        if speed == "Very Fast":
            return ExecutionSpeed.VERY_FAST
        elif speed == "Fast":
            return ExecutionSpeed.FAST
        elif speed == "Intermediate":
            return ExecutionSpeed.INTERMEDIATE
        elif speed == "Slow":
            return ExecutionSpeed.SLOW
        elif speed == "Very Slow":
            return ExecutionSpeed.VERY_SLOW
        else:
            raise NotImplementedError
