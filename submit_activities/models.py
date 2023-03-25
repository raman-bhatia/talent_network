from django.db import models


class Activity(models.Model):
    project_title = models.CharField(max_length=200)
    project_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.TextField()
    
    def __str__(self):
        return self.activity_owner


class HomeFunction(models.Model):
    question = models.ForeignKey(Activity, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_prioritized = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text