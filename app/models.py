from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Home(models.Model):
    # home_number = models.IntegerField(default=0, unique=True)
    home_title = models.CharField(max_length=100)
    home_description = models.CharField(max_length=300)
    home_image = models.ImageField(upload_to='home_img/')

    def __str__(self):
        return self.home_title


class Lois(models.Model):
    lois_title = models.CharField(max_length=300)
    propostion_nom = models.CharField(max_length=300)
    lois_content = models.TextField()
    lois_image = models.ImageField(upload_to='lois_img/')
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.lois_title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app:lois-view', args=[str(self.id)])


# Contact Form
class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objet_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=101)
    phone_num = models.CharField(max_length=15)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message de ' + self.first_name + ' ' + self.last_name

class ReseauSociaux(models.Model):
    rs_title = models.CharField(max_length=250)
    rs_url = models.URLField()
    rs_logo = models.ImageField(upload_to='socio_logo/')

    def __str__(self):
        return self.rs_title


class Comment(models.Model):
    comment_title = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lois = models.ForeignKey(Lois, on_delete=models.CASCADE, related_name='comment', null=True)
    comment = models.TextField(max_length=800, null=True)
    created = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return "{}".format(self.comment_title)
