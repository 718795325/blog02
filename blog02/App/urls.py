"""blog_pre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path

from App import views
app_name = 'App'
urlpatterns = [
    path('index/', views.index,name='index'),
    #分页查询
    path('blog/', views.blog,name='blog'),
    path('blog/<int:page>/', views.blog,name='blog'),
    # path('blog/<int:cid>/<int:page>/',views.blog,name='blog'),

    path('loginb/', views.loginb, name='loginb'),
    path('logoutb/', views.logoutb, name= 'logoutb'),

    path('post/', views.post,name='post'),
    path('post/<int:aid>/', views.post,name='post'),
    # path('post/<int:aid>/<int:cid>/', views.post,name='post'),
    path('zhuce/', views.zhuce,name='zhuce'),

    path('send/',views.mail_send,name='send'),

    # path('cap/', views.cap,name= 'cap'),

    # path('yzm/',views.user_login,name='yzm'),
    # path('yzm/', views.output_yzm,name= 'output_yzm'),




]
