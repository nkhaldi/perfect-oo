"""Project's constants"""

from enum import Enum


class Status(Enum):
    PENDING = "Pending"
    PRIORITIZED = "Prioritized"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
