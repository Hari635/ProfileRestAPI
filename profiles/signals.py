# the signal is used if the somemodel is creates it is automatically created the another model
# for example if you want to create the user model you want to create the simantanously create the user profile model 
#so signals will take care for that to create it automatically
#it will send the created argument this argument tell whether the user is created new or it is updated

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    print("created: ",created)
    if(created):
        Profile.objects.create(user=instance)
