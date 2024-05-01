from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from .forms import UserForm
from .models import User


def create_user(request):#creating a new user
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): #if the data is valid then save in the database
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'create.html', {'form': form})


def user_list(request):# display list of users
    users = User.objects.all()
    for user in users:
        print(user.id)
    return render(request, 'user_list.html', {'users': users})

#new user list display
def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        
        #pk is primary key retrieved form the data basae
        #get_object_or_404 is error 404 if user id does not exist
        user = get_object_or_404(User, pk=user_id)
        form = UserForm(request.POST, instance=user)
    else:
        users = User.objects.all()
        form = UserForm()
    return render(request, 'update.html', {'form': form, 'users': users})



#this change actually change the user details
def change_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        #if the data is valid then save in the database
        if form.is_valid():
            form.save()
            return redirect('user_list')#redirect to the home page after successfull
    else:
        form = UserForm(instance=user)
        #unable to change email and username
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['username'].widget.attrs['readonly'] = True
    return render(request, 'change.html', {'form': form})



#delete user from list
def delete_user(request):
    if request.method == 'POST':
        user_ids = request.POST.getlist('user_ids')
        users_to_delete = User.objects.filter(pk__in=user_ids)
        
        #delete and delete form the database
        for user in users_to_delete:
            user.delete()
        
        return redirect('user_list')
    else:
        ## Retrieve all user objects from the database
        users = User.objects.all()
        return render(request, 'delete.html', {'users': users})
    

