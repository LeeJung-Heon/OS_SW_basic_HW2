from django.db.models import F, Avg
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import	reverse
from django.views import generic

from .models import Project, Choice, Rating

def project_ranking(request):
    projects = Project.objects.annotate(
        avg_rating = Avg('ratings__stars')
    ).order_by('-avg_rating', 'title')
    return render(request, 'grading/project_ranking.html', {
        'projects':projects
    })

class IndexView(generic.ListView):
    template_name = "grading/index.html"
    context_object_name = "latest_project_list"

    def get_queryset(self):
        return Project.objects.order_by("-pub_date")[:11]

class DetailView(generic.DetailView):
    model = Project
    template_name = "grading/detail.html"


class ResultsView(generic.DetailView):
    model = Project
    template_name = "grading/results.html"

def vote(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    try:
        stars = int(request.POST['stars'])
        if stars < 1 or stars > 5:
            raise ValueError
    except (KeyError, ValueError):
        return render(request, 'grading/detail.html', {
            'project': project,
            'error_message': '별점을 1에서 5 사이에서 선택해 주세요.',
        })
    else:
        Rating.objects.create(project=project, stars=stars)
        return HttpResponseRedirect(reverse('grading:results', args=(project.id,)))
	# project = get_object_or_404(Project, pk=project_id)
	# try:
	# 	selected_choice = project.choice_set.get(pk=request.POST["choice"])
	# except (KeyError, Choice.DoesNotExist):
	# 	return render(
	# 		request,
	# 		"grading/detail.html",
	# 		{
	# 			"project": project,
	# 			"error_message": "평가하지 않았습니다.",
	# 		},
	# 	)
	# else:
	# 	selected_choice.counts = F("counts") + 1
	# 	selected_choice.save()
	# 	return HttpResponseRedirect(reverse("grading:results", args=(project.id,)))
	

