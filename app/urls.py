from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app import views

urlpatterns=[
  path('', views.home, name='home'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('register',views.register,name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
