from django import forms
from .models import School
from .models import Department
from .models import Class_room
from .models import Member

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'establish_day', 'volume', 'location']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'volume', 'school']
        

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Class_room
        fields = ['name', 'volume', 'department']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'password', 'date_of_birth', 'prefecture', 'type']
