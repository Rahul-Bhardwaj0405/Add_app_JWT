from django.urls import path
from .views import signup_view, login_view
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
 ]

# path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),

#     ########################################### API TOKEN ############################
#     path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),