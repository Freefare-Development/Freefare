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
        ##Assert the right template is used
        self.assertTemplateUsed(response, 'main/home.html')
        
class profileViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = CustomUserManager()
        # test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1._create_user(email="validemail@gmail.com", your_name="Biz Person", password='2HJ1vRV0Z&3iD', is_staff=False, is_superuser=False)
        # test_user2.save()
        
        # test_profile = Profile.objects.create(email="validemail@gmail.com", your_name="Biz Person")
        

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile-view'))
        self.assertRedirects(response, '/login/')