from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sondage(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    sondage_title = models.CharField(max_length=300)
    propostion_nom = models.CharField(max_length=300)
    sondage_content = models.TextField()
    vote_yes = models.IntegerField(default=0)
    vote_no = models.IntegerField(default=0)
    vote_null = models.IntegerField(default=0)
    sondage_image = models.ImageField(upload_to='sondage_img/')
    created = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('sondage:sondage-view', args=[str(self.id)])

    # def user_can_vote(self, user):
    #     """ 
    #         Return False if user already voted
    #     """
    #     user_votes = user.vote_set.all()
    #     qs = user_votes.filter(poll=self)
    #     if qs.exists():
    #         return False
    #     return True

    # @property
    # def get_vote_count(self):
    #     return self.vote_set.count()

    def total(self):
        return self.vote_yes + self.vote_no + self.vote_null

    def __str__(self):
        return self.sondage_title
