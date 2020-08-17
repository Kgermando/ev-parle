from django.db import models

# Create your models here.
class OurTeam(models.Model):
    team_name = models.CharField(max_length=55)
    team_designation = models.CharField(max_length=55)
    team_description = models.TextField()
    team_image = models.ImageField(upload_to='team_img/')
    # team_social = models.ForeignKey(ReseauSociaux, on_delete=models.CASCADE)
    team_facebook = models.URLField()
    team_twitter = models.URLField()
    team_linkedIn = models.URLField()
    team_instagram = models.URLField()
    team_youtube = models.URLField()
    team_created_date = models.DateTimeField(auto_now_add=True)
    team_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name
