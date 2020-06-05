from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.post_resources, name='post_resources'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('about/',views.about_page_view, name='about'),
    path('reports/',views.contact_us, name='contact'),
    

    
] 
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)