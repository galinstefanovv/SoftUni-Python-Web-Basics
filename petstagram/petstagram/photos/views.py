from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from .forms import PhotoAddForm
from .models import Photo
from django.views import generic as views


# Create your views here.

class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoAddForm


    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# def photo_add(request):
#     return render(request, 'photos/photo-add-page.html')


@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, 'photos/photo-details-page.html', context=context)


@login_required
def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
