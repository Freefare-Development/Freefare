from django.test import TestCase
from django.test import Client
from django.urls import reverse

class homepageTest(TestCase):
    @classmethod
    
    def setUp(self):
        # url = reverse('homepage')
        # response = self.client.get(url)
        self.client = Client()

    # def test_home_page_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEquals(response.status_code, 200)
        
    def test_view_url_exists_at_desired_location(self):
        url = reverse('homepage')
        response = self.client.get('/')
        print("THE CODE IS: " + str(response.status_code))
        self.assertEqual(response.status_code, 200)