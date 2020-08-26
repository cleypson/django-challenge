from rest_framework import serializers
from .models import User, Never, Project
from apps.api import utils
from .utils import get_user_request


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User(
            email=self.validated_data['email']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class NeverSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    class Meta:
        model = Never
        fields = '__all__'
    
    def create(self, validated_data):
        never = super(NeverSerializer, self).create(validated_data)
        never.user = get_user_request(self.context['request'])
        never.save()
        return never

    def get_projects(self, instance):
        projects_json = []
        for project in instance.project_set.all():
            projects_json.append({
                'id': project.id,
                'name': project.name
            })
        return projects_json


class ProjectSerializer(serializers.ModelSerializer):
    nevers_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'nevers', 'nevers_list']

    def create(self, validated_data):
        project = super(ProjectSerializer, self).create(validated_data)
        project.user = get_user_request(self.context['request'])
        project.save()
        return project

    def get_nevers_list(self, instance):
        nevers_json = []
        for never in instance.nevers.all():
            nevers_json.append({
                'id': never.id,
                'name': never.name,
                'birthdate': never.birthdate,
                'admission_date': never.admission_date,
                'job_role': never.job_role
            })
        return nevers_json
