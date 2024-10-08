from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from .validators import image_size_validator_5mb

# Create your models here.
UserModel = get_user_model()


class Photo(models.Model):
    pet_image = models.ImageField(
        blank=False,
        null=False,
        validators=(image_size_validator_5mb,),
        upload_to="photos/"
    )
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ["-date_of_publication"]

    def __str__(self):
        return f'{self.pk} - {self.pet_image}'
