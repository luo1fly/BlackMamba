#!/usr/bin/env python
# Name: serializers.py
# Time:8/17/16 11:17 PM
# Author:luo1fly

from rest_framework import serializers
from assets import models
# import custom modules above


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        把实例对象转换成前端能够展示的json格式
    """
    class Meta:
        """
            @:parameter model:
            @:parameter fields:
        """
        model = models.UserProfile
        depth = 2
        # fields = ('url', 'name', 'email', 'is_admin')


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Asset
        depth = 2
        fields = ('name', 'sn', 'server', 'networkdevice')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        # fields = ('asset',)
