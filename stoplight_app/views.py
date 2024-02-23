from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Reform, State, ReformStatus
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

def StateReforms(request, state_name):
    # Fetch the State object by name
    state = get_object_or_404(State, name=state_name)
    # Fetch all ReformStatus objects for the given state
    reform_statuses = ReformStatus.objects.filter(state=state).select_related('reform', 'state').order_by('reform__name')
    context = {
        'reform_statuses': reform_statuses,
        'state': state,
    }
    return render(request, 'stoplight_app/state_reforms.html', context)
    

