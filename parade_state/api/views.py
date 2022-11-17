from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from parade_state.models import ParadeState
from .serializers import ParadeStateSerializer
from rest_framework import permissions


# Create your views here.
class ParadeStateListView(ListCreateAPIView):
    serializer_class = ParadeStateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return ParadeState.objects.filter(author=self.request.user)    



class ParadeStateDetailView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ParadeStateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return ParadeState.objects.filter(author=self.request.user)
    


