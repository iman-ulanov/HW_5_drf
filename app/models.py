from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=40)
    date_birth = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.date_birth}'


class Mentor(models.Model):
    name = models.CharField(max_length=40)
    experience = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.experience}'




class Course(models.Model):
    name = models.CharField(max_length=40)
    month = models.IntegerField()
    student = models.ManyToManyField(Student)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)


    def __str__(self):
        return f'На курсе {self.name} учатся {self.student}'

