from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import CreateUserSerializer, UserSerializer, \
    LoginUserSerializer, TraceListSerializer, StockTradeDetailSerializer

# Create your views here.
class RegistrationAPI(generics.GenericAPIView):
    permission_classes = []
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    permission_classes = []
    serializer_class = LoginUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class StockTradeDetailAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StockTradeDetailSerializer
    page_class = PageNumberPagination()
    
    def get(self, request, *args, **kwargs):
        detail = StockTradeDetailSerializer.get_detail_by_date(**kwargs)
        
        page = self.page_class.paginate_queryset(queryset=detail, request=request)
        if page is not None:
            serializer = StockTradeDetailSerializer(page, many=True)
            return self.page_class.get_paginated_response(serializer.data)
        
        serializer = StockTradeDetailSerializer(detail, many=True)
        return Response({
            'detail': serializer.data   
        })

class StockTraceListAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TraceListSerializer

    def get(self, _):
        stock_trace_list = TraceListSerializer().get_trace_list()
        return Response({
            'trace_list': TraceListSerializer(stock_trace_list, many=True).data   
        })

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stock = serializer.save()
        return Response({
            "stock": TraceListSerializer(stock, context=self.get_serializer_context()).data
        })

