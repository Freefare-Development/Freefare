from django.test import TestCase
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile


from main.forms import ProfileForm


class ProfileFormTest(TestCase):
    data={'org_name': "Biz", 'org_role': "Donor", 
        'org_email': "validemail@gmail.com", 'org_phone': "1234567890", 'org_address': "1112 Winans Ave",
        'org_city': "Linden", 'org_state': "NJ", 'org_zipcode': "07036", 'org_country': "USA", 
        'org_desc': "Example text sentence."}
    
    image_path = Path(__file__).parent / "../media/default.png"
    default_form = ProfileForm(data, {'image': SimpleUploadedFile(name='default.png', content=open(image_path, 'rb').read(), content_type='image/jpeg') })
    


    def test_profile_form_org_name_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['org_name'].label is None or form.fields['org_name'].label == 'Your Organization')

    def test_profile_form_valid(self):
        self.assertTrue(self.default_form .is_valid())
        

    def test_profile_form_special_character(self):
        invalid_name = "@-|Invalids?&"
        form = self.default_form 
        form = ProfileForm(data={'org_name': invalid_name})
        self.assertFalse(form.is_valid())
        

