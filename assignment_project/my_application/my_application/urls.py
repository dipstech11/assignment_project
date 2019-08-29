from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('user_profile.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
