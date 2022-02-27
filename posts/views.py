from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
        Posts' serialization.

        This is a description.
    """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        Users' serialization.

        This is a description.
    
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


