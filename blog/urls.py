from django.urls import path

from .views import (change_user, create_user, delete_user, update_user,
                    user_list)

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', create_user, name='create'),
    path('delete/',delete_user , name='delete'),
    path('update/', update_user, name='update'),
    path('change/<int:user_id>/', change_user, name='change'),

    
]