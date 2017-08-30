from rest_framework.serializers import ModelSerializer, FloatField

from orders.models import Order, OrderLineItem


class OrderLineItemSerializer(ModelSerializer):
    class Meta:
        model = OrderLineItem
        fields = '__all__'


class OrderSummarySerializer(ModelSerializer):
    total_price = FloatField()

    class Meta:
        model = Order
        fields = ('id', 'total_price', 'date_ordered', 'status')


class OrderSerializer(ModelSerializer):
    total_price = FloatField()

    class Meta:
        model = Order
        fields = '__all__'
