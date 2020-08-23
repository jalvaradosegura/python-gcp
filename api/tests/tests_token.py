from rest_framework.test import APITestCase
from rest_framework import status


class DrugEndPointsTests(APITestCase):

    def test_drug_list_endpoint(self):
        """
        Test the GET /token endpoint. Returns a JWT token.
        It does not receive any parameters or password
        """
        response = self.client.get('/token/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_drug_list_endpoint_with_post_method(self):
        """
        Test the POST /token endpoint. Returns a 405 response because
        that method is not allowed for this endpoint
        """
        response = self.client.post('/token/')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_drug_list_endpoint_with_put_method(self):
        """
        Test the PUT /token endpoint. Returns a 405 response because
        that method is not allowed for this endpoint
        """
        response = self.client.put('/token/')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_drug_list_endpoint_with_delete_method(self):
        """
        Test the DELETE /token endpoint. Returns a 405 response because
        that method is not allowed for this endpoint
        """
        response = self.client.delete('/token/')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
