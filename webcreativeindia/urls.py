from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('gallery/',views.gallery_page),
    path('blog/',views.blog_page),
    path('career/',views.career_page),
    path('web-designing-and-development/',views.web_development_page),
    path('app-designing-and-development/',views.app_development_page),
    path('social-media-marketing/',views.social_media_marketing_page),
    path('search-engine-optimization-and-management/',views.seo_service_page),
    path('digital-pr-orm/',views.digital_pr_orm_page),
    path('content-writting/',views.content_writting_page),
    path('influencer-marketing/',views.influencer_marketing_page),
   
    #CRM
    path('login/',views.login_page),
    path('my-dashbord/',views.client_dashbord),
    #End CRM
    path('<str:title>/',views.dynamic_content2),
    path('blog-details/<str:title>-<int:id>/',views.blog_details_page),
    path('<str:location>/<str:title>/',views.dynamic_content),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

