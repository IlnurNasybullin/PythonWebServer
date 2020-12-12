from django.shortcuts import render, redirect
from .models import Post, get_posts, Student, get_students
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import PostForm, StudentForm

def post_list(request):
    return render(request, 'index.html', {})

def about_info(request):
    return render(request, 'about_info.html', {})

def index(request):
    search_query = request.GET.get('search', '')
    posts = get_posts(search_query)
    return render(request, 'posts/post_list.html', {"posts": posts})

def save(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index_list')
    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})

def edit_student(request, id):
    try:
        student = Student.objects.get(id=id)

        if request.method == "POST":
            student.group = request.POST.get("group")
            student.name = request.POST.get("name")
            student.lastname = request.POST.get("lastname")
            student.age = request.POST.get("age")
            student.hobbies = request.POST.get("hobbies")
            student.save()
            return redirect('students')
        else:
            return render(request, "students/edit_student.html", {"student": student})
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Student are not found</h2>")


def students(request):
    search_query = request.GET.get('search', '')
    students = get_students(search_query)
    return render(request, 'students/students_list.html', {"students": students})


def remove_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('students')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")