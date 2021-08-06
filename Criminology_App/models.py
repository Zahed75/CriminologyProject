from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Home(models.Model):
    slider_one = models.ImageField(upload_to='profile_pics')
    slider_two = models.ImageField(upload_to='profile_pics')
    slider_three = models.ImageField(upload_to='profile_pics')

    class Meta:
        ordering = ['-slider_one', ]


class ChairmanMessage(models.Model):
    departmnent_intro = models.TextField(max_length=4000, verbose_name='Put here department introduction')
    chairman_name = models.TextField(max_length=120, verbose_name='write here chariman Name')
    chairman_role = models.TextField(max_length=300, verbose_name='write hete chairman Role detials')
    chairman_img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.chairman_name


class Facilite(models.Model):
    facilites_title = models.TextField(max_length=700, verbose_name='Put your facilites title here')
    facilites_img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.facilites_title


class Facilites_details(models.Model):
    title = models.ForeignKey(Facilite, on_delete=models.CASCADE)
    details = models.TextField(max_length=30000, verbose_name='Put here facilites details')

    def __str__(self):
        return str(self.title)


class Program(models.Model):
    program_name = models.TextField(max_length=400, verbose_name='put here program Heading', blank=True)
    program_details = models.TextField(max_length=1000, verbose_name='put here program Heading', blank=True)

    def __str__(self):
        return self.program_name


class UpcomingEvents(models.Model):
    event_title = models.TextField(max_length=400, verbose_name='write here Event tile')
    event_date = models.CharField(max_length=20, verbose_name='put here date')
    event_details = models.TextField(max_length=1000, verbose_name='Put here event details')
    event_img = models.ImageField(upload_to='gallery')
    event_file = models.FileField(upload_to='event_docx')

    def __str__(self):
        return self.event_title


class About(models.Model):
    about_image = models.ImageField(upload_to='profile_pics')
    about_details = models.TextField(max_length=10000, verbose_name='Put here About Deatils')
    mission_title = models.TextField(max_length=1000, verbose_name='write here your mission title')
    mission_details = models.TextField(max_length=10000, verbose_name='write here mission details')

    def __str__(self):
        return self.about_details


class Eventlist(models.Model):
    events_title = models.CharField(max_length=333, verbose_name='Put a Event title here')
    events_img = models.ImageField(upload_to='profile_pics')
    events_date = models.CharField(max_length=120, verbose_name='Put here static date')

    def __str__(self):
        return self.events_title


class Event_Detail(models.Model):
    event_title = models.ForeignKey(Eventlist, on_delete=models.CASCADE)
    events_details = models.TextField(max_length=3000, verbose_name='Put a event details here')

    def __str__(self):
        return str(self.event_title)


class TeacherList(models.Model):
    teacher_name = models.CharField(max_length=212, verbose_name='Put a teacher name')
    teacher_img = models.ImageField(upload_to='profile_pics')
    teacher_designation = models.TextField(max_length=400, verbose_name='Put a teacher designation here')
    teacher_fb = models.URLField(max_length=200, verbose_name='Put here teacher Facebook id link')
    teacher_twitter = models.URLField(max_length=200, verbose_name='Put here teacher twitter id link')
    teacher_linkldn = models.URLField(max_length=200, verbose_name='Put here teacher Linkldn id link')

    def __str__(self):
        return self.teacher_name


class Teacher_Detail(models.Model):
    teacher_name = models.ForeignKey(TeacherList, on_delete=models.CASCADE)
    teacher_subjetct = models.TextField(max_length=600, verbose_name='Put which subject are you taken')
    research_interest = models.TextField(max_length=700, verbose_name='put here your reaserach and interest')
    teacher_cv = models.FileField(upload_to='Cv', blank=False)

    def __str__(self):
        return str(self.teacher_name)


class Research_Publication(models.Model):
    research_title = models.TextField(max_length=1000, verbose_name='Write here research title', blank=True)
    research_details = models.TextField(max_length=10000, verbose_name='Write here research details', blank=True)

    def __str__(self):
        return self.research_title


class Gallery(models.Model):
    img_one = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_two = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_three = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_four = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_five = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_six = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_seven = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)
    img_eight = models.ImageField(upload_to='gallery', verbose_name='Drop a Image', blank=False)

    def __str__(self):
        return str(self.img_one)


class Seminar_Lab(models.Model):
    seminar_image = models.ImageField(upload_to='gallery', verbose_name='image size should be', blank=False)
    seminar_details = models.TextField(max_length=10000, verbose_name='write here seminar details')

    def __str__(self):
        return self.seminar_details


class Computer_Lab(models.Model):
    lab_image = models.ImageField(upload_to='gallery', verbose_name='image size should be', blank=False)
    lab_details = models.TextField(max_length=10000, verbose_name='write here seminar details')

    def __str__(self):
        return self.lab_details


class Crime_Lab(models.Model):
    lab_image = models.ImageField(upload_to='gallery', verbose_name='image size should be', blank=False)
    lab_details = models.TextField(max_length=10000, verbose_name='write here seminar details')

    def __str__(self):
        return self.lab_details


class Bss_syllabus(models.Model):
    syllabus_file = models.FileField(upload_to='syllabus', verbose_name='Upload here any file')

    def __str__(self):
        return str(self.syllabus_file)


class Mss_syllabus(models.Model):
    syllabus_file = models.FileField(upload_to='syllabus', verbose_name='Upload here any file')

    def __str__(self):
        return str(self.syllabus_file)


class Mphil_phd(models.Model):
    syllabus_file = models.FileField(upload_to='syllabus', verbose_name='Upload here any file')

    def __str__(self):
        return str(self.syllabus_file)


class HeaderAndFooter(models.Model):
    phone_number = models.CharField(max_length=100)
    facebook_link = models.URLField(max_length=100, verbose_name='Facebook Link')
    twitter_link = models.URLField(max_length=100, verbose_name='Twitter Link')
    google_link = models.URLField(max_length=100, verbose_name='Google Plus Link')
    linkedin_link = models.URLField(max_length=100, verbose_name='LinkedIn Link')
    instagram_link = models.URLField(max_length=100, verbose_name='Instagram Link')

    def __str__(self):
        return str(self.id)

