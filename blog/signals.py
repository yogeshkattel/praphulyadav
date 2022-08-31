from django.contrib.auth.signals import user_logged_in, user_logged_out

from django.dispatch import receiver

@receiver(user_logged_in)
def user_signed_in(sender, user, request,**kwags):
  print('hello wortld')
  notify.send(user, recipient=user, verb="You signed in")


@receiver(user_logged_out)
def user_signed_out(request, user, **kwargs): 
  print('hello wortld')   

