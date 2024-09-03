from rest_framework import serializers
from .models import Timeu


class TimeuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeu
        fields = "__all__"
