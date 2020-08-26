from rest_framework import serializers
from .models import Naver
from projects.serializers import ProjectSerializer


class NaverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Naver
        fields = [
            'id',
            'name',
            'birthdate',
            'admission_date',
            'job_role',
        ]

class NaverCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Naver
        fields = [
            'id',
            'name',
            'birthdate',
            'admission_date',
            'job_role',
            'projects'
        ]
        extra_kwargs = {'projects': {'required': False}}


class NaverDetailSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Naver
        fields = [
            'id',
            'name',
            'birthdate',
            'admission_date',
            'job_role',
            'projects'
        ]
        extra_kwargs = {'projects': {'required': False}}
