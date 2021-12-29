from django.db import models

GENDERCHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
# Create your models here.
class Student_Data(models.Model):
    usn = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDERCHOICES,max_length=6,default=None)
    course = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Student_Data"
        verbose_name_plural = "Student_Datas"

    def __str__(self):
        return self.usn
