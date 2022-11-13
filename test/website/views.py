from django.shortcuts import render, redirect
from website import models, forms
from django.contrib import messages
from datetime import datetime, timedelta, timezone
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def is_ajax(request):
    """
    This utility function is used, as `request.is_ajax()` is deprecated.

    This implements the previous functionality. Note that you need to
    attach this header manually if using fetch.
    """
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

def profile(request):
    if request.user.is_authenticated:
        profile = models.Profile.objects.get(user=request.user)
        return render(request, 'profile.html', locals())
    else:
        messages.add_message(request, messages.INFO, '請先登入')
        return redirect('/login/')

def password_reset_confirm(request, uidb64, token):
    return render(request, 'registration/password_reset_confirm.html')

def index(request):
    # login_active = "<div class='nav-bar'><a href='/login'>登入</a></div>"
    all_posts = models.Post.objects.all().order_by('-updated_at')
    paginator = Paginator(all_posts, per_page=5)
    page_num = int(request.GET.get('page', 1))
    # print(page_num, type(page_num))
    # print(paginator.num_pages, type(paginator.num_pages))
    if page_num > paginator.num_pages:
        raise Http404
    posts = paginator.page(page_num)
    if is_ajax(request):
        return render(request, 'post/_posts.html', locals())
    test = "首頁開發中"
    if request.user.is_authenticated:
        
        login_active = ""
    # else:
    #     return redirect('/login/')

    return render(request, 'index.html', locals())


@login_required(login_url='/login/')
def search(request):
    mode = 0
    # login_active = "<div class='nav-bar'><a href='/login'>登入</a></div>"
    if request.user.is_authenticated:
        if request.user.is_superuser:
            login_active = ""
            active1 = "selected-active"
            active2 = "selected"
            active3 = "selected"
            display1 = "block"
            display2 = "none"
            display3 = "none"
            if "search-name" in request.POST:
                search = request.POST['search-name']
                mode = 1
                active1 = "selected-active"
                active2 = "selected"
                active3 = "selected"
                display1 = "block"
                display2 = "none"
                display3 = "none"
            elif "search-bed" in request.POST:
                search = request.POST['search-bed']
                mode = 2
                active2 = "selected-active"
                active1 = "selected"
                active3 = "selected"
                display1 = "none"
                display2 = "block"
                display3 = "none"
            elif "search-all-name" in request.POST:
                search = request.POST['search-all-name']
                mode = 3
            elif "search-name-list" in request.POST:
                search = request.POST['search-name-list']
                mode = 3
                active3 = "selected-active"
                active1 = "selected"
                active2 = "selected"
                display1 = "none"
                display2 = "none"
                display3 = "block"
            if mode == 1:
                try:
                    member_list = models.Member_info.objects.filter(name__contains=search)
                except:
                    member_list = None

            elif mode == 2:
                try:
                    member_info = models.Member_info.objects.get(bed=search)
                    title = ["照片", "房間", "床號", "班級", "學號", "姓名", "身分證號碼",
                            "生日", "電話", "家電", "戶籍地址", "緊急聯絡人", "緊急聯絡人電話"]
                    img = "https://tipfile.takming.edu.tw/stuphoto/" + member_info.student_ID + ".jpg"
                    data = [img, member_info.room, member_info.bed, member_info.member_class, member_info.student_ID, member_info.name, member_info.ID_number,
                            member_info.birthday, member_info.phone, member_info.home_phone, member_info.address, member_info.emergency_contact, member_info.emergency_contact_phone]
                    search_data = zip(title, data)
                except:
                    member_info = None

            elif mode == 3:
                try:
                    member_info = models.Member_info.objects.get(name=search)
                    title = ["照片", "房間", "床號", "班級", "學號", "姓名", "身分證號碼",
                            "生日", "電話", "家電", "戶籍地址", "緊急聯絡人", "緊急聯絡人電話"]
                    img = "https://tipfile.takming.edu.tw/stuphoto/" + member_info.student_ID + ".jpg"
                    data = [img, member_info.room, member_info.bed, member_info.member_class, member_info.student_ID, member_info.name, member_info.ID_number,
                            member_info.birthday, member_info.phone, member_info.home_phone, member_info.address, member_info.emergency_contact, member_info.emergency_contact_phone]
                    search_data = zip(title, data)
                except:
                    member_info = None
        else:
            return redirect('/login/')
    return render(request, 'search.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, '已登出')
    return redirect('/')

def showpost(request, slug):
    try:
        post_data = models.Post.objects.get(slug=slug)
    except:
        return redirect('/')
    return render(request, 'post/showpost.html', locals())

def createpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CreatePostForm = forms.CreatePostForm(request.POST)
            if CreatePostForm.is_valid():
                post = CreatePostForm.save(commit=False)
                post.user = request.user
                post.save()
                messages.add_message(request, messages.SUCCESS, '成功新增文章')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
        else:
            CreatePostForm = forms.CreatePostForm()
        return render(request, 'post/createpost.html', locals())
    else:
        messages.add_message(request, messages.INFO, '請先登入')
        return redirect('/login/')

def editpost(request, slug):
    if request.user.is_authenticated:
        try:
            post = models.Post.objects.get(slug=slug)
        except:
            return redirect('/')

        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            # models.Post.objects.all().update(title=title, content=content)
            # models.Post.objects.filter(slug=slug).update(title=title, content=content)
            post.title=title
            post.content=content
            post.save()
            # edit.save()
            messages.add_message(request, messages.SUCCESS, '成功編輯文章')
            return redirect('/')
        return render(request, 'post/editpost.html', locals())
    else:
        messages.add_message(request, messages.INFO, '請先登入')
        return redirect('/login/')


    #     if request.method == 'POST':
    #         EditPostForm = forms.EditPostForm(request.POST)
    #         if EditPostForm.is_valid():
    #             post = EditPostForm.save(commit=False)
    #             post.user = request.user
    #             post.save()
    #             messages.add_message(request, messages.SUCCESS, '成功編輯文章')
    #             return redirect('/')
    #         else:
    #             messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    #     else:
    #         EditPostForm = forms.EditPostForm()
    #     return render(request, 'post/editpost.html', locals())
    # else:
    #     messages.add_message(request, messages.INFO, '請先登入')
    #     return redirect('/login/')

def deletepost(request, slug):
    if request.user.is_authenticated:
        try:
            post = models.Post.objects.get(slug=slug)
        except:
            return redirect('/')
        post.delete()
        messages.add_message(request, messages.INFO, '刪除成功')
        return redirect('/')
    else:
        messages.add_message(request, messages.INFO, '請先登入')
        return redirect('/login/')

# def index(request):
#     if not request.session.get('is_login', None):
#         return redirect('/login/')
#     return render(request, 'index.html')

# def login(request):
#     if request.method == "POST":
#         login_form = forms.LoginForm(request.POST)
#         message = "請檢查填寫的內容！"
#         if login_form.is_valid():
#             login_username = login_form.cleaned_data['username']
#             login_password = login_form.cleaned_data['password']
#             try:
#                 user = models.User.objects.get(username=login_username)
#                 if user.password == login_password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.username
#                     return redirect('/')
#                 else:
#                     message = "密碼不正確！"
#             except:
#                 message = "用戶名不存在！"
#         else:
#             message = "請檢查填寫的內容！"
#     else:
#         login_form = forms.LoginForm()
#     return render(request, 'login.html', locals())
