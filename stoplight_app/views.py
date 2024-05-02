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
def home(request):
    # Fetch all Reform objects
    reforms = Reform.objects.all().order_by('slcid', 'name')
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

@api_view(['GET', 'POST', 'PUT'])
def reform_status_detail(request, pk=None):
    if request.method == 'GET':
        try:
            reform_status = ReformStatus.objects.get(pk=pk)
            serializer = ReformStatusSerializer(reform_status)
            return Response(serializer.data)
        except ReformStatus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method in ['POST', 'PUT']:
        data = request.data
        if pk:
            try:
                reform_status = ReformStatus.objects.get(pk=pk)
                serializer = ReformStatusSerializer(reform_status, data=data)
            except ReformStatus.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ReformStatusSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED if request.method == 'POST' else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def reform_area_list(request, pk):
    try:
        reform_area = ReformArea.objects.get(pk=pk)
    except ReformArea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReformAreaSerializer(reform_area)
        return Response(serializer.data)

@api_view(['GET'])
def state_list(request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)