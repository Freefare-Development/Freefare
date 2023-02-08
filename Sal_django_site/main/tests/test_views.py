from django.test import TestCase
from django.test import Client
from django.urls import reverse
from main.models import CustomUser, RecipientPost
class homepageTest(TestCase):
    @classmethod
    
    def setUp(self):
        # url = reverse('homepage')
        # response = self.client.get(url)
        self.client = Client()
        
    def test_view_url_exists_at_desired_location(self):
        url = reverse('homepage')
        response = self.client.get('/')
        # print("THE CODE IS: " + str(response.status_code))
        self.assertEqual(response.status_code, 200)
        ##Assert the right template is used
        self.assertTemplateUsed(response, 'main/home.html')
        
class profileViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = CustomUser.objects._create_user(email="validemail@gmail.com", your_name="Biz Person", password='2HJ1vRV0Z&3iD', is_staff=False, is_superuser=False)
        test_user2 = CustomUser.objects._create_user(email="another@gmail.com", your_name="Other Person", password='PassyWord9', is_staff=False, is_superuser=False)
        
        test_user1.save()
        test_user2.save()
        

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile-view'))
        self.assertRedirects(response, '/login/')
        
        
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='validemail@gmail.com', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('profile-view'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'validemail@gmail.com')
        
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'main/profile_view.html')
        
class EditPostViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = CustomUser.objects._create_user(email="validemail@gmail.com", your_name="Biz Person", password='2HJ1vRV0Z&3iD', is_staff=False, is_superuser=False)
        test_user2 = CustomUser.objects._create_user(email="another@gmail.com", your_name="Other Person", password='PassyWord9', is_staff=False, is_superuser=False)
        
        test_user1.save()
        test_user2.save()
        
        # Create a post
        data={'post_creator': test_user1, 'post_org_name': "Biz", 'post_org_role': "Donor", 
        'post_org_email': "validemail@gmail.com", 'post_org_phone': "1234567890", 'post_org_address': "1112 Winans Ave",
        'post_org_city': "Linden", 'post_org_state': "NJ", 'post_org_zipcode': "07036", 'post_org_country': "USA", 
        'post_org_desc': "Example text sentence."}