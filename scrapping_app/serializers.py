from rest_framework import serializers
from .models import Data

class DataInfo(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ["price"]
