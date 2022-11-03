from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:school_id>/', views.detail, name='school_detail'),
    path('add/', views.add, name='school_add'),
    path('edit/<int:school_id>/', views.edit, name='school_edit'),
    path('update/<int:school_id>/', views.update, name='school_update'),
    path('delete/<int:school_id>/', views.delete, name='school_delete'),
    path('department', views.department_index, name='index'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('department/add/', views.department_add, name='department_add'),
    path('department/edit/<int:department_id>/', views.department_edit, name='department_edit'),
    path('department/update/<int:department_id>/', views.department_update, name='department_update'),
    path('department/delete/<int:department_id>/', views.department_delete, name='department_delete'),
    path('class', views.class_index, name='index'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('class/add/', views.class_add, name='class_add'),
    path('class/edit/<int:class_id>/', views.class_edit, name='class_edit'),
    path('class/update/<int:class_id>/', views.class_update, name='class_update'),
    path('class/delete/<int:class_id>/', views.class_delete, name='class_delete'),
    path('member', views.member_index, name='index'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('member/add/', views.member_add, name='member_add'),
    path('member/edit/<int:member_id>/', views.member_edit, name='member_edit'),
    path('member/update/<int:member_id>/', views.member_update, name='member_update'),
    path('member/delete/<int:member_id>/', views.member_delete, name='member_delete'),
    
]