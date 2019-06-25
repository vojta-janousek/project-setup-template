from django.urls import path

from news.api.views import (article_list_create_api_view, ArticleDetailAPIView,
                            article_detail_api_view, ArticleListCreateAPIView,
                            JournalistListCreateAPIView)


urlpatterns = [
    path('class/articles/', ArticleListCreateAPIView.as_view(),
         name='class-article-list'),
    path('class/articles/<int:pk>/', ArticleDetailAPIView.as_view(),
         name='class-article-detail'),
    path('articles/', article_list_create_api_view, name='article-list'),
    path('articles/<int:pk>/', article_detail_api_view, name='article-detail'),
    path('class/journalists/', JournalistListCreateAPIView.as_view(),
         name='journalist-list'),
]
