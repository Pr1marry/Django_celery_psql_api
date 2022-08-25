from rest_framework import serializers
from .models import Client, Message, Mailing


# class ClientSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=10)
#     operator = serializers.CharField(max_length=5)
#     tag = serializers.CharField(max_length=100)
#     time_zone = serializers.CharField()
#
#     class Meta:
#         model = Client
#
#     def create(self, validated_data):
#         return Client(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.operator = validated_data.get('operator', instance.operator)
#         instance.tag = validated_data.get('tag', instance.tag)
#         instance.TimeZone = validated_data.get('TimeZone', instance.TimeZone)
#         instance.save()
#         return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'