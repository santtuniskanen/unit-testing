import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Santtu', 'Niskanen', 50000)
        emp_2 = Employee('Jane', 'Doe', 60000)

        self.assertEqual(emp_1.email, \
            'Santtu.Niskanen@email.com')
        self.assertEqual(emp_2.email, \
            'Jane.Doe@email.com')

        emp_1.first = 'Santeri'
        emp_2.first = 'John'

        self.assertEqual(emp_1.email, \
            'Santeri.Niskanen@email.com')
        self.assertEqual(emp_2.email, \
            'John.Doe@email.com')

if __name__ == '__main__':
    unittest.main()