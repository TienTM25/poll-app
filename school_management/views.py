from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import School, Department, Class_room, Member, Student_class
from django.http import Http404
from .form import SchoolForm, DepartmentForm, ClassroomForm, MemberForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
# School View
def index(request):
    school_list = School.objects.order_by('-modified_at')
    context = {
        'school_list': school_list,
    }
    return render(request, 'school/index.html', context)

def detail(request, school_id):
    try:
        school = School.objects.get(pk=school_id)
    except School.DoesNotExist:
        raise Http404("School does not exist")
    return render(request, 'school/detail.html', {'school': school})

def add(request):
    context = {}
    form = SchoolForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/school")
    context['form']= form
    return render(request, 'school/add.html', {'form': form})

def edit(request, school_id):
    school = School.objects.get(id=school_id)  
    return render(request,'school/update.html', {'school':school})  

def update(request, school_id):
    school_update = get_object_or_404(School, id = school_id)
    form = SchoolForm(request.POST, instance = school_update)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/school")
    return render(request, 'school/update.html', {'school': school_update})

def delete(request, school_id):
    school_delete = get_object_or_404(School, id = school_id)
    school_delete.delete()
    return HttpResponseRedirect("/school")

# Department View
def department_index(request):
    dep_list = Department.objects.order_by('-modified_at')
    context = {
        'dep_list': dep_list,
    }
    return render(request, 'department/index.html', context)

def department_detail(request, department_id):
    try:
        department = Department.objects.get(pk=department_id)
    except School.DoesNotExist:
        raise Http404("Department does not exist")
    return render(request, 'department/detail.html', {'department': department})

def department_add(request):
    form = DepartmentForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        school = School.objects.get(id=form_data['school'].id)
        if form_data['volume'] < school.volume:
            member = Member.objects.get(id='1')
            # d1 = form.save(commit=False)
            # d1.created_by = member
            # d1.save()
            department = Department(name=form_data['name'], volume=form_data['volume'], school=form_data['school'], created_by=member)
            department.save()
            return HttpResponseRedirect("/school/department")
        messages.error(request, 'Department volume cannot exceed School volume')
        return render(request, 'department/add.html', {'form': form})
    return render(request, 'department/add.html', {'form': form})

def department_edit(request, department_id):
    department = Department.objects.get(id=department_id)  
    school = School.objects.all()
    return render(request,'department/update.html', {'department': department, 'school': school})  

def department_update(request, department_id):
    department_update = get_object_or_404(Department, id = department_id)
    school_update = School.objects.get(id = request.POST.get("school_name"))
    department_update.name = request.POST.get("name")
    department_update.volume = request.POST.get("volume")
    department_update.school = school_update
    department_update.save()
    return HttpResponseRedirect("/school/department")

def department_delete(request, department_id):
    department_delete = get_object_or_404(Department, id = department_id)
    department_delete.delete()
    return HttpResponseRedirect("/school/department")

# Class View
def class_index(request):
    class_room = Class_room.objects.order_by('-modified_at')
    context = {
        'class': class_room,
    }
    return render(request, 'class/index.html', context)

def class_detail(request, class_id):
    try:
        class_room = Class_room.objects.get(pk=class_id)
    except Class_room.DoesNotExist:
        raise Http404("Class does not exist")
    return render(request, 'class/detail.html', {'class': class_room})

def class_add(request):
    form = ClassroomForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        department = Department.objects.get(id=form_data['department'].id)
        if form_data['volume'] < department.volume:
            member = Member.objects.get(id='1')
            # d1 = form.save(commit=False)
            # d1.created_by = member
            # d1.save()
            class_add = Class_room(name=form_data['name'], volume=form_data['volume'], department=form_data['department'], created_by=member)
            class_add.save()
            return HttpResponseRedirect("/school/class")
        messages.error(request, 'Class volume cannot exceed Department volume')
        return render(request, 'class/add.html', {'form': form})
    return render(request, 'class/add.html', {'form': form})

def class_edit(request, class_id):
    class_room = Class_room.objects.get(id=class_id)  
    department = Department.objects.all()
    return render(request,'class/update.html', {'class': class_room, 'department': department})  

def class_update(request, class_id):
    class_update = get_object_or_404(Class_room, id = class_id)
    dep_update = Department.objects.get(id = request.POST.get("dep_name"))
    class_update.name = request.POST.get("name")
    class_update.volume = request.POST.get("volume")
    class_update.department = dep_update
    class_update.save()
    return HttpResponseRedirect("/school/class")

def class_delete(request, class_id):
    class_delete = get_object_or_404(Class_room, id = class_id)
    class_delete.delete()
    return HttpResponseRedirect("/school/class")

# Member View
def member_index(request):
    member = Member.objects.order_by('-modified_at')
    context = {
        'member': member,
    }
    return render(request, 'class/index.html', context)

def member_detail(request, class_id):
    try:
        member = Member.objects.get(pk=class_id)
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'member/detail.html', {'member': member})

def member_add(request):
    form = ClassroomForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        password = make_password(form_data['password'])
        member = Member(first_name=form_data['name'], last_name=form_data['last_name'], 
            email=form_data['email'], password=password, date_of_birth=form_data['date_of_birth'],
            prefecture=form_data['prefecture'] ,created_by='1', type=form_data['type'])
        member.save()
        return HttpResponseRedirect("/school/member")
    return render(request, 'class/add.html', {'form': form})

def member_edit(request, member_id):
    member = Member.objects.get(id=member_id)
    class_room = Class_room.objects.all()  
    return render(request,'class/update.html', {'class': class_room, 'member': member})  

def member_update(request, member_id):
    member_update = get_object_or_404(Member, id = member_id)
    class_update = Class_room.objects.get(id = request.POST.get("dep_name"))
    member_update.first_name = request.POST.get("first_name")
    member_update.last_name = request.POST.get("last_name")
    member_update.email = request.POST.get("email")
    member_update.password = request.POST.get("password")
    member_update.date_of_birth = request.POST.get("volume")
    member_update.prefecture = request.POST.get("prefecture")
    member_update.type = request.POST.get("type")
    member_update.save()
    studen_class = Student_class(student=member_update, department=class_update)
    studen_class.save()
    return HttpResponseRedirect("/school/class")

def member_delete(request, class_id):
    class_delete = get_object_or_404(Class_room, id = class_id)
    class_delete.delete()
    return HttpResponseRedirect("/school/class")