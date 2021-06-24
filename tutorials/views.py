

# Create your views here.
from rest_framework import generics
from .models import Tutorial
from .serializers import TutorialSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

class TutorialAPIView(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # ... tutorial = Tutorial.objects.get(pk=pk)
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 