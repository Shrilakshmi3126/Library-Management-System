"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path,include
from signup import views
from django.conf.urls.static import static
#from signup.views import sigaction
from login.views import welcome,ad_logaction,student_logaction,question,bscience,comis,mechanical,civil,ec,maths,table,fadmin,firstadminpg,adminm,insertbook,deletebook,UpdBook,Supload,Sregister,Stlist,semCI3,semCI4,semCI5,semCI6,semCI7,semCI8,semCIV3,semCIV4,semCIV5,semCIV6,semCIV7,semCIV8,semME3,semME4,semME5,semME6,semME7,semME8,semECE3,semECE4,semECE5,semECE6,semECE7,semECE8,display_book,logbook,lending_books,display_book1

urlpatterns = [
    
    #url(r'^signup/',sigaction),
    #path('admin/', admin.site.urls),
    #path('signup_page.html', views.sigaction, name='signup_page'),
    #path(r'^$', views.sigaction, name='sigaction'),
    #path('signup/',views.sigaction),
    #path('',logaction),
    path('', welcome, name='welcome'),
    #path('upload',views.upload,name='upload'),
    
    path('admin_login', ad_logaction, name='adminlogin'),
    path('error', ad_logaction, name='error'),
    path('adminm', adminm, name='adminm'),
    #path('welcome_admin', ad_logaction, name='welcomeadmin'),
    #path('signup_page', sigaction, name='signup'),
    #path('admin_login', ad_logaction, name='adminlogin'),
    path('student_login', student_logaction, name='studentlogin'),
    path('student_page', student_logaction, name='studentpage'),
    
   # path('student_page', display_book, name='studentpage'),
    path('question_paper', question, name='qp'),
    path('basic_science', bscience, name='bs'),
    path('com_is', comis, name='ci'),
    path('mech', mechanical, name='me'),
    path('civil', civil, name='civ'),
    path('ec', ec, name='ece'),
    path('maths', maths, name='math'),
    #path('table', table, name='table'),
    path('fadmin', fadmin, name='fadmin'),
    path('firstadminpg', firstadminpg, name='firstadminpg'),
    path('insertbook', insertbook, name='insertbook'),
    path('deletebook', deletebook, name='deletebook'),
    path('UpdBook',UpdBook, name='UpdBook'),
    path('Supload',Supload, name='Supload'),
    path('Sregister', Sregister, name='Sregister'),
    path('Stlist', Stlist, name='Stlist'),
    path('3semCI', semCI3, name='3semCI'),
    path('4semCI', semCI4, name='4semCI'),
    path('5semCI', semCI5, name='5semCI'),
    path('6semCI', semCI6, name='6semCI'),
    path('7semCI', semCI7, name='7semCI'),
    path('8semCI', semCI8, name='8semCI'),
    path('3semCIV', semCIV3, name='3semCIV'),
    path('4semCIV', semCIV4, name='4semCIV'),
    path('5semCIV', semCIV5, name='5semCIV'),
    path('6semCIV', semCIV6, name='6semCIV'),
    path('7semCIV', semCIV7, name='7semCIV'),
    path('8semCIV', semCIV8, name='8semCIV'),
    path('3semME', semME3, name='3semME'),
    path('4semME', semME4, name='4semME'),
    path('5semME', semME5, name='5semME'),
    path('6semME', semME6, name='6semME'),
    path('7semME', semME7, name='7semME'),
    path('8semME', semME8, name='8semME'),
    path('3semECE', semECE3, name='3semECE'),
    path('4semECE', semECE4, name='4semECE'),
    path('5semECE', semECE5, name='5semECE'),
    path('6semECE', semECE6, name='6semECE'),
    path('7semECE', semECE7, name='7semECE'),
    path('8semECE', semECE8, name='8semECE'),
    path('table',display_book,name='table'),
    path('checkin', logbook, name='checkin'),
    path('table1',lending_books, name='table1'),
   path('displayLib',display_book1,name='displayLib'),
    #path('table1', lending_books, name='stu'),
    #path('student_page', student_logaction, name='welcomestudent'),
    #re_path(r'^signup_page/',sigaction),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
