from django.urls import path

from ebooks.api.views import (EbookListCreateAPIView, EbookDetailAPIView,
                              ReviewCreateAPIView, ReviewDetailAPIView)


urlpatterns = [
    path('list/', EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('detail/<int:pk>/', EbookDetailAPIView.as_view(),
         name='ebook-detail'),

    path('detail/<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(),
         name='ebook-review'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(),
         name='review-detail')
]
