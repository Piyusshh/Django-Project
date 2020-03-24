from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
# above line needs to be imported for the user custom registration and user custm edit form
# Create your views here.
# it contains logic


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.decorators import login_required

#def homex(request):
#    numbers = [1,2,3,4,5]
#    name = 'Max Goodridge'
#    args = {'myname': name, 'numbers': numbers} # html code me my name pass karna hoga
#
#    return render(request,'accounts/login.html',args)


#@login_required
#def home(request):
#    numbers = [1, 2, 3, 4, 5]
#    name = 'Max Goodridge'
#    # html code me my name pass karna hoga
#    args = {'myname': name, 'numbers': numbers}
#
#    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    else:
        #form = UserCreationForm()
        form = RegistrationForm()

    args = {'form': form}
    return render(request,'accounts/reg_form.html', args)

#login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request,'accounts/profile.html',args)

#login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,'accounts/edit_profile.html',args)



#login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:view_profile')
        else:
            return redirect('accounts:change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request,'accounts/change_password.html', args)
