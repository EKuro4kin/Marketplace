from typing import List

from rest_framework import serializers

from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, read_only=True)
    author_last_name = serializers.CharField(max_length=50, read_only=True)
    author_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "author_id",
            "author_image"
        ]

    def get_fields(self):
        data = getattr(self, "instance", None)

        if isinstance(data, List):
            for obj in data:
                author = getattr(obj, "author", None)

                obj.author_first_name = author.first_name
                obj.author_last_name = author.last_name
                obj.author_image = author.image
        elif data:
            author = getattr(data, "author", None)

            self.instance.author_first_name = author.first_name
            self.instance.author_last_name = author.last_name
            self.instance.author_image = author.image


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    author_id = serializers.SerializerMethodField()

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_author_id(self, obj):
        return obj.author.id

    class Meta:
        model = Ad
        fields = '__all__'

# написать сериализатор с логикой отображающий мои объявления (.../api/ads/me)
