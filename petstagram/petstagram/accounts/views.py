from django.http import HttpResponse
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.shortcuts import render
from petstagram.accounts.forms import RegisterUserForm, LoginUserForm
from petstagram.pets.models import Pet
from django.contrib.auth import mixins as auth_mixin

UserModel = get_user_model()
class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('index')


class LogoutUserView(auth_views.LogoutView):
    pass


# def register_user(request):
#     return render(request, 'accounts/register-page.html')


# def login_user(request):
#     return render(request, 'accounts/login-page.html')


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        context['profile_image'] = profile_image
        context['pets'] = self.request.user.pet_set.all()

        return context
class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'

# def profile_details(request, pk):
#     pets = Pet.objects.all()
#
#     context = {
#         'pets': pets,
#     }
#
#     return render(request, 'accounts/profile-details-page.html', context=context)
#
#
# def profile_edit(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')
#
#
# def profile_delete(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')
