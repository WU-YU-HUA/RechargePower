from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate
from .serializer import User, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login(request, *args, **kwargs):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if not user:
        return Response({
            "success": False,
            "message": "登入失敗",
            "detail": "帳號or密碼錯誤"
        }, status=400)
    
    jwttoken = RefreshToken.for_user(user)
    access = jwttoken.access_token

    return Response({"token": str(access)})

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        name = data.get('name')
        email = data.get('email')

        user, created = User.objects.update_or_create(
            email=email,
            defaults={
                'username': username,
                'name': name,
                'is_active': True,
            }
        )
        user.set_password(password)
        user.save()

        return Response(UserSerializer(user).data, status=201)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(pk=id)
        user.delete()
        return Response("", status=204)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(pk=id)
        
        return Response(UserSerializer(user).data, status=200)

@api_view(['POST'])
@authentication_classes([JWTAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def deposite(request, *args, **kwargs):
    data = request.data
    point = data.get('point', 0)
    user = request.user
    user.point += point
    user.save()

    return Response({
        "success": True,
        "message": "儲值成功",
        "detail": f"目前點數: {user.point}"
    }, status=200)