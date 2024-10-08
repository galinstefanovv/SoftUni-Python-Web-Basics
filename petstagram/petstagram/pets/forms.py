from django import forms
from .models import Pet


class BaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_pet_photo']
        widgets = {
            'name': forms.Textarea(
                attrs={
                    'placeholder': 'Pet name',

                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_pet_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )

        }
        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_pet_photo': 'Link to image',
        }


class PetAddForm(BaseForm):
    pass


class PetEditForm(BaseForm):
    pass


class PetDeleteForm(BaseForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


