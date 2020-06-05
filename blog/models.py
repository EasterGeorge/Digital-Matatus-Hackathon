from django.conf import settings
from django.db import models
from django.utils import timezone

from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput

class Ushuhuda(models.Model):

    estate = models.CharField(max_length=200)
    sub_county = models.CharField(max_length=200)    

    def approve(self):
        self.save()

    def __str__(self):
        return self.estate

class Cases(models.Model):
    sub_county = models.CharField(max_length=50)
    number_of_cases = models.IntegerField()    

    def approve(self):
        self.save()

    def __str__(self):
        return self.sub_county

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    cover = models.ImageField(upload_to='images/', default= 'images/blue-1.png')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Resources(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contact = models.URLField(blank=True, max_length=128,)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 

areas= (('Kibera', 'Kangemi', 'Kayole', 'Embakasi', 'Buruburu', 'Mathare', 'Rongai', 'Kawangware', 'Huruma', 'Highrise', 'Embakasi', 'Baba Dogo','CBD'))
class Reports(models.Model):
    CHOICES = (
        ('CBD','CBD'),
        ( 'Kibera', 'Kibera'),
        ('Kangemi', 'Kangemi'),
        ('Kayole', 'Kayole'),
        ('Embakasi', 'Embakasi'),
        ('Buruburu', 'Buruburu'),
        ('Mathare', 'Mathare'),
        ('Rongai', 'Rongai'),
    )


    name = models.CharField(max_length=200)
    offense_description = models.TextField()
    station_from = models.CharField(max_length=50,choices=CHOICES, default='CBD')
    station_to = models.CharField(max_length=50, choices=CHOICES, default='CBD')
    sacco_name = models.CharField(max_length=200) 
    occurrence_date= models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_report = models.BooleanField(default=False)

    

    def approve(self):
        self.save()

    def __str__(self):
        return self.name

areas= (('Kibera', 'Kangemi', 'Kayole', 'Embakasi', 'Buruburu', 'Mathare', 'Rongai', 'Kawangware', 'Huruma', 'Highrise', 'Embakasi', 'Baba Dogo','CBD'))


