from django.http import HttpResponse
from django.template import loader
from .forms import ActivityForm
from .models import Activity
from django.shortcuts import render, redirect



def index(request):
    latest_activity_list = Activity.objects.order_by('-activity_date')[:3]
    template = loader.get_template('submit_activities/index.html')
    context = {
        'latest_activity_list': latest_activity_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, activity_id):
    return HttpResponse("You're looking at question %s." % activity_id)


def search_activities(request, activity_id):
    response = "You will see the activities here"
    return HttpResponse(response)

def dashboard_activity(request, activity_id):
    response = "You will see the dashboard here"
    return HttpResponse(response)

def submit_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ActivityForm()
    return render(request, 'submit_activities/submit_activity.html', {'form': form})



# Leave the rest of the views (detail, results, vote) unchanged