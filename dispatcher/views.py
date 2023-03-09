from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dispatcher.models import Users, Landmarks, Cities
from django.http import JsonResponse

API_TOKEN = 'mgGp76209aN4AJUaGZA1ByVoLVBHcfpfJ1nF5D/a08TbcRlXOIIvmdd9Wkw!KdV?lwz5xSeEYsoPl0mkN76lmYYzdxLVQ!KqfWwX-NTGiXy00F?YXeRqGfP93dfOng9jhA=zG9nnHzQojZG!KEtxJGShgNRG2rhWLW4zBJIqngMMBEkDdpzoXZ8CnefF0!/13KrTBoff6H2xN5L9Ttt8?0nqmLdnPsZiPXrZ2T32w8t7KaEaAe72zMxvluEhT!8L'

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        response = HttpResponse()
        if request.GET.get('token') == API_TOKEN:#Проверка токена
            user = Users(login = request.GET.get('login'), password = request.GET.get('password'))
            for i in Users.objects.all():
                if i.login == user.login:#Логин уже использован
                    response.headers['success'] = 0
                    return response
            response.headers['success'] = 1#Успешное создание пользователя
            user.save()
        else:
            response.headers['success'] = -1#Токен отвергнут
        return response
def get_landmark(request):#Передаёт все данные о достопримечательностях из базы данных
    data = dict(data=[dict()])
    info = []
    for i in Landmarks.objects.all():
        info.append(dict(name = i.name, description = i.description, latitude = i.latitude, longitude = i.longitude, image = i.image))
    data.update(data=info)
    response = JsonResponse(data = data)#Все достопримечательности в json формате
    return response
def sign_in(request):
    if request.method == 'GET':
        response = HttpResponse()
        user = Users(login=request.GET.get('login'), password=request.GET.get('password'))
        for i in Users.objects.all():
                if i.login == user.login:
                    if i.password == user.password:
                        response.headers['success'] = 1#Успешная авторизация
                        return response
                    else:
                        response.headers['success'] = -1#Неверный пароль
                        return response
        response.headers['success'] = 0#Пользователь не найден
        return response