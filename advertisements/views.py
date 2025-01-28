from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from advertisements.models import Announcement, Review
from advertisements.paginators import CustomPaginator
from advertisements.serializers import AnnouncementSerializer, ReviewSerializer
from users.permissions import IsAdmin, IsAuthor, IsUser


class AnnouncementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (
        IsAuthenticated,
        IsUser | IsAdmin,
    )


class AnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    pagination_class = CustomPaginator
    permission_classes = (AllowAny,)
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_fields = ("title",)
    ordering_fields = ("created_at",)


class AnnouncementCreateAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (
        IsAuthenticated,
        IsUser | IsAdmin,
    )

    def perform_create(self, serializer):
        """Устанавливает текущего пользователя автором объявления"""
        announcement = serializer.save()
        announcement.author = self.request.user
        announcement.save()


class AnnouncementUpdateAPIView(generics.UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdmin | IsAuthor,
        IsUser | IsAuthor,
    )


class AnnouncementDestroyAPIView(generics.DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdmin | IsAuthor,
        IsUser | IsAuthor,
    )


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPaginator
    permission_classes = (
        IsAuthenticated,
        IsUser | IsAdmin,
    )


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticated,
        IsUser | IsAdmin,
    )

    def perform_create(self, serializer):
        """Устанавливает текущего пользователя автором отзыва"""
        if IsAuthenticated:
            review = serializer.save()
            review.author = self.request.user
            review.save()


class ReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdmin | IsAuthor,
        IsUser | IsAuthor,
    )


class ReviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdmin | IsAuthor,
        IsUser | IsAuthor,
    )
