import random

#验证码




from django.contrib import auth
from django.core.paginator import Paginator

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
# Create your views here.
from django.utils import timezone

from App.eml_token import token_confirm
from App.forms import RegisterForm
from App.models import Article, Category, UserComment, User
from Django_Projects import settings


def index(request):

    #最近三篇展示
    articles1 = Article.objects.filter().order_by('-create_time').all()[:3]
    #指定三篇展示
    articles = Article.objects.filter(aid__in = (2,100,4))

    return render(request,'index.html',locals())


def blog(request, page=1):
    articles1 = Article.objects.filter().order_by('-create_time').all()[:3]
    categorys = Category.objects.filter().all()
    categories = Category.objects.all()

    if(request.method == 'POST'):
        search = request.POST['search']
        #搜索
        articless = Article.objects.filter(title__contains=search)

    else:
        articless = Article.objects.filter().all()

    paginator = Paginator(articless, 8)

    pager = paginator.page(page)

    #总的文章个数
    pa_count = paginator.count
    #总的页码
    pa_all = paginator.num_pages

    li1 = pager.object_list[::2]
    li2 = pager.object_list[1::2]

    pa_num = range(1,paginator.num_pages+1)

    return render(request,'blog.html',locals())


def loginb(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username , password = password)
        if user:
            request.session['username'] = username
            login(request, user)
            return redirect('App:index')

        else:
            return render(request, 'login.htm', {'msg': '用户名或密码错误'})
    else:
        return render(request, 'login.htm')




def post(request,aid=1):
    articles1 = Article.objects.filter().order_by('-create_time').all()[:3]
    categorys = Category.objects.filter().all()

    article = Article.objects.filter(aid=aid).first()

    art_last = Article.objects.order_by('aid').last()

    u_comment = UserComment.objects.filter(aid=aid)


    if aid < art_last.aid:
        if aid == 1:
            Bid = aid
        else:
            Bid = aid - 1
        bid = aid + 1
    else:
        Bid = aid - 1
        bid = aid

    u_comment = UserComment.objects.filter(aid=aid)


    #创建评论
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.session.get('username')
        usercomment = request.POST.get('usercomment')
        user = User.objects.filter(username=username).first()
        uid = user.uid
        UserComment.objects.create(u_comment=usercomment, aid=aid, uid=uid, u_name=username)


    return render(request,'post.html',locals())


def zhuce(request):
        if request.method == 'POST':

            form = RegisterForm(request.POST)
            #验证表单
            if form.is_valid():

                data = form.cleaned_data
                data.pop('confirm')
                u = User.objects.filter(username=data['username'])
                if u:

                    return render(request,'注册.htm',{'msg':'用户名已存在'})
                user = User.objects.create_user(**data)
                if user:

                    return redirect('App:loginb')

        return render(request, '注册.htm', locals())





def logoutb(request):
    logout(request)

    return redirect('App:loginb')


# def cap(request):
#
#
#     return render(request,'asd.html')


# def output_yzm(request):
#     if request.method == "POST":
#         yzm = request.POST.get('yzm','')
#         hashkey = request.POST.get('code')
#         # 根据key获取验证码对象
#         cap = CaptchaStore.objects.filter(hashkey=hashkey).first()
#         if cap:
#             if cap.response == yzm.lower():
#                 return HttpResponse("验证成功")
#         return HttpResponse("验证失败")
#     else:
#         # 生成hashkey和image_url
#         new_key = CaptchaStore.pick()
#         image_url = captcha_image_url(new_key)
#
#         return render(request,'注册.htm',locals())


def mail_send(request):
    if request.method == 'POST':
        # send_mail('账户激活','',settings.EMAIL_FROM, ['718795325@qq.com'])
        token = token_confirm.generate_validate_token(User.uid)
        # print(token)
        return HttpResponse('ok')


    return render(request, 'asd.html',locals())