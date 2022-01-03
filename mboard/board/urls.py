from django.urls import path
from .views import IndexPage, PostDetail, CategoryList, Create, CategoryView

urlpatterns = [
    path('', IndexPage.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('create/', Create.as_view()),
    path('category/<int:pk>', CategoryView.as_view(), name="category"),
]