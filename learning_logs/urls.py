"""定义learning_logs的URL模式"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('entries/<int:topic_id>/', views.entries, name='entries'),
    path('new_topic/', views.new_topic, name='new_topic')
]