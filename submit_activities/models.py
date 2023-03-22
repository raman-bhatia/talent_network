from django.db import models


class Activity(models.Model):
    activity_objective = models.CharField(max_length=2000)
    activity_date = models.DateTimeField('date published')
    activity_owner = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.activity_owner


class HomeFunction(models.Model):
    question = models.ForeignKey(Activity, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_prioritized = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text