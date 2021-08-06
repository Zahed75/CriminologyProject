from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from Criminology_App.models import (Home,About, Eventlist, Teacher_Detail, TeacherList,
        Gallery,Event_Detail, UpcomingEvents, Program, ChairmanMessage, HeaderAndFooter,
        Facilite, Facilites_details,Research_Publication,Seminar_Lab,Computer_Lab,Crime_Lab,Bss_syllabus,Mss_syllabus,Mphil_phd,NewEvent)

# Register your models here.
admin.site.register(Home)


class FaciliteModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Facilite, FaciliteModelAdmin)



class Research_PublicationModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Research_Publication, Research_PublicationModelAdmin)




class Facilites_detailsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Facilites_details, Facilites_detailsModelAdmin)


class UpcomingEventsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(UpcomingEvents, UpcomingEventsModelAdmin)


class AboutModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(About, AboutModelAdmin)


class EventlistModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Eventlist, EventlistModelAdmin)


class TeacherListModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(TeacherList, TeacherListModelAdmin)


class Teacher_DetailModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Teacher_Detail, Teacher_DetailModelAdmin)

admin.site.register(Gallery)


class Event_DetailModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Event_Detail, Event_DetailModelAdmin)


class ProgramModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Program, ProgramModelAdmin)


class ChairmanMessageModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(ChairmanMessage, ChairmanMessageModelAdmin)

class Seminar_LabModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Seminar_Lab, Seminar_LabModelAdmin)


class Computer_LabModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Computer_Lab, Computer_LabModelAdmin)


class Crime_LabModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Crime_Lab, Crime_LabModelAdmin)


class Bss_syllabusModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Bss_syllabus, Bss_syllabusModelAdmin)

class Mss_syllabusModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Mss_syllabus, Mss_syllabusModelAdmin)


class Mphil_phdModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Mphil_phd, Mphil_phdModelAdmin)

admin.site.register(HeaderAndFooter)



class NewEventModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(NewEvent, NewEventModelAdmin)