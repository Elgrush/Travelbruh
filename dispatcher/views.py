from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dispatcher.models import Users, Landmarks, Cities, LMSuggestion
from django.http import JsonResponse

API_TOKEN = 'mgGp76209aN4AJUaGZA1ByVoLVBHcfpfJ1nF5D/a08TbcRlXOIIvmdd9Wkw!KdV?lwz5xSeEYsoPl0mkN76lmYYzdxLVQ!KqfWwX-NTGiXy00F?YXeRqGfP93dfOng9jhA=zG9nnHzQojZG!KEtxJGShgNRG2rhWLW4zBJIqngMMBEkDdpzoXZ8CnefF0!/13KrTBoff6H2xN5L9Ttt8?0nqmLdnPsZiPXrZ2T32w8t7KaEaAe72zMxvluEhT!8L'


# login, password, token, name(additional)
def sign_up(request):
    if request.method == 'GET':
        response = HttpResponse()
        if request.GET.get('token') == API_TOKEN:  # Проверка токена
            response.headers['token_accept'] = 1  # Токен принят
            user = Users(login=request.GET.get('login'), password=request.GET.get('password'))
            response.headers['login_accept'] = 0
            response.headers['name_accept'] = 0
            i = Users.objects.get(login=request.GET.get('login'))
            if i is not None:
                return response
            response.headers['login_accept'] = 1  # Логин принят
            if request.GET.get('name') is not None:
                user.name = request.GET.get('name')
                i = Users.objects.get(name=request.GET.get('name'))
                if i is not None:  # Имя занято
                    response.headers['name_accept'] = 0
                    user.name = request.GET.get('login')
            else:
                user.name = user.login  # Создание стандартного имени
            user.save()
        else:
            response.headers['token_accept'] = 0  # Токен отвергнут
        return response


# none
def get_landmark(request):  # Передаёт все данные о достопримечательностях из базы данных
    data = dict(data=[dict()])
    info = []
    for i in Landmarks.objects.all():
        info.append(
            dict(name=i.name, description=i.description, latitude=i.latitude, longitude=i.longitude, image=i.image))
    data.update(data=info)
    response = JsonResponse(data=data)  # Все достопримечательности в json формате
    return response


# login, password
def sign_in(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        i = Users.objects.get(login=request.GET.get('login'))
        if i is None:
            return response
        response.headers['login_accept'] = 1  # Логин принят
        if i.password != request.GET.get('password'):
            return response
        response.headers['password_accept'] = 1  # Пароль принят
        return response


# login, password, name
def change_name(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        i = Users.objects.get(login=request.GET.get('login'))
        if i is None:
            return response
        response.headers['login_accept'] = 1  # Логин принят
        if i.password != request.GET.get('password'):
            return response
        response.headers['password_accept'] = 1  # Пароль принят
        if Users.objects.get(name=request.GET.get('name')) is not None:
            response.headers['name_accept'] = 0  # Имя занято
            return response
        response.headers['name_accept'] = 1  # Имя принято
        i.name = request.GET.get('name')
        i.save()
        return response


# login, password, name, city id(additional), message(additional)
def suggest_landmark(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        i = Users.objects.get(login=request.GET.get('login'))
        if i is None:
            return response
        response.headers['login_accept'] = 1  # Логин принят
        if i.password != request.GET.get('password'):
            return response
        response.headers['password_accept'] = 1  # Пароль принят
        suggestion = LMSuggestion(user_id=i.id,
                                  city_id=request.GET.get('city_id'),
                                  name=request.GET.get('name'),
                                  message=request.GET.get('message'))
        suggestion.save()
        return response


# login, password, landmark_id, token
def visit(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['token_accept'] = 0
        response.headers['landmark_accept'] = 0
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        if request.GET.get('token') != API_TOKEN:
            return response
        response.headers['token_accept'] = 1
        login = request.GET.get('login')
        password = request.GET.get('password')
        if request.GET.get('landmark') is None:  # Проверка наличия id
            return response
        landmark = int(request.GET.get('landmark'))  # Id достопримечательности
        i = Landmarks.objects.get(id=landmark)
        if i is None:  # Проверка существования достопримечательности
            return response
        response.headers['landmark_accept'] = 1  # Достопримечательность принята
        i = Users.objects.get(login=request.GET.get('login'))
        if i is None:
            return response
        response.headers['login_accept'] = 1  # Логин принят
        if i.password != request.GET.get('password'):
            return response
        response.headers['password_accept'] = 1  # Пароль принят
        if i.visits is None:
            i.visits = []
        if landmark not in i.visits:  # Проверка посещал ли пользователь место раньше
            i.visits.append(landmark)
            i.save()
        return response
