from django.shortcuts import redirect, render

from data.forms import CreateStudentForm,UpdateStudentForm
from data.models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request, 'home.html', {'student':student})


def student(request, student_id):
    student = Student.objects.all()
    return render(request, 'new_student.html', {'student':student})



def create_student(request):
    if request.method == 'POST':
        create_student_form = CreateStudentForm(request.POST, request.FILES)
        if create_student_form.is_valid():
            student = create_student_form.save(commit=False)
            student.save()
        return redirect('home')
    else:
        create_student_form = CreateStudentForm()
    return render(request, 'new_student.html', {'create_student_form': create_student_form})

def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        update_student_form = UpdateStudentForm(request.POST,request.FILES, instance=student)
        if update_student_form.is_valid():
            update_student_form.save()
            messages.success(request, f'Post updated!')
            return redirect('home')
    else:
        update_student_form = UpdateStudentForm(instance=student)

    return render(request, 'update_student.html', {"update_student_form":update_student_form})


def delete_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    if student:
        student.delete_student()
    return redirect('home')
