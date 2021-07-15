from django.conf.urls import url
from django.urls import path
from Criminology_App import views

app_name = 'Criminology_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('event/', views.events, name='event'),
    path('event_details/<int:pk>/', views.event_details, name='event_details'),
    path('research_publication/', views.research_publication, name='research_publication'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('course/', views.course, name='course'),
    path('course_details/', views.course_details, name='course_details'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher_details/<int:pk>/', views.teacher_details, name='teacher_details'),
    path('facilites/<int:pk>/',views.facilites,name='facilites'),
    path('seminar_lab/',views.seminar_lab,name='seminar_lab'),
    path('computer_lab/',views.computer_lab,name='computer_lab'),
    path('crime_lab/',views.crime_lab,name='crime_lab'),
    path('bss_syllabus/',views.bss,name='bss'),
    path('mss_syllabus/',views.mss,name='mss_syllabus'),

]
