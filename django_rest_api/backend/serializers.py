from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import TraceList, TradeDetail

class TraceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraceList
        fields = ['stock_num', 'stock_name']

    def get_trace_list(self):
        stock_ract_list = TraceList.objects.all()
        return stock_ract_list

    def create(self, validated_data):
        stock = TraceList.objects.create(
            stock_num=validated_data['stock_num'],
            stock_name=validated_data['stock_name']
        )
        return stock

class StockTradeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeDetail
        fields = [
            'brokerage_name', 'total', 'buy_avg',
            'buy_quantity', 'sell_avg', 'sell_quantity'
        ]

    def get_detail_by_date(**kwargs):
        detail = TradeDetail.objects.filter(**kwargs).order_by('-total')
        return detail

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','email']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid login.")
