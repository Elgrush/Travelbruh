from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dispatcher.models import Users, Landmarks, Cities
from django.http import JsonResponse

API_TOKEN = 'mgGp76209aN4AJUaGZA1ByVoLVBHcfpfJ1nF5D/a08TbcRlXOIIvmdd9Wkw!KdV?lwz5xSeEYsoPl0mkN76lmYYzdxLVQ!KqfWwX-NTGiXy00F?YXeRqGfP93dfOng9jhA=zG9nnHzQojZG!KEtxJGShgNRG2rhWLW4zBJIqngMMBEkDdpzoXZ8CnefF0!/13KrTBoff6H2xN5L9Ttt8?0nqmLdnPsZiPXrZ2T32w8t7KaEaAe72zMxvluEhT!8L'

# Create your views here.
def add_user(request):
    response = HttpResponse()
    if(request.GET.__getitem__('token') == API_TOKEN):
        print(request.GET.__getitem__('login') + ' || ' + request.GET.__getitem__('password'))
        User = Users(login = request.GET.__getitem__('login'), password = request.GET.__getitem__('password'))
        for i in Users.objects.all():
            if i.login == User.login:
                response.headers['success'] = 0
                return response
        response.headers['success'] = 1
        User.save()
    else:
        response.headers['success'] = 0
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
        data.update(data=[dict(name = i.name, description = i.description, latitude = i.latitude, longitude = i.longitude, image = i.image)])
    response = JsonResponse(data = data)
    return response
