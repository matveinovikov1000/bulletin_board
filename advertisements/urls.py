from django.urls import path

from advertisements.apps import AdvertisementsConfig
from advertisements.views import (AnnouncementCreateAPIView,
                                  AnnouncementDestroyAPIView,
                                  AnnouncementListAPIView,
                                  AnnouncementRetrieveAPIView,
                                  AnnouncementUpdateAPIView,
                                  ReviewCreateAPIView, ReviewDestroyAPIView,
                                  ReviewListAPIView, ReviewUpdateAPIView)

app_name = AdvertisementsConfig.name

urlpatterns = [
    path("ann_create/", AnnouncementCreateAPIView.as_view(), name="ann_create"),
    path(
        "ann_update/<int:pk>/", AnnouncementUpdateAPIView.as_view(), name="ann_update"
    ),
    path(
        "ann_delete/<int:pk>/", AnnouncementDestroyAPIView.as_view(), name="ann_delete"
    ),
    path(
        "announcement/<int:pk>/",
        AnnouncementRetrieveAPIView.as_view(),
        name="announcement",
    ),
    path("announcements/", AnnouncementListAPIView.as_view(), name="announcements"),
    path("review_create/", ReviewCreateAPIView.as_view(), name="review_create"),
    path(
        "review_update/<int:pk>/", ReviewUpdateAPIView.as_view(), name="review_update"
    ),
    path(
        "review_delete/<int:pk>/", ReviewDestroyAPIView.as_view(), name="review_delete"
    ),
    path("reviews/", ReviewListAPIView.as_view(), name="reviews"),
]
