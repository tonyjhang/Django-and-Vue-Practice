from django.urls import path

from .views import RegistrationAPI, LoginAPI, \
        UserAPI, StockTraceListAPI, StockTradeDetailAPI

urlpatterns = [
    path('register', RegistrationAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('user', UserAPI.as_view()),
    path('trace', StockTraceListAPI.as_view()),
    path(
        r'stock/<str:stock_num>/date/<str:date>', 
        StockTradeDetailAPI.as_view()
    )
]