from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dispatcher.models import Users, Landmarks, Cities
from django.http import JsonResponse

# Create your views here.
def add_user(request):
    print(request.GET.__getitem__('login') + ' || ' + request.GET.__getitem__('password'))
    User = Users(login = request.GET.__getitem__('login'), password = request.GET.__getitem__('password'))
    response = HttpResponse()
    for i in Users.objects.all():
        if i.login == User.login:
            response.headers['success'] = 0
            return response
    response.headers['success'] = 1
    User.save()
    return response
def check_users(request):
    s = ""
    for i in Users.objects.all():
        #i.get(id = i).login
        s = s + i.login
    response = HttpResponse(s)
    return response

def get_landmark(request):
    data = dict(data=[dict()])
    for i in Landmarks.objects.all():
        data.update(data=[dict(name = i.name, description = i.description, latitude = i.latitude, longitude = i.longitude)])
    response = JsonResponse(data = data)
    return response
