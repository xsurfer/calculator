from unittest import TestCase

from django.test import Client

from models import Calculator


class IndexTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_empty_request(self):
        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

    def test_add_value(self):
        self.client = Client()

        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

        response = self.client.post('/calc/', {'input': '2', 'op': 'sum'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)

        response = self.client.post('/calc/', {'input': '3', 'op': 'equ'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], 5)
        self.assertEqual(response.context['error'], 0)

    def test_complex_expression(self):
        self.client = Client()

        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

        response = self.client.post('/calc/', {'input': '2', 'op': 'sum'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 2+
        response = self.client.post('/calc/', {'input': '7', 'op': 'mul'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 2+7*
        response = self.client.post('/calc/', {'input': '2', 'op': 'equ'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], 16)
        self.assertEqual(response.context['error'], 0)
        # 2+7*2

    def test_division_by_zero(self):
        self.client = Client()

        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

        response = self.client.post('/calc/', {'input': '2', 'op': 'sum'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 2+
        response = self.client.post('/calc/', {'input': '7', 'op': 'div'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 2+7/
        response = self.client.post('/calc/', {'input': '0', 'op': 'equ'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], dict(Calculator.ERRORS)[1])
        # 2+7/0

    def test_decimal(self):
        self.client = Client()

        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

        response = self.client.post('/calc/', {'input': '5', 'op': 'div'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 5/
        response = self.client.post('/calc/', {'input': '2', 'op': 'equ'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], 2.5)
        self.assertEqual(response.context['error'], 0)
        # 5/2

        self.client = Client()
        response = self.client.get('/calc/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        self.assertEqual(response.context['form'], None)

        response = self.client.post('/calc/', {'input': '1', 'op': 'div'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total'], None)
        self.assertEqual(response.context['error'], None)
        # 1/
        response = self.client.post('/calc/', {'input': '0.3', 'op': 'equ'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(round(response.context['total'],4), round(3.3333,4))
        self.assertEqual(response.context['error'], 0)
        # 5/2