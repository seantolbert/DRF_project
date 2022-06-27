from audioop import reverse
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from notes.models import Note, Category
from django.contrib.auth.models import User


class NoteTests(APITestCase):
    def test_view_notes(self):
        url = reverse('notes_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

