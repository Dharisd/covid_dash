from django.db import models

# Create your models here.
class ActiveCase(models.Model):
    number = models.IntegerField(
        blank=True,
        null=True
    )
    last_day = models.IntegerField(
        blank=True,
        null=True
    )


class SampleDetail(models.Model):
    name = models.CharField(max_length=255)
    positive_samples = models.IntegerField(
        blank=True,
        null=True
    )
    positive_samples_last_day = models.IntegerField(
        blank=True,
        null=True
    )  
    negative_samples = models.IntegerField(
        blank=True,
        null=True
    )
    negative_samples_last_day = models.IntegerField(
        blank=True,
        null=True
    )  
    waiting_samples = models.IntegerField(
        blank=True,
        null=True
    )
    total_samples = models.IntegerField(
        blank=True,
        null=True
    )
    total_samples_last_day = models.IntegerField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name}"



class QuarantineAddress(models.Model):
    name= models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


