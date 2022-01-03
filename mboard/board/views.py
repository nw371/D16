from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Category


class IndexPage(TemplateView):
    template_name = 'default.html'
# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'board/view.html'  # название шаблона будет post.html
    context_object_name = 'post'  # название объекта. в нём будет

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'board/categories.html'
    queryset = Category.objects.all()