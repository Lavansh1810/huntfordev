from django.contrib.auth.models import User
from django.core.mail import send_mail
from users.forms import ProfileForm
from .models import Profile
from django.db.models.signals import post_save,post_delete
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    # print("Profile Saved")
    # print('Instance', instance)
    # print('Created', created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name= user.first_name,
            email=user.email,
            username=user.username,
        )
        
        subject = 'Welcome to Hunt For Developer'
        message = 'Thank you for creating an with huntdev.herokuapp.com. We hope you\'ll like our services.'
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )



def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False: 
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username

        user.save()


def deleteUser(sender, instance, **kwargs):
    user=instance.user
    user.delete()



post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
post_save.connect(updateUser, sender = Profile)