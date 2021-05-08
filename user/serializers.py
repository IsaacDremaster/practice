from django.contrib.auth import get_user_model

from rest_auth.models import TokenModel

from rest_framework import serializers

from .models import Profiles, Stuff


class ProfileRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    birthday = serializers.DateField()
    phone = serializers.CharField()
    balance = serializers.IntegerField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Profiles.objects.create(
            user=user,
            name=validated_data.get('name'),
            last_name=validated_data.get('last_name'),
            birthday=validated_data.get('birthday'),
            phone=validated_data.get('phone'),
            balance=validated_data.get('balance'),
        )
        return profile

class StuffRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Profiles.objects.create(
            user=user,
            name=validated_data.get('name'),
            last_name=validated_data.get('last_name'),
        )
        return profile


class ProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class StuffLoginSerializer(ProfileLoginSerializer):
    pass
