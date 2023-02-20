from django.test import TestCase
from django.test import Client
from django.urls import reverse

from main.models import CustomUser, Profile, RecipientPost, Availability
from main.forms import ProfileForm, AvailabilityFormset
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
        
        profile_user1 = Profile.objects.create(user=test_user1)
        # Create a post
        data={'post_creator': test_user1, 'post_org_name': "Biz", 'post_org_role': "Donor", 
        'post_org_email': "validemail@gmail.com", 'post_org_phone': "1234567890", 'post_org_address': "1112 Winans Ave",
        'post_org_city': "Linden", 'post_org_state': "NJ", 'post_org_zipcode': "07036", 'post_org_country': "USA", 
        'post_org_desc': "Example text sentence."}
        
        image_path = Path(__file__).parent / "../media/default.png"
        self.test_post_form = ProfileForm(data, {'post_image': SimpleUploadedFile(name='default.png', content=open(image_path, 'rb').read(), content_type='image/jpeg') })
        
        self.r_post = RecipientPost.objects.create(post_creator= test_user1, post_org_name= "Biz", donor_or_recip="Donor", 
        post_org_email="validemail@gmail.com", post_org_phone="1234567890", post_org_address="1112 Winans Ave",
        post_org_city="Linden", post_org_state="NJ", post_org_zipcode="07036", post_org_country= "USA", 
        post_desc="Example text sentence.")
        
        self.av_data={
            'form-TOTAL_FORMS': 1, 
            'form-INITIAL_FORMS': 0, 
            
            # "form-0-assigned_post" :self.r_post, 
            "form-0-post_day": ['m', 'th'],
            "form-0-start_hour" :datetime.time(10, 33, 45), 
            "form-0-end_hour" :datetime.time(10, 50, 45)}
        
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
        # valid_date_in_future = datetime.date.today() + datetime.timedelta(weeks=2)
        # response = self.client.post(reverse('new_rpost', kwargs={'recipient_post_form':self.r_post.pk,}), {'avail_form':self.newAvail})
        # response = self.client.post(reverse('new_rpost'),{'recipient_post_form':self.test_post_form}, {'avail_form':self.av_data})
        response = self.client.post(reverse('new_rpost'),data={'recipient_post_form':self.test_post_form, 'avail_form':self.av_data})
        self.assertRedirects(response, reverse('my_posts'))
        
    