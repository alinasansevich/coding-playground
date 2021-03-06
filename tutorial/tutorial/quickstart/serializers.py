#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:43:21 2021

@author: alina
"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']