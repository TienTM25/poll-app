from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    prefecture = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=20)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + self.last_name

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    establish_day = models.DateTimeField('date published')
    volume = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    volume = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

class Class_room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    volume = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

class Student_class(models.Model):
    student = models.ForeignKey(Member, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)