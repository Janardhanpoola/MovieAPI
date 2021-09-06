from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

from .models import Movie

from .serializers import MovieSerializer

from asgiref.sync import sync_to_async
import asyncio

class MovieAPIView(APIView):
    
    def get(self,request,*args,**kwargs):
        movies=(Movie.objects.all())
        serializer=MovieSerializer(movies,many=True)
        #print(type(request.data))
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)

    # @sync_to_async
    # def post(self,request,*args,**kwargs):
    #     task = asyncio.create_task(MovieAPIDetail.put(self,request,id=None))
    #     await task

    #     serializer=MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=201)
    #     else:
    #         return Response(serializer.errors,status=400)


class MovieAPIDetail(APIView):
    

    def get(self,request,id=None):
        try:
            movie=Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            msg={'msg':"Requested movie doesnt exists"}
            return Response(msg,status=404)
        
        serializer=MovieSerializer(movie)
        return Response(serializer.data,status=200)


    
    def put(self,request,id=None):
        # task = asyncio.create_task(MovieAPIView.post(self,request,id=None))
        # await task

        movie=Movie.objects.get(id=id)

        serializer=MovieSerializer(movie,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)

    def patch(self,request,id=None):
        movie=Movie.objects.get(id=id)

        serializer=MovieSerializer(movie,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)
        

    def delete(self,request,id=None):
        movie=Movie.objects.get(id=id)
        movie.delete()
        msg={"msg":"resource deleted successfully"}
        return Response(msg,status=204)
        





