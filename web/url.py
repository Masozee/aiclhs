from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='web/index.html'), name='home'),
    path('speakers/', TemplateView.as_view(template_name='web/speakers.html'), name='speakers'),
    path('schedule/', TemplateView.as_view(template_name='web/schedule.html'), name='schedule'),
    path('sponsors/', TemplateView.as_view(template_name='web/sponsors.html'), name='sponsors'),
    path('contact/', TemplateView.as_view(template_name='web/contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='web/about.html'), name='about'),
    path('gallery/', TemplateView.as_view(template_name='web/gallery.html'), name='gallery'),
    path('blog/', TemplateView.as_view(template_name='web/blog.html'), name='blog'),
    path('blog/detail/', TemplateView.as_view(template_name='web/blog-single.html'), name='blog-detail'),
]