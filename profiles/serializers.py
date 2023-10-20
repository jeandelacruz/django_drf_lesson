from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'author']
        # Con esta opción obtenemos los objetos relaciones segun el nivel
        # de profundidad
        # depth = 1

    def get_author(self, obj):
        from authors.serializers import AuthorDeepSerializer
        return AuthorDeepSerializer(obj.author).data

    # 1º Forma de mostrar datos relacionados
    # def to_representation(self, instance):
    #     return {
    #         'id': instance.id,
    #         'bio': instance.bio,
    #         'author': {
    #             'id': instance.author.id,
    #             'name': instance.author.name
    #         }
    #     }
