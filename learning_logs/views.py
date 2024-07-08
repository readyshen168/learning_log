from django.shortcuts import render, redirect
from learning_logs.models import Topic
from .forms import TopicForm


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    # 根据topic_id找到相关的topic
    topic = Topic.objects.get(id=topic_id)
    # 找到该topic下的entry集合
    entries = topic.entry_set.order_by('-date_added')
    # context里包含topic以及entry集合
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)