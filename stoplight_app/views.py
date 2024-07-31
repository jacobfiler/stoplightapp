from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Reform, State, ReformStatus, ReformArea
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Reform
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReformSerializer, StateSerializer, ReformStatusSerializer, ReformAreaSerializer
from django.contrib.auth.decorators import login_required

@login_required
def home_default(request):
    return home(request, data_version='new')

@login_required
def home(request, data_version='new'):
    # Fetch all Reform objects based on data version
    if data_version == 'old':
        reforms = Reform.objects.filter(version=1).order_by('slcid', 'name')
    else:
        reforms = Reform.objects.filter(version=2).order_by('slcid', 'name')
        
    context = {
        'reforms': reforms,
    }
    return render(request, 'stoplight_app/home.html', context)


@login_required
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
    
@login_required
def reform_detail(request, slcid):
    reform = get_object_or_404(Reform, slcid=slcid)
    statuses = ReformStatus.objects.filter(reform=reform)

    status_details = {
        'green': statuses.filter(status=ReformStatus.StatusChoices.GREEN),
        'red': statuses.filter(status=ReformStatus.StatusChoices.RED),
        'yellow': statuses.filter(status=ReformStatus.StatusChoices.YELLOW),
        'blue': statuses.filter(status=ReformStatus.StatusChoices.BLUE),
        'black': statuses.filter(status=ReformStatus.StatusChoices.BLACK),
        'null': statuses.filter(status=ReformStatus.StatusChoices.NULL)
    }

    status_counts = {key: value.count() for key, value in status_details.items()}

    context = {
        'reform': reform,
        'status_counts': status_counts,
        'status_details': status_details,
    }
    return render(request, 'stoplight_app/reform_detail.html', context)
