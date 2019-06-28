from django.urls import path

from job_offers.api.views import (JobOfferListCreateAPIView,
                                  JobOfferDetailAPIView)

urlpatterns = [
    path('offers/', JobOfferListCreateAPIView.as_view(),
         name='job-offer-list'),
    path('offers/<int:pk>/', JobOfferDetailAPIView.as_view(),
         name='job-offer-detail'),
]
