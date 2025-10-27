from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'c'
        elif self.marks >= 40:
            return 'D'
        else:
            return 'Fail'
        
        
        
