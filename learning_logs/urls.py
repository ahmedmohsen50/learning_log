"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    ]
