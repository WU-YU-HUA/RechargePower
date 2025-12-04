from .serializer import Order, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET'])
@authentication_classes([JWTAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def list(request, *args, **kwargs):
    orders = Order.objects.all()
    return Response(OrderSerializer(orders, many=True).data, status=200)