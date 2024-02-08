from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Reform
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Reform

def home(request):
    # Fetch all Reform objects
    reforms = Reform.objects.all().order_by('slcid', 'name')  # Ordering by name for better readability
    context = {
        'reforms': reforms,
    }
    return render(request, 'stoplight_app/home.html', context)


class ReformCreate(CreateView):
    model = Reform
    fields = ['name', 'description', 'slcid', 'criteria', 'reform_area']
    template_name = 'stoplight_app/reform_form.html'
    succuss_url = reverse_lazy('home')

class ReformUpdate(UpdateView):
    model = Reform
    fields = ['name', 'description', 'slcid', 'criteria', 'reform_area']
    template_name = 'stoplight_app/reform_form.html'
    succuss_url = reverse_lazy('home')

    

