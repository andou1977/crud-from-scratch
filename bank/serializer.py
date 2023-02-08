from rest_framework import serializers

from sogebank.models import Sogebank

class sogebankserialiser(serializers.ModelSerializer):
    class Meta:
        model = Sogebank
        fields = '__all__'