from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Card
from .serializers import CardSerializer

@csrf_exempt
def userApi(request,Id=0):
    if request.method=='GET':
        card= Card.objects.all()
        card_serializer= CardSerializer(card,many=True)
        return JsonResponse(card_serializer.data,safe=False)
    elif request.method=='POST':
        card_data= JSONParser().parse(request)
        card_serializer= CardSerializer(data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        card_data= JSONParser().parse(request)
        card= Card.objects.get(videoId=card_data['videoId'])
        card_serializer=CardSerializer(card,data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        card=Card.objects.get(videoId=id)
        card.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    # elif request.method=='DELETE':
    #     card=Card.objects.get(videoId=id)
    #     card.delete()
    #     return JsonResponse("Deleted Successfully",safe=False)

# # Create your views here.


