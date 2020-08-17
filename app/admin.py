from django.contrib import admin

from app.models import Home, Lois, ReseauSociaux, ContactForm, Comment

# Register your models here.
admin.site.register(Home)
admin.site.register(Lois)
admin.site.register(ReseauSociaux)
admin.site.register(ContactForm)
admin.site.register(Comment)
