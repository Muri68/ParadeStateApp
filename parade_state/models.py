from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
from django.utils import timezone



# Create your models here.
class ParadeState(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now, unique=True, max_length=15)

    posted_strength_officers = models.IntegerField()
    posted_strength_soldiers = models.IntegerField()

    # on_parade_officers = models.IntegerField()
    # on_parade_soldiers = models.IntegerField()

    # on_duty_officers = models.IntegerField()
    # on_duty_soldiers = models.IntegerField()

    # off_duty_officers = models.IntegerField()
    # off_duty_soldiers = models.IntegerField()

    # sick_report_officers = models.IntegerField()
    # sick_report_soldiers = models.IntegerField()

    # civil_institution_officers = models.IntegerField()
    # civil_institution_soldiers = models.IntegerField()

    # punishment_duty_officers = models.IntegerField()
    # punishment_duty_soldiers = models.IntegerField()

    # pass_officers = models.IntegerField()
    # pass_soldiers = models.IntegerField()

    # leave_officers = models.IntegerField()
    # leave_soldiers = models.IntegerField()

    # course_officers = models.IntegerField()
    # course_soldiers = models.IntegerField()

    # attached_officers = models.IntegerField()
    # attached_soldiers = models.IntegerField()

    # detached_officers = models.IntegerField()
    # detached_soldiers = models.IntegerField()

    # call_centre_officers = models.IntegerField()
    # call_centre_soldiers = models.IntegerField()

    # external_operations_officers = models.IntegerField()
    # external_operations_soldiers = models.IntegerField()

    # internal_operations_officers = models.IntegerField()
    # internal_operations_soldiers = models.IntegerField()

    # assignment_officers = models.IntegerField()
    # assignment_soldiers = models.IntegerField()

    # absent_officers = models.IntegerField()
    # absent_soldiers = models.IntegerField()

    # awol_officers = models.IntegerField()
    # awol_soldiers = models.IntegerField()

    # mess_officers = models.IntegerField()
    # guard_room_soldiers = models.IntegerField()

    # IHL_officers = models.IntegerField()
    # IHL_soldiers = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created_at',)

    #

    def __str__(self):
        return self.title

