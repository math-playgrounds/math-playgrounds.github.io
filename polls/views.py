from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')

def room(request, room_name):
    return render(request, 'polls/room.html', {
        'room_name': room_name
    })
