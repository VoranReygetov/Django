from django.test import TestCase
from .models import Employee
# Create your tests here.


# Create your tests here.
class EmployeeModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.employee = Employee.objects.create(
            name = 'John',
            email = 'tut@gmail.com',
            contact = '343748'
        )
    def test_fields(self):
            
        self.assertIsInstance(self.employee.name, str)
        self.assertIsInstance(self.employee.email, str)
        self.assertIsInstance(self.employee.contact, str)