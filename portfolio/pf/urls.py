from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email', views.send_email, name='send-email'),

    #projects
    path('projects', views.projects, name="projects"),

    #Practice
    path('practice', views.practice, name="practice"),

    #Blog
    path('blogs', views.BlogListView.as_view(), name="blogs"),
    path('blogs/create', views.create_blog, name="blog-create"),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name="blog-detail"),
]
