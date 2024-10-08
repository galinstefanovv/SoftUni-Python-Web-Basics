from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetAddForm, PetEditForm, PetDeleteForm


# Create your views here.
@login_required
def pet_add(request):
    form = PetAddForm()

    if request.method == 'POST':
        form = PetAddForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context=context)

@login_required
def pet_details(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()

    context = {
        "pet": pet,
        "all_photos": all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context=context)

@login_required
def pet_edit(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == "GET":
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_name=pet_name)

    context = {
        'form': form,
        'pet_name': pet_name,
        'username': username,
    }

    return render(request, 'pets/pet-edit-page.html', context=context)

@login_required
def pet_delete(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()

    context = {
        'form': form,
        'username': username,
        'pet_name': pet_name,
    }

    return render(request, 'pets/pet-delete-page.html', context=context)
