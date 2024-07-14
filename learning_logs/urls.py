"""定义learning_logs的URL模式"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 主题陈列
    path('topics/', views.topics, name='topics'),
    # 主题下的条目清单并可直接添加条目
    path('entries/<int:topic_id>/', views.entries, name='entries'),
    # 增加一个主题
    path('new_topic/', views.new_topic, name='new_topic'),
    # 编辑某主题下的条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]