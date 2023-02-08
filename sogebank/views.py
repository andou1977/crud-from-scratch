from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from sogebank.models import Sogebank
from bank.serializer import sogebankserialiser
from django.http import JsonResponse
from bank.serializer import sogebankserialiser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return render(request,'index.html')

# list all
@api_view(['GET'])
def listersogebank(request):
    if request.method=='GET':
        query=Sogebank.objects.all()
        serializer=sogebankserialiser(query,many=True)
        return JsonResponse({'drinks':serializer.data})


# //add
@api_view(['POST'])
def sogebankadd(request):
        if request.method == 'POST':
            serializer = sogebankserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# lister by id
@api_view(['GET'])
def sogebanklistid(request, id):

    try:
        if request.method=='GET':
            query=Sogebank.objects.get(pk=id)
            serializer=sogebankserialiser(query)
            return Response(serializer.data)
    except Sogebank.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# //lister par nom
@api_view(['GET'])
def sogebanklistname(request, nom):

    try:
        if request.method=='GET':
            query=Sogebank.objects.get(nom=nom)
            serializer=sogebankserialiser(query)
            return Response(serializer.data)
    except Sogebank.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



# mise a jour
@api_view(['PUT'])
def updatesogebank(request, id):
    if request.method=='PUT':
        drink=Sogebank.objects.get(pk=id)
        serializer=sogebankserialiser(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


# //delete
@api_view(['DELETE'])
def deletesogebank(request, id):
    if request.method=='DELETE':
        drink=Sogebank.objects.get(pk=id)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
