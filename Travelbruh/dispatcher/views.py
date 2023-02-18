from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dispatcher.models import Users, Landmarks, Cities

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
def initialise(request):
    Mark = Landmarks(name = "dummy", description = "dummy", city_id = 0)
    Mark.save
    Mark = Cities(name="dummy", description="dummy")
    Mark.save
    return HttpResponse