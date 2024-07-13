from django.shortcuts import render, redirect
from learning_logs.models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def entries(request, topic_id):
    # 根据topic_id找到相关的topic
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        # 增加新的Entry
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
    # 找到该topic下的entry集合
    entries = topic.entry_set.order_by('-date_added')
    # context里包含topic以及entry集合
    context = {'topic': topic, 'entries': entries, 'form': form}
    return render(request, 'learning_logs/entries.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    print(context)
    return render(request, 'learning_logs/new_topic.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:entries', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)









