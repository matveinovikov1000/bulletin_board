from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from advertisements.models import Announcement, Review
from advertisements.serializers import AnnouncementSerializer, ReviewSerializer
from advertisements.paginators import CustomPaginator


class AnnouncementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    pagination_class = CustomPaginator
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ("title",)
    ordering_fields = ("-created_at",)


class AnnouncementCreateAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        """Устанавливает текущего пользователя автором объявления"""
        announcement = serializer.save()
        announcement.author = self.request.user
        announcement.save()


class AnnouncementUpdateAPIView(generics.UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementDestroyAPIView(generics.DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPaginator


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """Устанавливает текущего пользователя автором отзыва"""
        if IsAuthenticated:
            review = serializer.save()
            review.author = self.request.user
            review.save()


class ReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDestroyAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
