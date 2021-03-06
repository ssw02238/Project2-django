from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update', views.update, name='update'),
    path('<int:article_pk>/comment', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/like', views.like, name='like'),
    path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),
    # path('hashtags/', views.popular_tag, name='popular_tag'),
    path('make_cloud/', views.make_cloud, name='make_cloud'),
    path('popular_tags/', views.popular_tags, name='popular_tags'),
]
