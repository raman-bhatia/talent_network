from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['project_title', 'project_details', 'start_date', 'end_date', 'team_members']
