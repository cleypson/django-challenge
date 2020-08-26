from rest_framework.test import APIClient
from django.test import TestCase

# Create your tests here.
import json
from django.test import TestCase, Client
from django.db.models import Max, Min
from rest_framework import status
from apps.api.models import Never, Project

# Create your tests here.

# client = Client()



class ModelTestClass(TestCase):
    
    def setUp(self):
        self.project_payload = {
            'name': 'Projeto Payload',
        }
        self.project_invalid_payload = {
            'name': '',
        }
        self.project_nevers_payload = {
            'name': 'Projeto Payload',
            'nevers': [2,3,4,5,6]
        }
        self.never_payload = {
            'name': 'Never Payload',
            'birthdate': '01/01/2004',
            'admission_date': '01/05/2016',
            'job_role': 'DBA'
        }
        self.never_invalid_payload = {
            'name': '',
            'birthdate': '01/01=0000',
            'admission_date': '01=05/2016',
            'job_role': ''
        }
        self.signup_payload = {
            'email': 'test@example.com',
            'password': 'password'   
        }
        self.login_payload = {
            'email': 'test@example.com',
            'password': 'password'
        }

    def tearDown(self):
        pass

    def test_signup(self):
        client = APIClient()
        response = client.post('/api/v1/signup/', self.signup_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        client = APIClient()
        client.post(
            '/api/v1/signup/', self.signup_payload, format='json')
        response = client.post('/api/v1/login/', self.login_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_never(self):
        client = APIClient()
        token = self.get_token()
        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = client.post(
            '/api/v1/nevers/', self.never_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_project(self):
        client = APIClient()
        token = self.get_token()
        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = client.post(
            '/api/v1/projects/', self.project_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_never_in_project(self):
        client = APIClient()
        project = Project.objects.create(name="Project Payload")
        for n in range(5):
            never = Never.objects.create(
                name="never {}".format(n),
                birthdate='2000-01-01',
                admission_date='2000-01-01',
                job_role='Dev'
            )

        token = self.get_token()
        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = client.post(
            '/api/v1/projects/', self.project_nevers_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filter_never_admission_date(self):
        client = APIClient()
        for n in range(1,12):
            never = Never.objects.create(
                name="never {}".format(n),
                birthdate='2000-01-01',
                admission_date='2000-01-{}'.format(n),
                job_role='Dev'
            )

        token = self.get_token()
        client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = client.get(
            '/api/v1/projects/', data={'name': 'never 5'}, format='json')
        print(response)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




    def get_token(self):
        client = APIClient()
        client.post(
            '/api/v1/signup/', self.signup_payload, format='json')
        response = client.post(
            '/api/v1/login/', self.login_payload, format='json')
        content = json.loads(response.content)
        header = {'Authorization': 'JWT {}'.format(content['token'])}
        return content['token']
