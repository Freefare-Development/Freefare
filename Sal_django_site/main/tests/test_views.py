from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.http import HttpRequest

from main.models import CustomUser, Profile, RecipientPost, Availability
from main.forms import ProfileForm, RecipientPostForm, AvailabilityFormset
from django.core.files.uploadedfile import SimpleUploadedFile

import datetime
from pathlib import Path
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
        response = self.client.get(reverse('profile_view'))
        self.assertEqual(response.status_code, 302)

        
        
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='validemail@gmail.com', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('profile_view'))
        # print(response.content)

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
        
        self.profile_user1 = Profile.objects.create(user=test_user1)
        # Create a post
        data={'post_creator': test_user1, 'post_org_name': "Biz", 'post_org_role': "Donor", 
        'post_org_email': "validemail@gmail.com", 'post_org_phone': "1234567890", 'post_org_address': "1112 Winans Ave",
        'post_org_city': "Linden", 'post_org_state': "NJ", 'post_org_zipcode': "07036", 'post_org_country': "USA", 
        'post_org_desc': "Example text sentence.",'post_begin_date': datetime.date(2023, 1, 28), 'post_end_date': datetime.date(2023, 5, 1),
         'post_deliver': False, 'post_recurring': False, 'recurrences': " "}
        # 'post_image': <ImageFieldFile: post_pics/heart-png-38780.png>,
        image_path = Path(__file__).parent / "../media/default.png"
        self.test_post_form = RecipientPostForm(data, {'post_image': SimpleUploadedFile(name='default.png', content=open(image_path, 'rb').read(), content_type='image/jpeg') })
        
        self.r_post = RecipientPost.objects.create(post_creator= test_user1, post_org_name= "Biz", donor_or_recip="Donor", 
        post_org_email="validemail@gmail.com", post_org_phone="1234567890", post_org_address="1112 Winans Ave",
        post_org_city="Linden", post_org_state="NJ", post_org_zipcode="07036", post_org_country= "USA", 
        post_desc="Example text sentence.")
        
        full_filename=Path(__file__).parent / "../media/default.png"
        self.data={'post_creator': test_user1, 'post_org_name': "Biz", 'post_org_role': "Donor", 
        'post_org_email': "validemail@gmail.com", 'post_org_phone': "1234567890", 'post_org_address': "1112 Winans Ave",
        'post_org_city': "Linden", 'post_org_state': "NJ", 'post_org_zipcode': "07036", 'post_org_country': "USA", 
        'post_desc': "Example text sentence.",'post_begin_date': datetime.date(2023, 1, 28), 'post_end_date': datetime.date(2023, 5, 1),
        'post_image':("test_file.png", open(full_filename, "rb")), 'post_deliver': False, 'post_recurring': False, 'recurrences': " "}
        
        self.av_data={
            'availability_set-TOTAL_FORMS': 1, 
            'availability_set-INITIAL_FORMS': 0,
            'availability_set-MIN_NUM_FORMS':0,
            'availability_set-MAX_NUM_FORMS': 1000, 
            
            "availability_set-0-assigned_post" :self.r_post, 
            "availability_set-0-post_day": ['m', 'th'],
            "availability_set-0-start_hour" :datetime.time(10, 33, 45), 
            "availability_set-0-end_hour" :datetime.time(10, 50, 45)
            
            }
        
        # self.formset = AvailabilityFormset(av_data)
        
        
        self.newAvail = Availability.objects.create(assigned_post =self.r_post, post_day = ['m', 'th'],
    start_hour =datetime.time(10, 33, 45), end_hour =datetime.time(10, 50, 45))
        
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('new_rpost'))
        self.assertEqual(response.status_code, 302)
        
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='validemail@gmail.com', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('new_rpost'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/new_rpost.html')
        
        
    def test_redirects_to_all_posts_list_on_success(self):
        login = self.client.login(username='validemail@gmail.com', password='2HJ1vRV0Z&3iD')
        response = self.client.post(reverse('new_rpost'), data={**self.data, **self.av_data})
        # response = self.client.get(reverse('new_rpost'))
        print("****")
        print(response.content)
        # self.assertTemplateUsed(response, 'main/email.html')
        self.assertRedirects(response, reverse('my-posts'))
        
    