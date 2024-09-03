from django.http import HttpResponse
from .models import Timeu
from .serializer import TimeuSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def data(request: Request):
    if request.method == 'GET':
        main_data = Timeu.objects.order_by('id').all()
        data_serializer = TimeuSerializer(main_data, many=True)
        return Response(data_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TimeuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def data_list(request: Request, data_id: int):
    try:
        data = Timeu.objects.get(pk=data_id)
    except Timeu.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TimeuSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TimeuSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


def home(request):
    instance = Timeu.objects.get(title='Typing')
    duration = instance.get_duration()
    return HttpResponse(f'Welcom {duration}')
