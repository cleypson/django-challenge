from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSignupSerializer, NeverSerializer, ProjectSerializer
from .models import User, Never, Project
from .permissions import IsOwnerOrReadOnly
from .utils import get_user_request
from django_filters.rest_framework import DjangoFilterBackend


class UserSignupViewSet(viewsets.ModelViewSet):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = get_user_request(self.request)
        queryset = User.objects.none()
        if user != None:
            queryset = User.objects.filter(id=user.id)
        return queryset

    def save(self, request):
        signup = UserSignupSerializer(data=request.data)
        status_code = status.HTTP_400_BAD_REQUEST
        if signup.is_valid():
            signup.save()
            status_code = status.HTTP_201_CREATED
        return Response(status=status_code)


class NeverViewSet(viewsets.ModelViewSet):
    queryset = Never.objects.all().order_by('name')
    serializer_class = NeverSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'admission_date']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']
