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
            response.headers['login_accept'] = 1  # Успешное создание пользователя
            response.headers['name_accept'] = 1
            for i in Users.objects.all():
                if i.login == user.login:  # Логин уже использован
                    response.headers['login_accept'] = 0
                    return response
            if request.GET.get('name') is not None:
                user.name = request.GET.get('name')
                for i in Users.objects.all():
                    if i.name == user.name:  # Имя занято
                        response.headers['name_accept'] = 0
                        user = Users(login=request.GET.get('login'), password=request.GET.get('password'),
                                     name=request.GET.get('login'))
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
        user = Users(login=request.GET.get('login'), password=request.GET.get('password'))
        for i in Users.objects.all():
            if i.login == user.login:
                response.headers['login_accept'] = 1
                if i.password == user.password:
                    response.headers['password_accept'] = 1  # Успешная авторизация
                    return response
                else:
                    response.headers['password_accept'] = 0  # Неверный пароль
                    return response
        response.headers['login_accept'] = 0  # Пользователь не найден
        return response


# login, password, name
def change_name(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        user = Users(login=request.GET.get('login'), password=request.GET.get('password'), name=request.GET.get('name'))
        for i in Users.objects.all():
            if i.login == user.login:
                response.headers['login_accept'] = 1
                if i.password == user.password:
                    response.headers['password_accept'] = 1  # Пароль принят
                    response.headers['name_accept'] = 1
                    for q in Users.objects.all():
                        if q.name == user.name:
                            response.headers['name_accept'] = 0  # Имя занято
                            return response
                    response.headers['name_accept'] = 1  # Имя принято
                    i.name = user.name
                    i.save()
        return response


# login, password, city id(additional)
def suggest_landmark(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.headers['login_accept'] = 0
        response.headers['password_accept'] = 0
        user = Users(login=request.GET.get('login'), password=request.GET.get('password'), name=request.GET.get('name'))
        for i in Users.objects.all():
            if i.login == user.login:
                user_id = i.id
                response.headers['login_accept'] = 1
                if i.password == user.password:
                    response.headers['password_accept'] = 1  # Пароль принят
                    suggestion = LMSuggestion(user_id=user_id, city_id=request.GET.get('city_id') if (
                            request.GET.get('city_id') is not None) else -1, message=request.GET.get('message'))
                    suggestion.save()
        return response


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
        if request.GET.get('landmark') is None:  # проверка наличия id
            return response
        landmark = int(request.GET.get('landmark'))  # id достопримечательности
        i = Landmarks.objects.get(id=landmark)
        if i is None:  # проверка существования достопримечательности
            return response
        response.headers['landmark_accept'] = 1  # достопримечательность принята
        for i in Users.objects.all():
            if i.login == login:
                response.headers['login_accept'] = 1  # Логин принят
                if i.password == password:
                    response.headers['password_accept'] = 1  # Пароль принят
                    if i.visits is None:
                        i.visits = []
                    if landmark not in i.visits:  # Проверка посещал ли пользователь место раньше
                        i.visits.append(landmark)
                        i.save()
        return response
