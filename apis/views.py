from rest_framework import generics
from library.models import Books
from .serializers import BooksSerializer

# Create your views here.

class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    