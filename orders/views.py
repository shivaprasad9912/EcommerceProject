from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from notifications.utils import send_order_notification

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product').order_by('-created_at')

    def perform_create(self, serializer):
        order = serializer.save()
        send_order_notification(order.user.id, f'Your order #{order.id} has been placed successfully.')

class OrderRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')

    def perform_update(self, serializer):
        old_status = self.get_object().status
        order = serializer.save()
        
        if old_status != order.status:
            send_order_notification(
                order.user.id, 
                f'Your order #{order.id} status has been updated to {order.status}.'
            )