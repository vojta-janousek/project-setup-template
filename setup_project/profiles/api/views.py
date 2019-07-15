from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import (ProfileSerializer,
                                      ProfileStatusSerializer,
                                      ProfileAvatarSerializer)
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


class ProfileStatusViewSet(viewsets.ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

# class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]
