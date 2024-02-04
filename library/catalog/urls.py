from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('create/', BookCreate.as_view(), name='create'),
	path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/', ProfileBookView.as_view(), name='profile'),
]