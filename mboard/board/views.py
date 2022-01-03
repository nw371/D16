from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .forms import PostForm
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

class Create(CreateView):
    template_name = 'board/create.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save()
        post.save()
        return redirect(f'/{post.id}')

class CategoryView(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    context_object_name = 'category'
    template_name = 'board/category.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    paginate_by = 5

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['categoryview'] = Post.objects.filter(category=id).order_by('-date')  # вписываем наш фильтр в контекст
        usr = self.request.user.id
        context['category'] = Category.objects.get(id=id)
        print(f'THIS IS CINTEXT: {context}')
        return context


