import os

from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Drug, Vaccination

token = os.environ.get('TOKEN_TESTING')
AUTH_HEADERS = {
    'HTTP_AUTHORIZATION': token
}


class DrugModelTests(TestCase):

    def setUp(self):
        self.drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )

    def test_drug_str(self):
        self.assertEqual(self.drug.__str__(), 'test drug')


class VaccinationModelTests(TestCase):

    def setUp(self):
        drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )
        self.vaccination = Vaccination.objects.create(
            rut='11.111.111-1',
            dose=0.5,
            drug=drug
        )

    def test_vaccination_str(self):
        self.assertEqual(
            self.vaccination.__str__(),
            f'Vaccination for {self.vaccination.rut}'
        )


class DrugEndPointsTests(APITestCase):
    def setUp(self):
        self.drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )

    def test_drug_list_endpoint(self):
        response = self.client.get('/drugs/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_detail_endpoint_with_drug_that_does_exists(self):
        response = self.client.get('/drugs/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_detail_endpoint_with_drug_that_does_not_exists(self):
        response = self.client.get('/drugs/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_post_endpoint(self):
        data = {
            'name': 'covid19-cure',
            'code': 'COVID19',
            'description': 'This will save the world'
        }
        response = self.client.post('/drug/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_drug_post_endpoint_with_bad_data(self):
        data = {
            'name': 'covid19-cure',
            'code': 'This is a very long code',
            'description': 'This will save the world'
        }
        response = self.client.post('/drug/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_drug_put_endpoint(self):
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put('/drug/1/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_put_endpoint_drug_does_not_exist(self):
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put('/drug/2/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint(self):
        response = self.client.delete('/drug/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_drug_delete_endpoint_drug_does_not_exist(self):
        response = self.client.delete('/drug/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint_drug_with_vaccinations(self):
        vaccination = Vaccination.objects.create(
            rut='11.111.111-1',
            dose=0.5,
            drug=self.drug
        )
        response = self.client.delete('/drug/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VaccinationEndPointsTests(APITestCase):
    def setUp(self):
        self.drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )
        self.vaccination = Vaccination.objects.create(
            rut='11.111.111-1',
            dose=0.5,
            drug=self.drug
        )

    def test_vaccination_list_endpoint(self):
        response = self.client.get('/vaccination/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vaccination_detail_endpoint_vaccination_exists(self):
        response = self.client.get('/vaccination/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vaccination_detail_endpoint_vaccination_doesnt_exists(self):
        response = self.client.get('/vaccination/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vaccination_post_endpoint(self):
        data = {
            'rut': '11.111.111-1',
            'dose': 1,
            'drug': 1
        }
        response = self.client.post('/vaccination/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vaccination_post_endpoint_dose_bigger_to_the_allowed(self):
        data = {
            'rut': '11.111.111-1',
            'dose': 2,
            'drug': 1
        }
        response = self.client.post('/vaccination/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_post_endpoint_dose_smaller_to_the_allowed(self):
        data = {
            'rut': '11.111.111-1',
            'dose': 0.1,
            'drug': 1
        }
        response = self.client.post('/vaccination/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_put_endpoint(self):
        data = {
            "id": 1,
            "rut": "11.111.111-1",
            "dose": 1.0,
            "date": "2020-08-22",
            "drug": 1
        }
        response = self.client.put('/vaccination/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vaccination_put_endpoint_does_not_exist(self):
        data = {
            "id": 100,
            "rut": "11.111.111-1",
            "dose": 1.0,
            "date": "2020-08-22",
            "drug": 1
        }
        response = self.client.put('/vaccination/100/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vaccination_put_endpoint_bad_data(self):
        data = {
            'id': 1,
            'rut': '18',
            'dose': 2.0,
            'date': '2020-08-22',
            'drug': 1
        }
        response = self.client.put('/vaccination/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_delete_endpoint(self):
        response = self.client.delete('/vaccination/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_vaccination_delete_endpoint_vaccination_does_not_exist(self):
        response = self.client.delete('/vaccination/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vaccination_post_endpoint_invalid_rut(self):
        data = {
            'rut': '3',
            'dose': 1,
            'drug': 1
        }
        response = self.client.post('/vaccination/', data, **AUTH_HEADERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)