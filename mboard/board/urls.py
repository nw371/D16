from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import IndexPage, PostDetail, Create

urlpatterns = [
    path('', IndexPage.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view()),
    path('create/', Create.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)