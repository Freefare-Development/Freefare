import os
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, UserPost, Availability, DonorPost, RecipientPost
from .models import DAYS_OF_WEEK
# from address.forms import AddressField, AddressWidget
# import django.contrib.admin.widgets
from django.utils.html import escape
from django.forms.widgets import SelectDateWidget, DateTimeInput
from django.forms import inlineformset_factory
from django.forms import formset_factory
from django.forms import ModelForm


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


AvailabilityFormset = inlineformset_factory(UserPost, Availability, fields=('post_day', 'start_hour', 'end_hour',),
                                            widgets={
    'post_day': forms.CheckboxSelectMultiple,
    'start_hour': forms.TimeInput(attrs={
        'type': 'time'
    }),
    'end_hour': forms.TimeInput(attrs={
        'type': 'time'
    })},
    extra=4,
    # can_order=True
)


class RecipientPostForm(forms.ModelForm):
    post_image = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/png, .jpg, .jpeg'}))
    post_begin_date = forms.DateField(widget=SelectDateWidget)
    post_end_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = RecipientPost
        fields = ['post_title', 'post_org_name', 'post_org_phone', 'post_org_email', 'post_org_address', 'post_org_city',
                  'post_org_state', 'post_org_zipcode', 'post_org_country', 'post_desc', 'post_begin_date', 'post_image',
                  'post_end_date', 'post_deliver', 'post_recurring', 'recurrences', ]

    def clean_post_title(self):
        post_title = self.cleaned_data['post_title']
        # No Special Characters
        if '<' in post_title or '>' in post_title or '*' in post_title or '/' in post_title or '|' in post_title or '=' in post_title:
           raise forms.ValidationError("Titles should not have special characters.")
        return post_title

    def clean_post_org_name(self):
        post_org_name = self.cleaned_data['post_org_name']
        if '<' in post_org_name or '>' in post_org_name or '*' in post_org_name or '/' in post_org_name or '|' in post_org_name or '=' in post_org_name:
           raise forms.ValidationError("Name should not have special characters.")
        if len(post_org_name) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_name
    
    def clean_post_org_email(self):
        post_org_email = self.cleaned_data['post_org_email']
        # No Special Characters
        if '<' in post_org_email or '>' in post_org_email or '*' in post_org_email or '/' in post_org_email or '|' in post_org_email or '=' in post_org_email:
           raise forms.ValidationError("Email should not have weird characters.")
        if '@' not in post_org_email:
           raise forms.ValidationError("Please use a correct email address")
        if len(post_org_email) < 6:
            raise forms.ValidationError("Please use a correct email address")
        return post_org_email

    def clean_post_org_phone(self):
        post_org_phone = self.cleaned_data['post_org_phone']
        # No Special Characters
        # if '<' in post_org_phone or '>' in post_org_phone or '*' in post_org_phone or '/' in post_org_phone or '|' in post_org_phone or '=' in post_org_phone:
        #    raise forms.ValidationError("Phone # should not have special characters.")
        # if len(post_org_phone) < 10:
        #    raise forms.ValidationError('Phone # must be at least 10 digits')
        return post_org_phone
    

    def clean_post_org_address(self):
        post_org_address = self.cleaned_data['post_org_address']
        # No Special Characters
        if '<' in post_org_address or '>' in post_org_address or '*' in post_org_address or '/' in post_org_address or '|' in post_org_address or '=' in post_org_address:
            raise forms.ValidationError("Address should not have special characters.")
        post_org_address = escape(post_org_address)
        if len(post_org_address) < 2:
            raise forms.ValidationError("Please enter a real address")
        return post_org_address
    
    def clean_post_org_country(self):
        post_org_country = self.cleaned_data['post_org_country']
        # No Special Characters
        if '<' in post_org_country or '>' in post_org_country or '*' in post_org_country or '/' in post_org_country or '|' in post_org_country or '=' in post_org_country:
            raise forms.ValidationError("Country name should not have special characters.")
        post_org_country = escape(post_org_country)
        if len(post_org_country) < 2:
            raise forms.ValidationError("Please enter a real country")
        return post_org_country 
    
    def clean_post_org_city(self):
        post_org_city = self.cleaned_data['post_org_city']
        # No Special Characters
        if '<' in post_org_city or '>' in post_org_city or '*' in post_org_city or '/' in post_org_city or '|' in post_org_city or '=' in post_org_city:
            raise forms.ValidationError("City name should not have special characters.")
        post_org_city = escape(post_org_city)
        if len(post_org_city) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_city   
     
    def clean_post_org_state(self):
        post_org_state = self.cleaned_data['post_org_state']
        # No Special Characters
        if '<' in post_org_state or '>' in post_org_state or '*' in post_org_state or '/' in post_org_state or '|' in post_org_state or '=' in post_org_state:
            raise forms.ValidationError("State name should not have special characters.")
        post_org_state = escape(post_org_state)
        if len(post_org_state) < 2:
            raise forms.ValidationError("Please enter a real state")
        return post_org_state   

    def clean_post_org_zipcode(self):
        post_org_zipcode = self.cleaned_data['post_org_zipcode']
        # # No Special Characters
        # if '<' in post_org_zipcode or '>' in post_org_zipcode or '*' in post_org_zipcode or '/' in post_org_zipcode or '|' in post_org_zipcode or '=' in post_org_zipcode:
        #     raise forms.ValidationError("Zipcode should not have special characters.")
        post_org_zipcode = escape(post_org_zipcode)
        if len(post_org_zipcode) < 5:
            raise forms.ValidationError("Please enter a real zip code")
        return post_org_zipcode 
      
    def clean_post_desc(self):
        post_desc = self.cleaned_data['post_desc']
        # No Special Characters
        if '<' in post_desc or '>' in post_desc or '*' in post_desc or '/' in post_desc or '|' in post_desc or '=' in post_desc:
            raise forms.ValidationError("Item description should not have special characters.")
        # if len(post_desc) < 5:
        #     raise forms.ValidationError("Please describe your post")
        # post_desc = escape(post_desc)
        return post_desc


