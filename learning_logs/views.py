from django.shortcuts import render
from .models import Topic

def index(request):
	return render(request,'learning_logs/index.html')

def topics(request):
	"""显示所有主题"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html',context)

def topic(request, topic_id):
	"""显示单个主题及其所有项目"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request,'learning_logs/topic.html',context)
# Create your views here.
