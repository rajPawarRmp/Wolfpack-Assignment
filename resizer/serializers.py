from rest_framework import serializers
from .models import MyImage

class ImgSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyImage
		fields=['mainImg','imgName']