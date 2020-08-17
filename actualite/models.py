from django.db import models

# Create your models here.
class Actualite(models.Model):
    actu_title = models.CharField(max_length=300)
    propostion_nom = models.CharField(max_length=300)
    actu_content = models.TextField()
    actu_image = models.ImageField(upload_to='actu_img/')
    created = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('actualite:actualite-view-detail', args=[str(self.id)])

    def __str__(self):
        return self.actu_title
    
