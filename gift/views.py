from .serializer import Gift, GiftSerializer
from order.models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class GiftViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # 設定哪些不需要權限
        if self.action in ['retrieve', 'list']:
            return [AllowAny()]
        
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({
                "success": False,
                "message": "創建贈品失敗",
                "detail": "只有員工可以創立贈品"
            }, status=401)
        
        return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     pass

    def list(self, request, *args, **kwargs):
        return Response(GiftSerializer(self.queryset.exclude(amount=0), many=True).data, status=200)
    
@api_view(['POST'])
@authentication_classes([JWTAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def exchange(request, *args, **kwargs):
    data = request.data
    quantity = data.get('quantity')
    gift = Gift.objects.get(pk=data.get('id'))
    total = quantity * gift.point

    if request.user.point < total:
        return Response({
            "success": False,
            "message": "兌換贈品失敗",
            "detail": "點數不足"
        }, status=400)
    
    request.user.point -= total
    request.user.save()
    gift.amount -= quantity
    gift.save()
    
    Order.objects.create(
        gift=gift,
        user=request.user,
        amount=quantity,
        point=gift.point
    )

    return Response({
        "success": True,
        "message": f"已成功兌換 {gift.name}: {quantity}",
        "detail": f"剩餘點數{request.user.point}"
    })