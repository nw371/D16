from django.urls import path
from .views import IndexPage, PostDetail, CategoryList

urlpatterns = [
    path('', IndexPage.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view()),
    path('categories/', CategoryList.as_view()),
]