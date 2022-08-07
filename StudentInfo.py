# Imports
from typing import TypedDict


# Class for each student's dictionary to have type hints
class StudentInfo(TypedDict):
    name: str
    mark: float
    exam_completed: bool
