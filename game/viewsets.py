from rest_framework import viewsets, filters
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


