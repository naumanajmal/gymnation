from django.urls import path
from . import views

urlpatterns = [
path('member/<int:member_id>/', views.member_profile, name='member_profile'),
]
