from django.shortcuts import get_object_or_404, render

from szobabeosztas.models import Camp, Room
from barkochba.models import Story

def index(request):
	camp_list = Camp.objects.order_by('group__name', 'number')
	context = {'camp_list': camp_list}
	return render(request, 'export/index.html', context)

def camp_export(request, camp_id):
	camp = get_object_or_404(Camp, pk=camp_id)
	rooms = camp.room_set.all()
	story_list = Story.objects.order_by('order_number')
	stories = []
	storiesWithZeroOrderNumber = []
	for story in story_list:
		story_map = {}
		story_map['story'] = story
		story_map['people'] = story.people.all()
		story_map['rooms'] = []
		for room in rooms:
			room_people_ids = room.people.all().values('id')
			people = story.people.filter(id__in=room_people_ids).order_by('name')
			if (not people):
				continue
			room_map = {}
			room_map['room'] = room.name
			room_map['people'] = people
			story_map['rooms'].append(room_map)
		if story.order_number == 0:
			storiesWithZeroOrderNumber.append(story_map)
		else:
			stories.append(story_map)
	stories.extend(storiesWithZeroOrderNumber)
	context = {'stories': stories, 'camp': camp}
	return render(request, 'export/camp_export.html', context)


