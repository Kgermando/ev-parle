from django.db import models

# Create your models here.
class Actualite(models.Model):
    actu_title = models.CharField(max_length=300)
    lois_content = models.TextField()
    actu_image = models.ImageField(upload_to='actu_img/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.actu_title