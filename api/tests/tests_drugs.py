import os

from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Drug, Vaccination

AUTH_HEADERS = {
    'HTTP_AUTHORIZATION': os.environ.get('TOKEN_TESTING')
}


class DrugModelTests(TestCase):

    def setUp(self):
        self.drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )

    def test_drug_str(self):
        """
        Test the __str__ function of the model.
        """
        self.assertEqual(self.drug.__str__(), 'test drug')


class DrugEndPointsTests(APITestCase):
    def setUp(self):
        self.drug = Drug.objects.create(
            name='test drug',
            code='test code',
            description='test description'
        )

    def test_drug_list_endpoint(self):
        """
        Test the GET /drugs endpoint. Returns all the drugs.
        """
        response = self.client.get('/drugs/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_list_endpoint_with_no_token(self):
        """
        Test the GET /drugs endpoint without providing a token.
        Returns a 403 response
        """
        response = self.client.get('/drugs/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_drug_detail_endpoint_with_drug_that_does_exists(self):
        """
        Test the GET /drugs/:id endpoint. Returns a drug by its id.
        """
        response = self.client.get('/drugs/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_detail_endpoint_with_drug_that_does_not_exists(self):
        """
        Test the GET /drugs/:id endpoint. Returns a 404 response because
        the drug id does not exist.
        """
        response = self.client.get('/drugs/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_post_endpoint(self):
        """
        Test the POST /drug endpoint. Creates a drug from a given payload.
        """
        data = {
            'name': 'covid19-cure',
            'code': 'COVID19',
            'description': 'This will save the world'
        }
        response = self.client.post(
            '/drug/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_drug_post_endpoint_with_bad_data(self):
        """
        Test the POST /drug endpoint. Tries to create a drug from
        a given payload, but the payload has an invalidate code.
        Returns a 400 response.
        """
        data = {
            'name': 'covid19-cure',
            'code': 'This is a very long code',
            'description': 'This will save the world'
        }
        response = self.client.post(
            '/drug/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_drug_put_endpoint(self):
        """
        Test the PUT /drug/:id endpoint. Updates a given drug by a payload.
        """
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put(
            '/drug/1/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_put_endpoint_drug_does_not_exist(self):
        """
        Test the PUT /drug/:id endpoint for a drug that does not exists.
        Returns a 404 response.
        """
        data = {
            'name': 'covid19-cure edit',
            'code': 'test code',
            'description': 'This will save the world'
        }
        response = self.client.put(
            '/drug/2/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint(self):
        """
        Test the DELETE /drug/:id endpoint. Deletes a drug from a given id.
        """
        response = self.client.delete('/drug/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_drug_delete_endpoint_drug_does_not_exist(self):
        """
        Test the DELETE /drug/:id endpoint for a drug that does not exists.
        Returns a 404 response.
        """
        response = self.client.delete('/drug/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drug_delete_endpoint_drug_with_vaccinations(self):
        """
        Test the DELETE /drug/:id endpoint for a drug that has
        been used for vaccinations. Returns a 400 response.
        """
        vaccination = Vaccination.objects.create(
            rut='11.111.111-1',
            dose=0.5,
            drug=self.drug
        )
        response = self.client.delete('/drug/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
