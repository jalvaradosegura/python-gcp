from django.test import TestCase

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
