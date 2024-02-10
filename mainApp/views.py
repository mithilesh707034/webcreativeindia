from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def home_page(Request):
    return render(Request,'front/index.html')

def about_page(Request):
    return render(Request,'front/about.html')

def contact_page(Request):
    msg=''
    if(Request.method=="POST"):
        c=Contact()
        c.name=Request.POST.get('name')
        c.email=Request.POST.get('email')
        c.phone=Request.POST.get('phone')
        c.message=Request.POST.get('message')
        c.save()
        msg="Done"
    return render(Request,'front/connect.html',{'msg':msg})

def gallery_page(Request):
    data=Gallery.objects.all().order_by('id').reverse()
    return render(Request,'front/gallery.html',{'data':data})

def blog_page(Request):
    data=Blog.objects.all().order_by('id').reverse()
    return render(Request,'front/blog.html',{'data':data})

def blog_details_page(Request,title,id):
    data=Blog.objects.get(id=id)
    return render(Request,'front/blog-details.html',{'data':data})

def career_page(Request):
    return render(Request,'front/career.html')

def web_development_page(Request):
    return render(Request,'front/web-development.html')

def app_development_page(Request):
    return render(Request,'front/app-development.html')

def seo_service_page(Request):
    return render(Request,'front/seo-service.html')

def social_media_marketing_page(Request):
    return render(Request,'front/social-media-marketing.html')

def digital_pr_orm_page(Request):
    return render(Request,'front/digital-pr-orm.html')

def content_writting_page(Request):
    return render(Request,'front/content-writting.html')

def influencer_marketing_page(Request):
    return render(Request,'front/influencer-marketing.html')

def dynamic_content(Request,location,title):
    loc=Location.objects.all()
    ser=Service.objects.all()
    return render(Request,'front/dynamic-service.html',{'location':location,'title':title,'loc':loc,'ser':ser})

def dynamic_content2(Request,title):
    loc=Location.objects.all()
    ser=Service.objects.all()
    return render(Request,'front/dynamic-service.html',{'title':title,'loc':loc,'ser':ser})


#CRM

def login_page(Request):
    msg=''
    username=''
    password=''
    if (Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin")
            else:
                return redirect("/my-dashbord")
        else:
            msg="Not Matched"
    return render(Request,'front/login.html',{'msg':msg,'u':username,'p':password})

def client_dashbord(Request):
    msg=''
    ticket=Ticket.objects.all().order_by('id').reverse()
    if Request.method=="POST":
        t=Ticket()
        t.username=Request.user.username
        t.subject=Request.POST.get('subject')
        t.description=Request.POST.get('description')
        t.save()
        msg='Done'
    return render(Request, 'client/client-dashbord.html',{'msg':msg,'ticket':ticket})