from django.test import TestCase
from django.core import mail
from main.models import CustomUser, Profile, UserPost, Availability

class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        CustomUser.objects.create(email="validemail@gmail.com", your_name="Biz Person")
        
    def test_email_label(self):
        customUser = CustomUser.objects.get(id=1)
        field_label = customUser._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')
        
    def test_name_label(self):
        customUser = CustomUser.objects.get(id=1)
        field_label = customUser._meta.get_field('your_name').verbose_name
        self.assertEqual(field_label, 'user name')
        
    def test_first_name_max_length(self):
        customUser = CustomUser.objects.get(id=1)
        max_length = customUser._meta.get_field('your_name').max_length
        self.assertEqual(max_length, 30)
        
    def test_get_absolute_url(self):
        customUser = CustomUser.objects.get(id=1)
        # This will fail if the urlconf is not defined.
        self.assertEqual(customUser.get_absolute_url(), '/users/validemail%40gmail.com/')
    
    def test_get_short_name(self):
        customUser = CustomUser.objects.get(id=1)
        # This will fail if the User's full name isn't defined.
        self.assertEqual(customUser.get_short_name(), 'Biz Person')
        
    def test_email_user(self):
        customUser = CustomUser.objects.get(id=1)
        customUser.email_user('Subject here', 'Here is the message.',
            'from@example.com',)
        # This will test if the email function sends an email first checking that theres something 
        # in the outbox array and then that the subject of that email is as expected
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')        
        


# class UserModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email='user@info.com',
#             password='0000')

#     def test_send_password_token(self):
#         """
#         Sends a password reset mail with users authentication token.
#         """
#         token = Token.objects.get(user=self.user)
#         User.send_password_token(self.user.email)
#         self.assertEqual(len(outbox), 1)
#         self.assertEqual(mail.outbox.subject, 'Password reset:')
#         self.assertEqual(mail.outbox.from_email, <insert_from_email>)
#         self.assertEqual(mail.outbox.to, [<insert_list_of_to_emails>])
#         self.assertEqual(mail.outbox.body,
#             'Your password reset token:\n\n\t%s' % token.key)