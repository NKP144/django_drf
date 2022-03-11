import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)     #   Только для чтения, чтобы сериализатор не генерировал
#     time_update = serializers.DateTimeField(read_only=True)     #   ошибку в ответе на post запрос без времени создания
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)       #  Автоматически вызывается при serializer.save()
#
#     def update(self, instance, validated_data):
#         """ instanse - ссылка на объект модели, в котором необходимо заменить данные
#             validated_data - словарь из проверенных данных, которые необходимо применить """
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


class WomenSerializer(serializers.ModelSerializer):
    """ Сериализатор для работы с моделью """
    class Meta:
        model = Women
        # fields = ("title", "content", "cat")    #   Поля которые будут возвращаться по запросу API
        fields = "__all__"    #   Поля которые будут возвращаться по запросу API


