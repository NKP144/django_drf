from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import WomenSerializer

from rest_framework.views import APIView


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIView(APIView):
    # def get(self, request):              # Обрабатывает GET-запросы
    #     lst = Women.objects.all().values()
    #     return Response({'posts': list(lst)})

    def get(self, request):              # Обрабатывает GET-запросы
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)     #   Передаём данные сериализатору
        serializer.is_valid(raise_exception=True)           #   Проверка на валидность данных, если не валидные,
                                                            #   сгенерировать исключение
        # post_new = Women.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )

        serializer.save()   #   Вызывает метод create сериализатора

        # return Response({'post': WomenSerializer(post_new).data})
        return Response({'post': serializer.data})  #   Используются данные, которые возвращает метод create

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance)      #   При создании сериализатора с параметрами:
        serializer.is_valid(raise_exception=True)               # data и instance
        serializer.save()                                       # при высове метода save в сериализаторе выполняется метод update
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        instance.delete()
        return Response({"post": "delete post " + str(pk)})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
