from django.urls import path
from .views import TextView, PeselView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("text/", TextView.as_view(), name="text_view"),
    path("pesel/", PeselView.as_view(), name="pesel_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
