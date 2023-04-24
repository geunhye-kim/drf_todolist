from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_edit_view'),
    path('api/token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
