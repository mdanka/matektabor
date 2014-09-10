import json
from django.shortcuts import render
from django.http import HttpResponse

from barkochba.models import Story, Person


def main(request):
	story_list = Story.objects.order_by('order_number')
	stories = []
	for story in story_list:
		person_ids = story.people.values_list('id', flat=True)
		person_ids_json = '["' + '", "'.join(str(person_id) for person_id in person_ids) + '"]'
		story_map = {}
		story_map['story'] = story
		story_map['person_ids_json'] = person_ids_json
		stories.append(story_map)
	context = {
		'stories': stories
	}
	return render(request, 'barkochba/main.html', context)

def person_search(request):
	query = request.GET.get('q', '')
	normalized_query = query.lower()  # kisbetu
	normalized_query = normalized_query.replace(u'a', u'(a|\u00e1)')  # a
	normalized_query = normalized_query.replace(u'e', u'(e|\u00e9)')  # e
	normalized_query = normalized_query.replace(u'i', u'(i|\u00ed)')  # i
	normalized_query = normalized_query.replace(u'o', u'(o|\u00f3|\u00f6|\u0151)')  # o
	normalized_query = normalized_query.replace(u'u', u'(u|\u00fa|\u00fc|\u0171)')  # u

	person_list = Person.objects.filter(
		name__iregex=r'' + normalized_query
	)
	resultJson = [{'id': p.id, 'name': p.name} for p in person_list]
	output = json.dumps(resultJson)
	return HttpResponse(output)