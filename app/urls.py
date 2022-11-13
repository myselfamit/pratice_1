from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pre_home/', views.pre_home, name='pre_home'),
    path('home/', views.home, name='home'),
    path('graph2/', views.graph2, name='graph2'),
    path('register/', views.register, name='register'),
    path('activity_messages/', views.activity_messages, name='activity_messages'),
    path('friends_and_followers/', views.friends_and_followers, name='friends_and_followers'),
    path('ads_information/', views.ads_information, name='ads_information'),
    path('apps_and_websites/', views.apps_and_websites, name='apps_and_websites'),
    path('your_interactions_on_facebook/', views.your_interactions_on_facebook, name='your_interactions_on_facebook'),
    path('your_topics/', views.your_topics, name='your_topics'),
    path('other_logged_information/', views.other_logged_information, name='other_logged_information'),
    path('pages_only/', views.pages_only, name='pages_only'),
    path('facebook_gaming/', views.facebook_gaming, name='facebook_gaming'),
    path('events/', views.events, name='events'),
    path('messages_only/', views.messages_only, name='messages_only'),
    path('profile_information/', views.profile_information, name='profile_information'),
    path('groups/', views.groups, name='groups'),
    path('amit/', views.amit, name='amit'),
]
