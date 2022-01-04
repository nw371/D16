from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from .forms import PostForm
from .models import Post


class IndexPage(TemplateView):
    template_name = 'default.html'
# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'board/view.html'  # название шаблона будет post.html
    context_object_name = 'post'  # название объекта. в нём будет

class Create(CreateView):
    template_name = 'board/create.html'
    form_class = PostForm




