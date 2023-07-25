from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    dropdown = models.CharField(max_length=100, choices=[
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ])
    check_box = models.BooleanField()

    def __str__(self):
        return self.name