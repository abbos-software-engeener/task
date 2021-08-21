from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    credits = models.CharField(max_length=500)

    def str(self):
        return self.credits


class PositionCategory(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=500)

    def str(self):
        return self.model


class Credit(models.Model):

    CHOICE = (
        (1, _('Credit')),
        (2, _('Leasing')),
    )
    # credits = models.ForeignKey('Credit',on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    car = models.ForeignKey('Car',on_delete=models.CASCADE, related_name='cridets')
    model = models.ManyToManyField('PositionCategory', related_name='cridets')
    month = models.IntegerField(default=12)
    status = models.IntegerField(choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.month)
    @property
    def model_title(self):
        return self.title


class Payment(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments')
    order = models.IntegerField(default=1)
    sum = models.FloatField(default=0)
    percent = models.FloatField(default=12)
    total = models.FloatField(default=0)
    remain = models.FloatField(default=0)

    def str(self):
        return str(self.order)