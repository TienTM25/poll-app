from django.contrib import admin
from .models import Member
from .models import School
from .models import Department
from .models import Class_room
from .models import Student_class

# Register your models here.
admin.site.register(Member)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Class_room)
admin.site.register(Student_class)