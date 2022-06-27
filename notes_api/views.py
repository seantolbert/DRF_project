from rest_framework import generics
from notes.models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.noteobjects.all()
    serializer_class = NoteSerializer



class NoteDetail(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

