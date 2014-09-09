from django.shortcuts import render
from django.http import HttpResponse

from barkochba.models import Story


def main(request):
	story_list = Story.objects.order_by('order_number')
	context = {'story_list': story_list}
	output = '<br />'.join([story.title for story in story_list])
	return render(request, 'barkochba/main.html', context)
