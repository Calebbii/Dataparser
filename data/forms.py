from django import forms
from data.models import Student


class CreateStudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('first_name','last_name','contact','email')

class UpdateStudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('first_name','last_name','contact','email')