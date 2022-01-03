from django.forms import ModelForm

from .models import Post, User


# Создаём модельную форму
class PostForm(ModelForm):
    # # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    # def __init__(self, *args, **kwargs):
    #     """ Grants access to the request object so that only members of the current user
    #     are given as options"""
    #
    #     self.request = kwargs.pop('request')
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].queryset = User.objects.filter(id=self.request.user)
    class Meta:
        model = Post
        fields = ['name', 'body', 'category', 'user']