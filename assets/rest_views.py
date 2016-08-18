#!/usr/bin/env python
# Name: rest_views.py
# Time:8/17/16 11:08 PM
# Author:luo1fly

from rest_framework import viewsets
from assets import models
from assets import serializers
from rest_framework.decorators import (api_view, permission_classes)
from rest_framework import (status, permissions)
from rest_framework.response import Response
# import custom modules above


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        以下两个属性给定接口数据源和序列化类
    """
    queryset = models.UserProfile.objects.all().order_by('-date_joined')
    # 数据库查询结果集
    serializer_class = serializers.UserSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all()
    serializer_class = serializers.ServerSerializer


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def asset_list(request):
    if request.method == 'GET':
        assets_list = models.Asset.objects.all()
        serializer = serializers.AssetSerializer(assets_list, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
