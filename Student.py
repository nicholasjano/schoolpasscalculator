# Class to set up each student, with the pass_checker method.
class Student:
    # Constructor to initialize each student's name, mark, and cutoff
    def __init__(self, name: str, mark: float):
        self.name: str = name
        self.mark: float = mark
        self.cutoff: int = 65

    # repr method to return a visible value of an object
    def __repr__(self):
        return f'Student({self.name}, {self.mark})'

    # Method to return if the student passed or not as a formatted string
    def pass_checker(self, completed_exam: bool) -> str:
        if self.mark >= self.cutoff:
            above_or_below = "above or equal to"
            if completed_exam:
                exam = "completed"
                status = "The class was passed!"
            else:
                exam = "not completed"
                status = "The class has been failed!"
        else:
            above_or_below = "below"
            status = "The class has been failed!"
            if completed_exam:
                exam = "completed"
            else:
                exam = "not completed"

        return f"""
        {self.name} obtained a grade of {self.mark}%, which is {above_or_below} the cutoff of {self.cutoff}%.
        The exam was {exam}. {status}"""
