from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_trainer_code': 'Trainer Code',
            'default_email': 'Email',
        }

        self.fields['default_trainer_code'].widget.attrs['autofocus'] = True
