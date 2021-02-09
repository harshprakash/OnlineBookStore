from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView,ListView,TemplateView
from django.db.models import Q

# Create your views here.
def home(request):
    context ={
        'books':Book.objects.all()
    }
    return render(request,"Book/home.html",context)

#class HomePageView(TemplateView):
    #model= Book
    #template_name="Book/home.html"
class BookDetailView(DetailView):
    model = Book
    template_name="Book/detail.html"
class SearchResultsView(ListView):
    model = Book
    template_name = 'Book/search_result.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list =Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query)
        )
        return object_list