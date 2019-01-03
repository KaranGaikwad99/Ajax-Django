from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Shotinfo(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    
    shot_type = models.CharField(max_length=255, blank=True, null=True)
    shot_status = models.CharField(max_length=255, blank=True, null=True)
    shot_record = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.shot_type

    class Meta:
        verbose_name_plural = 'ShotInfo'