from asyncio import constants
import email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,LoginForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
# import user
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created! Your ar now able to login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


# login with username and email classed based login system
class LoginView(View):
    # send login form with get request
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    def post(self, request):
        # login system with both username and email
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if username is email
        if '@' in username:
            print('email')
            # if username is email
            # authenticate user with email isntead of username
            user = User.objects.filter(email=username)
            if user.exists():

                user = authenticate(request, username=user.first().username, password=password)
            else:
                messages.error(request, "This email is not registered.")
                return redirect('login')


            
        else:

            user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
