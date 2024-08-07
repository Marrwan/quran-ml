from rest_framework import serializers

class RecitationSerializer(serializers.Serializer):
    audio = serializers.FileField()
