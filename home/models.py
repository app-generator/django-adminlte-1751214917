# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    istenant = models.CharField(max_length=255, null=True, blank=True)
    tenantfirstname = models.CharField(max_length=255, null=True, blank=True)
    tenantmidname = models.CharField(max_length=255, null=True, blank=True)
    tenantlastname = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Property(models.Model):

    #__Property_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    propertytype = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    num_units = models.CharField(max_length=255, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    #__Property_FIELDS__END

    class Meta:
        verbose_name        = _("Property")
        verbose_name_plural = _("Property")


class Propertytype(models.Model):

    #__Propertytype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    numunits = models.CharField(max_length=255, null=True, blank=True)
    isresidential = models.BooleanField()
    iscommercial = models.BooleanField()
    numresidentialunits = models.IntegerField(null=True, blank=True)
    numcommercialunits = models.IntegerField(null=True, blank=True)
    island = models.BooleanField()
    numacreland = models.IntegerField(null=True, blank=True)

    #__Propertytype_FIELDS__END

    class Meta:
        verbose_name        = _("Propertytype")
        verbose_name_plural = _("Propertytype")


class Owner(models.Model):

    #__Owner_FIELDS__
    ownername = models.CharField(max_length=255, null=True, blank=True)
    contactfirstname = models.CharField(max_length=255, null=True, blank=True)
    contactmidname = models.CharField(max_length=255, null=True, blank=True)
    contactlasrtname = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    cellphone = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    #__Owner_FIELDS__END

    class Meta:
        verbose_name        = _("Owner")
        verbose_name_plural = _("Owner")



#__MODELS__END
