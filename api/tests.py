from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from .models import Drug, Vaccination


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
        response = self.client.get('/drugs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_detail_endpoint_with_drug_that_does_exists(self):
        response = self.client.get('/drugs/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_detail_endpoint_with_drug_that_does_not_exists(self):
        response = self.client.get('/drugs/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_post_endpoint(self):
        data = {
            'name': 'covid19-cure',
            'code': 'COVID19',
            'description': 'This will save the world'
        }
        response = self.client.post('/drug/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_drug_post_endpoint_with_bad_data(self):
        data = {
            'name': 'covid19-cure',
            'code': 'This is a very long code',
            'description': 'This will save the world'
        }
        response = self.client.post('/drug/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_drug_put_endpoint(self):
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put('/drug/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_put_endpoint_drug_does_not_exist(self):
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put('/drug/2/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint(self):
        response = self.client.delete('/drug/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_drug_delete_endpoint_drug_does_not_exist(self):
        response = self.client.delete('/drug/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint_drug_with_vaccinations(self):
        vaccination = Vaccination.objects.create(
            rut='11.111.111-1',
            dose=0.5,
            drug=self.drug
        )
        response = self.client.delete('/drug/1/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
