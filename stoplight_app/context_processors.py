from .models import State

def states_processor(request):
    states = State.objects.all()
    return {'states': states}