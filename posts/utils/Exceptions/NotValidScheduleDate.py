
class NotValidScheduleDateException(Exception):
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"Invalid schedule {self.date}. Date most be greater than now"