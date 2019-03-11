from django.db import models


# Create your models here.
class Subject(models.Model):
    def __init__(self, which_angel, date, score, elapsed_time, result, body, answer):
        self.which_angel = which_angel
        self.date = date
        self.score = score
        self.elapsed_time = elapsed_time
        self.result = result
        self.body = body
        self.answer = answer


class Math(Subject):
    def __init__(self, which_angel, date, score, elapsed_time, result, body, answer, operation_type):
        super(Subject, self).__init__(which_angel, date, score, elapsed_time, result, body, answer)
        self.operation_type = operation_type
