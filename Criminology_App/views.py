import os.path
from django.db import models
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from Criminology_App.forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from Criminology_App.models import (Home, About, Eventlist, Teacher_Detail,
                                    TeacherList,
                                    Gallery, Event_Detail, UpcomingEvents, Program,
                                    ChairmanMessage, Facilite, Facilites_details,
                                    Research_Publication, Seminar_Lab, Computer_Lab, Crime_Lab, Bss_syllabus,
                                    Mss_syllabus,Mphil_phd, Event_Detail, Past_Eventlist)


# Create your views here.

def index(request):
    home = Home.objects.all()
    fc = Facilite.objects.all()
    up_events = UpcomingEvents.objects.all()
    program = Program.objects.all()
    welcome = ChairmanMessage.objects.all()
    dict = {'home': home, 'up_events': up_events, 'program': program, 'welcome': welcome, 'fc': fc}
    return render(request, 'Criminology_App/index.html', context=dict)


def facilites(request, pk):
    exp = Facilites_details.objects.get(title_id=pk)
    expp = Facilite.objects.get(id=pk)
    dict = {'exp': exp, 'expp': expp}
    return render(request, 'Criminology_App/feature_details.html', context=dict)


def about(request):
    about = About.objects.all()
    dict = {'about': about}
    return render(request, 'Criminology_App/about.html', context=dict)


# =============Send mail
class Contact(TemplateView):
    template_name = './Criminology_App/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message = "From: " + email + "/n"  " " + message

        mail = EmailMessage(subject, message, to=[settings.EMAIL_HOST_USER])
        mail.content_subtype = 'html'
        mail.send()
        return render(request, './Criminology_App/contact.html', context={})


# ==========Send mail


def research_publication(request):
    rp = Research_Publication.objects.all()

    dict = {'rp': rp}
    return render(request, 'Criminology_App/ResearchPublication.html', context=dict)


def gallery(request):
    img = Gallery.objects.all
    dict = {'img': img}
    return render(request, 'Criminology_App/gallery.html', context=dict)


def course(request):
    dict = {}
    return render(request, 'Criminology_App/courses.html', context=dict)


def course_details(request):
    dict = {}
    return render(request, 'Criminology_App/course-details.html', context=dict)


def events(request):
    pt_event = Past_Eventlist.objects.all()
    events_list = Eventlist.objects.all()
    dict = {'events_list': events_list, 'pt_event': pt_event}
    return render(request, 'Criminology_App/events.html', context=dict)


def event_details(request, pk):
    event_info = Event_Detail.objects.get(event_title_id=pk)
    single_event = Eventlist.objects.get(id=pk)
    dict = {'event_info': event_info, 'single_event': single_event}
    return render(request, 'Criminology_App/event-details.html', context=dict)

#
# def pastevent_details(request,pk):
#     pt_details=PastEvent_Detail.objects.get(event_title_id=pk)
#     pt_list=Past_Eventlist.objects.get(id=pk)
#     dict={'pt_details':pt_details,'  pt_list':  pt_list}
#     return render(request,'Criminology_App/past_event_details.html',context=dict)



def teacher_list(request):
    teacher_list = TeacherList.objects.all()
    dict = {'teacher_list': teacher_list}
    print('test', dict)
    return render(request, 'Criminology_App/faculty.html', context=dict)




def teacher_details(requests, pk):
    teacher_details = Teacher_Detail.objects.get(teacher_name_id=pk)
    teacher_data = TeacherList.objects.get(id=pk)
    print(teacher_details)
    dict = {'teacher_details': teacher_details, 'teacher_data': teacher_data}

    return render(requests, 'Criminology_App/card_details.html', context=dict)


def seminar_lab(request):
    smlab = Seminar_Lab.objects.all()
    dict = {'smlab': smlab}

    return render(request, 'Criminology_App/SeminarLab.html', context=dict)


def computer_lab(request):
    comp = Computer_Lab.objects.all()
    dict = {'comp': comp}

    return render(request, 'Criminology_App/Computer_Lab.html', context=dict)


def crime_lab(request):
    crm_lab = Crime_Lab.objects.all()
    dict = {'crm_lab': crm_lab}

    return render(request, 'Criminology_App/Crime_Lab.html', context=dict)


def bss(request):
    bs_syllabus = Bss_syllabus.objects.all()
    dict = {'bs_syllabus': bs_syllabus}

    return render(request, 'Criminology_App/B.S.S.html', context=dict)


def mss(request):
    mss_syllabus = Mss_syllabus.objects.all()
    dict = {'mss_syllabus': mss_syllabus}

    return render(request, 'Criminology_App/M.S.S.html', context=dict)


def mphil_phd(request):
    m_phd = Mphil_phd.objects.all()
    dict = {'m_phd': m_phd}

    return render(request, 'Criminology_App/Mphil_phd.html', context=dict)

# class past_event(TemplateView):
#     template_name = 'Criminology_App/events.html'


# def upload_cv(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = Upload_cv(request.POST)
#             cv_file = request.POST.get('cv_file')
#             cv_ins = Cv(name=request.user, cv_file=cv_file)
#             cv_ins.save()
#
#             return HttpResponse("<h1>Cv uploaded successfully</h1>")
#         else:
#             form = Upload_cv(initial={'name': request.user})
#
#         data = Cv.objects.all()
#         logged_in_user = request.user
#
#         dict = {'data': data, 'form': form, 'logged_in_user': logged_in_user}
#         return render(request, 'Criminology_App/resume.html', context=dict)
#     else:
#         return render(request, 'App_Login/login.html')

# class CvUpdate(View):
#     def get(self, request, id):
#         cv_ins = Cv.objects.get(pk=id)
#         form = Upload_cv(instance=cv_ins)
#         return render(request, 'Criminology_App/updatecv.html', {'form' : form})
#
#     def post(self, request, id):
#         cv_ins = Cv.objects.get(pk=id)
#         form = Upload_cv(request.POST, instance=cv_ins)
#         # if form.is_valid():
#         form.save()

# return render(request, 'Criminology_App/updatecv.html', {'form': form})
