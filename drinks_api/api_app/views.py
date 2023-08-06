from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status 

@api_view(['GET','POST'])
def drink_list(request, format=None):

    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        # return JsonResponse({"drinks" : serializer.data})
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])       
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.filter(id=id).get()
    except Drink.DoesNotExist:
        return Response({"error":"A valid integer is required - Out of range"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        drink.delete()
        return Response({"success":"Delete operation is successful."},status=status.HTTP_200_OK)
