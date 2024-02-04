from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy


from .models import *
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):

    all_books = Book.objects.all()

    book_nums = Book.objects.all().count()
    book_instances = BookInstance.objects.all().count()
    book_avails = BookInstance.objects.filter(status='a').count()
    book_titles = [book.title for book in all_books]

    context = {
        'book_nums': book_nums,
        'book_instances': book_instances,
        'book_avails': book_avails,
        'book_titles': book_titles,
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book

class SignUpView(CreateView):

    form_class = UserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'catalog/signup.html'

class ProfileBookView(LoginRequiredMixin, ListView):
    model = BookInstance

    template_name = 'catalog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()



