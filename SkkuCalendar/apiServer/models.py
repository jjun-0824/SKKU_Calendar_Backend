from django.db import models

class Schedule(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    nickname = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    place = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=225, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    alarm = models.IntegerField(blank=True, null=True)
    alarm_time = models.DateTimeField(blank=True, null=True)
    color = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'post_schedule'