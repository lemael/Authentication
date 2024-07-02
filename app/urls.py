from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
  path('', views.home, name='home'),
  path('login',views.logIn,name='login'),
  path('logout',views.logOut,name='logout'),
  path('register',views.register,name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

