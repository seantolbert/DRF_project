from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, DjangoModelPermissions, IsAdminUser, BasePermission, DjangoModelPermissionsOrAnonReadOnly
from notes.models import Note
from .serializers import NoteSerializer


class NoteUserWritePermission(BasePermission):
    message = 'editing posts is retricted to authorized users only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class NoteList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Note.noteobjects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView, NoteUserWritePermission):
    permission_classes = [NoteUserWritePermission]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
