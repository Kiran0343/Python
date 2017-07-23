from django.conf.urls import include,url
from . import views


urlpatterns = [
    url(r'home/',views.home,name = 'home'),
    url(r'^signup',views.index,name = 'index'),
    url(r'^signin',views.index1,name = 'index1'),
    url(r'^welcome',views.welcome,name = 'welcome'),
]