from rest_framework import serializers
from .models import Project
from navers.models import Naver


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
        ]


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'navers',
        ]
        extra_kwargs = {'navers': {'required': True}}


class ProjectDetailSerializer(serializers.ModelSerializer):
    navers = serializers.SerializerMethodField()

    def get_navers(self, obj):
        from navers.serializers import NaverSerializer
        return NaverSerializer(Naver.objects.filter(projects=obj), many=True, read_only=True).data

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'navers',
        ]
        extra_kwargs = {'navers': {'required': False}}
