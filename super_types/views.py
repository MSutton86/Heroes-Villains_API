
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypesSerializer
from .models import SuperType
# Create your views here.
@api_view(['GET', 'POST'])
def supertype_list(request):

    if request.method == 'GET':
        super_type = request.query_params.get('type')
        print(super_type)
        supertypes = SuperType.objects.all()

            
        if super_type:
            supertypes = supertypes.filter(super_type__type=super_type)
            
        serializer = SuperTypesSerializer(supertypes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = SuperTypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supertype_detail(request, pk):
    supertype = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(supertype);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(supertype, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        