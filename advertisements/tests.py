from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from advertisements.models import Announcement, Review
from users.models import User


class AdvertisementsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="1111@gmail.com", role="admin")
        self.announcement = Announcement.objects.create(
            title="Телевизор", price=10000, author=self.user, created_at=datetime.now()
        )
        self.review = Review.objects.create(text="Отзыв", author=self.user)
        self.client.force_authenticate(user=self.user)

    def test_announcement_retrieve(self):
        url = reverse("advertisements:announcement", args=(self.announcement.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.announcement.title)

    def test_announcement_create(self):
        url = reverse("advertisements:ann_create")
        data = {
            "title": "Телевизор1",
            "price": "50000",
            "description": "Средняя диагональ",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Announcement.objects.all().count(), 2)

    def test_announcement_update(self):
        url = reverse("advertisements:ann_update", args=(self.announcement.pk,))
        data = {"title": "Телевизор2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Телевизор2")

    def test_announcement_delete(self):
        url = reverse("advertisements:ann_delete", args=(self.announcement.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Announcement.objects.all().count(), 0)

    def test_announcement_list(self):
        url = reverse("advertisements:announcements")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_create(self):
        url = reverse("advertisements:review_create")
        data = {"text": "Отзыв1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.all().count(), 2)

    def test_review_update(self):
        url = reverse("advertisements:review_update", args=(self.review.pk,))
        data = {"text": "Отзыв1"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("text"), "Отзыв1")

    def test_review_delete(self):
        url = reverse("advertisements:review_delete", args=(self.review.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.all().count(), 0)

    def test_review_list(self):
        url = reverse("advertisements:reviews")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
