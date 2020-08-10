from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .. forms import UserUpdateForm

def profile(request):
	if request.method =='POST':
		form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile is updated with success')
			return redirect('profile')
		else:
			messages.info(request, 'Something wrong happened fail')
	else:
		form = UserUpdateForm(instance=request.user)
	return render(request,'classroom/profile.html',{'form':form})


def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(request.POST, request.user)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request, 'password is changed with success')
			return redirect('profile')
		else:
			messages.info(request, 'Profile is updated with success')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'classroom/change_password.html',{'form':form})