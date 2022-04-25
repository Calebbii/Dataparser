from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField() 
    contact = models.IntegerField(null=True,blank = True)

    def create_student(self):
        self.save()

    def delete_student(self):
        self.delete()
        
    def __str__(self):
        return self.first_name