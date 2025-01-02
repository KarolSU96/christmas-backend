from rest_framework import generics,permissions, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift
from .serializers import GiftSerializer
from christmas_backend.permissions import IsOwnerOrReadOnly

class GiftList(generics.ListCreateAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Gift.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class GiftDetail(APIView):
    serializer_class = GiftSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            gift = Gift.objects.get(pk=pk)
            self.check_object_permissions(self.request, gift)
            return gift
        except Gift.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        gift = self.get_object(pk)
        serializer = GiftSerializer(gift,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        gift = self.get_object(pk)
        serializer = GiftSerializer(gift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        gift = self.get_object(pk)
        gift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
