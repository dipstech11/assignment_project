from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('userlist/', login_required(views.UserList.as_view()), name='user_list'),
    path('userlist/<int:pk>', login_required(views.UserDetailView.as_view()), name='user_detail'),
]
