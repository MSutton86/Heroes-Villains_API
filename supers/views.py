from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers

@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':
        supers_types = request.query_params.get('supers_types')
        print(supers_types)
        supers = Supers.objects.all()
        
        queryset = Supers.objects.all()
            
        if supers_types:
            queryset = queryset.filter(supers__types=supers_types)
            
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        