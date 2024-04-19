from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Reform, State, ReformStatus, ReformArea
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Reform
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReformSerializer, StateSerializer, ReformStatusSerializer, ReformAreaSerializer

def home(request):
    # Fetch all Reform objects
    reforms = Reform.objects.all().order_by('slcid', 'name')
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
    

@api_view(['GET', 'POST'])
def reform_list(request):
    if request.method == 'GET':
        reforms = Reform.objects.all()
        serializer = ReformSerializer(reforms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def reform_status_detail(request, pk):
    try:
        reform_status = ReformStatus.objects.get(pk=pk)
    except ReformStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReformStatusSerializer(reform_status)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReformStatusSerializer(reform_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def reform_area_list(request):
    if request.method == 'GET':
        reform_areas = ReformArea.objects.all()
        serializer = ReformAreaSerializer(reform_areas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReformAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def reform_area_detail(request, pk):
    try:
        reform_area = ReformArea.objects.get(pk=pk)
    except ReformArea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReformAreaSerializer(reform_area)
        return Response(serializer.data)