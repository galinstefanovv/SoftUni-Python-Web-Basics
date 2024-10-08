from django import forms
from .models import Photo

labels = {
    'pet_image': 'Photo file',
    'description': 'Description',
    'location': 'Location',
    'tagged_pets': 'Tag Pets'
}


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pet_image', 'description', 'location', 'tagged_pets']
        labels = labels


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'location', 'tagged_pets']
        exclude = ['pet_image']
        labels = labels
