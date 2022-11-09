from typing import List

from rest_framework import serializers

from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(max_length=50, read_only=True, source='author.first_name')
    author_last_name = serializers.CharField(max_length=50, read_only=True, source='author.last_name')
    author_image = serializers.ImageField(read_only=True, source='author.image')
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)


    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image"
        ]

class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(max_length=50, read_only=True, source='author.first_name')
    author_last_name = serializers.CharField(max_length=50, read_only=True, source='author.last_name')
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = [
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id",
        ]


# class AdDetailSerializer(serializers.ModelSerializer):
#     author_first_name = serializers.SerializerMethodField()
#     author_last_name = serializers.SerializerMethodField()
#     author_id = serializers.SerializerMethodField()
#     # phone = serializers.SerializerMethodField()
#
#     def get_author_first_name(self, obj):
#         return obj.author.first_name
#
#     def get_author_last_name(self, obj):
#         return obj.author.last_name
#
#     def get_author_id(self, obj):
#         return obj.author.id
#
#     class Meta:
#         model = Ad
#         fields = [
#             'pk',
#             'image',
#             'title',
#             'price',
#             'description',
#             'author_first_name',
#             'author_last_name',
#             'author_id'
#         ]
#
# # написать сериалайзер с логикой отображающий мои объявления (.../api/ads/me)
