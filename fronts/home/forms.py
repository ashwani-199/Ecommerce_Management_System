from django import forms
from apps.users.models import User
from django.core.exceptions import ValidationError
from django.forms.widgets import Select

GENDER_CHOICES = (
    ("", "Select"),
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)

class ProfileEditForm(forms.ModelForm):

    username = forms.CharField(
        required=False,
        label='Username',
        widget=forms.TextInput(attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
                                      'placeholder': "Your User Name"}),
        error_messages={
            'required': "The username field is required"
        }
    )

    image = forms.ImageField(
        required=False,
        label='Image',
        widget=forms.FileInput(),
        error_messages={
            'required': "The image field is required"
        }
    )

    first_name = forms.CharField(
        required=False,
        label='First Name',
        widget=forms.TextInput(attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
                                      'placeholder': "Your First Name"}),
        error_messages={
            'required': "The first name field is required"
        }
    )
    last_name = forms.CharField(
        required=False,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
                                      'placeholder': "Your Last Name"}),
        error_messages={
            'required': "The last name field is required"
        }
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False , widget=Select(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30'}))
    email = forms.EmailField(
        required=False,
        label='Email',
        widget=forms.TextInput(attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
                                      'placeholder': "Your Email address"}),
        error_messages={
            'required': "The email field is required",
            # 'invalid': "The email is not valid"
        }
    )

    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'gender', 'email']

    def clean_username(self):
        data = self.cleaned_data
        username = data.get('username')
        if username == "" or username is None:
            raise ValidationError(self.fields['username'].error_messages['required'])
        return username
    
    def clean_image(self):
        data = self.cleaned_data
        image = data.get('image')
        if image == "" or image is None:
            raise ValidationError(self.fields['image'].error_messages['required'])
        return image
    
    def clean_first_name(self):
        data = self.cleaned_data
        first_name = data.get('first_name')
        if first_name == "" or first_name is None:
            raise ValidationError(self.fields['first_name'].error_messages['required'])
        return first_name
    
    def clean_last_name(self):
        data = self.cleaned_data
        last_name = data.get('last_name')
        if last_name == "" or last_name is None:
            raise ValidationError(self.fields['last_name'].error_messages['required'])
        return last_name
    
    def clean_gender(self):
        data = self.cleaned_data
        gender = data.get('gender')
        if gender == "" or gender is None:
            raise ValidationError(self.fields['gender'].error_messages['required'])
        return gender
    
    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email
    


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=False,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30 ",
                   'placeholder': 'Email'}),
        error_messages={
            'required': "The email field is required.",
            'invalid': "email_is_not_valid"
        }
    )
    password = forms.CharField(
        required=False,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': "stext-111 cl2 plh3 size-116 p-l-62 p-r-30",
                   'placeholder': 'Password'}),
        error_messages={
            'required': "The password field is required.",
            'min_value': "The confirm password should contains at least 8 digits",
        }
    )

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email
    
    def clean_password(self):
        data = self.cleaned_data
        password = data.get('password')
        if password == "" or password is None:
            raise ValidationError(self.fields['password'].error_messages['required'])
        elif 8 > len(password) > 0:
            raise ValidationError(self.fields['password'].error_messages['min_value'])
        return password