class DonorPostForm(forms.ModelForm):
    post_image = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/png,.jpg'}))
    post_avail = forms.ModelMultipleChoiceField(queryset=Availability.objects.all(), widget=forms.SelectMultiple)
    # post_avail = inlineformset_factory(Author, Book, fields=('title',))
    post_begin_date = forms.DateField(widget=SelectDateWidget)
    post_end_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = DonorPost
        fields = ['post_title', 'post_org_name', 'post_org_phone', 'post_org_email', 'post_org_address', 'post_org_city',
                  'post_org_state', 'post_org_zipcode', 'post_org_country', 'post_desc', 'post_begin_date', 'post_image',
                  'post_end_date', 'post_deliver', 'post_recurring', 'recurrences', ]
    
    def clean_post_title(self):
        post_title = self.cleaned_data['post_title']
        if '<' in post_title or '>' in post_title or '*' in post_title or '/' in post_title or '|' in post_title or '=' in post_title:
           raise forms.ValidationError("Titles should not have special characters.")
        return post_title

    def clean_post_org_name(self):
        post_org_name = self.cleaned_data['post_org_name']
        if '<' in post_org_name or '>' in post_org_name or '*' in post_org_name or '/' in post_org_name or '|' in post_org_name or '=' in post_org_name:
           raise forms.ValidationError("Name should not have special characters.")
        if len(post_org_name) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_name
    
    def clean_post_org_email(self):
        post_org_email = self.cleaned_data['post_org_email']
        if '<' in post_org_email or '>' in post_org_email or '*' in post_org_email or '/' in post_org_email or '|' in post_org_email or '=' in post_org_email:
           raise forms.ValidationError("Email should not have weird characters.")
        if '@' not in post_org_email:
           raise forms.ValidationError("Please use a correct email address")
        return post_org_email
    
    def clean_post_org_phone(self):
        post_org_phone = self.cleaned_data['post_org_phone']
        if '<' in post_org_phone or '>' in post_org_phone or '*' in post_org_phone or '/' in post_org_phone or '|' in post_org_phone or '=' in post_org_phone:
           raise forms.ValidationError("Phone # should not have special characters.")
        if len(post_org_phone) < 10:
           raise forms.ValidationError('Phone # must be at least 10 digits')
        return post_org_phone

    def clean_post_org_address(self):
        post_org_address = self.cleaned_data['post_org_address']
        post_org_address = escape(post_org_address)
        if len(post_org_address) < 2:
            raise forms.ValidationError("Please enter a real address")
        return post_org_address

    def clean_post_org_city(self):
        post_org_city = self.cleaned_data['post_org_city']
        # No Special Characters
        if '<' in post_org_city or '>' in post_org_city or '*' in post_org_city or '/' in post_org_city or '|' in post_org_city or '=' in post_org_city:
            raise forms.ValidationError("City name should not have special characters.")
        post_org_city = escape(post_org_city)
        if len(post_org_city) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_city   
     
    def clean_post_org_state(self):
        post_org_state = self.cleaned_data['post_org_state']
        # No Special Characters
        if '<' in post_org_state or '>' in post_org_state or '*' in post_org_state or '/' in post_org_state or '|' in post_org_state or '=' in post_org_state:
            raise forms.ValidationError("State name should not have special characters.")
        post_org_state = escape(post_org_state)
        if len(post_org_state) < 2:
            raise forms.ValidationError("Please enter a real state")
        return post_org_state   
    
    def clean_post_org_zipcode(self):
        post_org_zipcode = self.cleaned_data['post_org_zipcode']
        # # No Special Characters
        # if '<' in post_org_zipcode or '>' in post_org_zipcode or '*' in post_org_zipcode or '/' in post_org_zipcode or '|' in post_org_zipcode or '=' in post_org_zipcode:
        #     raise forms.ValidationError("Zipcode should not have special characters.")
        post_org_zipcode = escape(post_org_zipcode)
        if len(post_org_zipcode) < 5:
            raise forms.ValidationError("Please enter a real zip code")
        return post_org_zipcode 

    def clean_post_org_country(self):
        post_org_country = self.cleaned_data['post_org_country']
        post_org_country = escape(post_org_country)
        if len(post_org_country) < 2:
            raise forms.ValidationError("Please enter a real country")
        return post_org_country

    def clean_post_desc(self):
        post_desc = self.cleaned_data['post_desc']
        post_desc = escape(post_desc)
        if '<' in post_desc or '>' in post_desc or '*' in post_desc or '/' in post_desc or '|' in post_desc or '=' in post_desc:
           raise forms.ValidationError("Description should not have special characters.")
        return post_desc


class EditProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'accept': 'image/png,.jpg'}))

    class Meta:
        model = Profile
        fields = ['org_name', 'org_role', 'org_email', 'org_phone', 'org_address',
                  'org_city', 'org_state', 'org_zipcode', 'org_country', 'image', 'org_desc']

    def clean_post_org_name(self):
        post_org_name = self.cleaned_data['post_org_name']
        if '<' in post_org_name or '>' in post_org_name or '*' in post_org_name or '/' in post_org_name or '|' in post_org_name or '=' in post_org_name:
           raise forms.ValidationError("Name should not have special characters.")
        if len(post_org_name) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_name

    def clean_org_address(self):
        org_address = self.cleaned_data['org_address']
        org_address = escape(org_address)
        return org_address

    def clean_post_org_city(self):
        post_org_city = self.cleaned_data['post_org_city']
        # No Special Characters
        if '<' in post_org_city or '>' in post_org_city or '*' in post_org_city or '/' in post_org_city or '|' in post_org_city or '=' in post_org_city:
            raise forms.ValidationError("City name should not have special characters.")
        post_org_city = escape(post_org_city)
        if len(post_org_city) < 2:
            raise forms.ValidationError("Please enter a real city")
        return post_org_city   
     
    def clean_post_org_state(self):
        post_org_state = self.cleaned_data['post_org_state']
        # No Special Characters
        if '<' in post_org_state or '>' in post_org_state or '*' in post_org_state or '/' in post_org_state or '|' in post_org_state or '=' in post_org_state:
            raise forms.ValidationError("State name should not have special characters.")
        post_org_state = escape(post_org_state)
        if len(post_org_state) < 2:
            raise forms.ValidationError("Please enter a real state")
        return post_org_state
    
    def clean_post_org_zipcode(self):
        post_org_zipcode = self.cleaned_data['post_org_zipcode']
        # # No Special Characters
        # if '<' in post_org_zipcode or '>' in post_org_zipcode or '*' in post_org_zipcode or '/' in post_org_zipcode or '|' in post_org_zipcode or '=' in post_org_zipcode:
        #     raise forms.ValidationError("Zipcode should not have special characters.")
        post_org_zipcode = escape(post_org_zipcode)
        if len(post_org_zipcode) < 5:
            raise forms.ValidationError("Please enter a real zip code")
        return post_org_zipcode 
        
    def clean_org_country(self):
        org_country = self.cleaned_data['org_country']
        org_country = escape(org_country)
        
        return org_country

    def clean_org_desc(self):
        org_desc = self.cleaned_data['org_desc']
        org_desc = escape(org_desc)
        if '<' in org_desc or '>' in org_desc or '*' in org_desc or '/' in org_desc or '|' in org_desc or '=' in org_desc:
           raise forms.ValidationError("Description should not have special characters.")
        return org_desc

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        self.fields['password1'].help_text = 'Password must contain at least 8 characters.'
        self.fields['password2'].help_text = ''
        if 'username' in self.fields:
            print("deleting username from form")
            del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email", "your_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(
            self.cleaned_data.get('password2'), self.instance
        )
        return password2


class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        self.fields['password'].help_text = 'Password must contain at least 8 characters'
        self.fields['password'].help_text = ' '
        if 'username' in self.fields:
            print("deleting username from form")
            del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("your_name",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(
            self.cleaned_data.get('password2'), self.instance
        )
        return password2

