from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from user.serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import Http404
from rest_framework.views import APIView
from user.forms import UserRegister, UserLogin
from django.contrib.auth import login, authenticate, logout

# signin and signup views -----------------------------------------------------------

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("home-page")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home-page")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home-page")

#Permission in the views ------------------------------------------

# def some_view(request):
#     if request.user.is_anonymous:
#         return redirect("login")

# def some_view(request):
#     if not request.user.is_staff:
#         raise Http404



#API Views----------------------------------------------------------

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)