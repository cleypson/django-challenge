from django.test import TestCase

# Create your tests here.
import json
from django.test import TestCase, Client
from django.db.models import Max, Min
from rest_framework import status

# Create your tests here.

BASE_URL = '/api/v1'

client = Client()


class ModelTestClass(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
