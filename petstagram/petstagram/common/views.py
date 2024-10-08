from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from petstagram.photos.models import Photo
from .forms import SearchForm, CommentForm
from .models import Like
from pyperclip import copy


# Create your views here.

def index(request):
    photos = Photo.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        photos = photos.filter(
            tagged_pets__name__icontains=search_text
        )

    for photo in photos:
        photo.liked_by_user = photo.like_set.filter(user=request.user.id).exists()

    context = {
        'all_photos': photos,
        'form': CommentForm(),
        'search_form': search_form
    }

    return render(request, 'common/home-page.html', context=context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    like_object = Like.objects.filter(
        to_photo_id=photo_id,
        user=request.user
    ).first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(to_photo=photo, user=request.user)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo.id}')


@login_required
def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
