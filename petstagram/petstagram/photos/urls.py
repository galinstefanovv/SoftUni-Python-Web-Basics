from django.urls import path, include
from .views import photo_details, photo_edit, PhotoAddView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # localhost:8000/photos/
    path('add/', PhotoAddView.as_view(), name="photo add"),
    path('<int:pk>/', include([
        path('', photo_details, name='photo details'),
        path('edit/', photo_edit, name="photo edit"),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)