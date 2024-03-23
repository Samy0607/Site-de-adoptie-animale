from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Animale
from django.views.generic import ListView

def index(request):
    return HttpResponse("Bine ati venit!")
class AnimaleListView(ListView):
    model = Animale
    template_name = "animale.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animale'] = context ['object_list']
        return context
def search_items(request):
    query = request.GET.get('query')
    if query:
        animale = Animale.objects.filter(nume__icontains=query)
    else:
        animale = Animale.objects.all()
    return render(request, 'animal_search.html', {'animale': animale})

def animale_detalii(request, animale_id):
    animale = get_object_or_404(Animale, pk=animale_id)
    return render(request, "animale_detalii.html", {"animale": animale})
def welcome(request):
    return render(request, "welcome.html")
