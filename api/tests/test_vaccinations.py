import os

from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Drug, Vaccination


AUTH_HEADERS = {
    'HTTP_AUTHORIZATION': os.environ.get('TOKEN_TESTING')
}


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
        """
        Test the __str__ function of the model.
        """
        self.assertEqual(
            self.vaccination.__str__(),
            f'Vaccination for {self.vaccination.rut}'
        )


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
        """
        Test the GET /vaccination endpoint. Returns all the vaccinations.
        """
        response = self.client.get('/vaccination/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vaccination_detail_endpoint_vaccination_exists(self):
        """
        Test the GET /vaccination/:id endpoint. Returns a
        vaccination from a given id.
        """
        response = self.client.get('/vaccination/1/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vaccination_detail_endpoint_vaccination_doesnt_exists(self):
        """
        Test the GET /vaccination/:id endpoint for a
        vaccination that does not exists. Returns a 404 response.
        """
        response = self.client.get('/vaccination/2/', **AUTH_HEADERS)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vaccination_post_endpoint(self):
        """
        Test the POST /vaccination endpoint. Creates a vaccination.
        """
        data = {
            'rut': '11.111.111-1',
            'dose': 1,
            'drug': 1
        }
        response = self.client.post(
            '/vaccination/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vaccination_post_endpoint_dose_bigger_to_the_allowed(self):
        """
        Test the POST /vaccination endpoint. Tries to creates a
        vaccination with an incorrect dose. Returns a 400 response.
        """
        data = {
            'rut': '11.111.111-1',
            'dose': 2,
            'drug': 1
        }
        response = self.client.post(
            '/vaccination/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_post_endpoint_dose_smaller_to_the_allowed(self):
        """
        Test the POST /vaccination endpoint. Tries to create a
        vaccination with an incorrect dose. Returns a 400 response.
        """
        data = {
            'rut': '11.111.111-1',
            'dose': 0.1,
            'drug': 1
        }
        response = self.client.post(
            '/vaccination/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_post_endpoint_invalid_rut(self):
        """
        Test the POST /vaccination endpoint.
        Tries to create a vaccination with an incorrect rut.
        Returns a 400 response.
        """
        data = {
            'rut': '3',
            'dose': 1,
            'drug': 1
        }
        response = self.client.post(
            '/vaccination/',
            data,
            **AUTH_HEADERS,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vaccination_put_endpoint(self):
        """
        Test the PUT /vaccination/:id endpoint. Updates a vaccination
        from a given id.
        """
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
        """
        Test the PUT /vaccination/:id endpoint. Tries to update a
        vaccination that does not exists. Returns a 404 response.
        """
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
        """
        Test the PUT /vaccination/:id endpoint. Tries to update a
        vaccination with a wrong dose. Returns a 400 response.
        """
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
        """
        Test the DELETE /vaccination/:id endpoint. Deletes a
        vaccination from a given id.
        """
        response = self.client.delete('/vaccination/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_vaccination_delete_endpoint_vaccination_does_not_exist(self):
        """
        Test the DELETE /vaccination/:id endpoint. Tries to delete a
        vaccination from a given id that does not exists.
        """
        response = self.client.delete('/vaccination/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
