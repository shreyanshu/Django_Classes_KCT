"""kct_demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student_mgmt_system import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add_cord/', views.add_cord),
    path('update_cord/<int:id>/', views.update_cord, name='update_cord'),
    path('list_cord/', views.ListCord.as_view(), name='list_cord'),
    path('delete_cord/<int:id>/', views.DeleteCordView.as_view(), name='delete_cord')
]
