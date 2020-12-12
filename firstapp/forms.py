from django import forms
from .models import Post, Student


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('group', 'name', 'name', 'age', 'hobbies')