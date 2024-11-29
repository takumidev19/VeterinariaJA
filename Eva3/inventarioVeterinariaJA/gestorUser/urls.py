from django.urls import path

from gestorUser.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]