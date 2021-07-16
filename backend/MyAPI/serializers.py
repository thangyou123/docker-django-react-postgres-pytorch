from rest_framework import serializers
from . models import homepage,ImageModel,ConversationModel,ProductModel

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=homepage
		fields='__all__'

class ImageModelSerializers(serializers.ModelSerializer):
	class Meta:
		model=ImageModel
		fields='__all__'

class ConversationModelSerializers(serializers.ModelSerializer):
	class Meta:
		model=ConversationModel
		fields='__all__'

class ProductModelSerializers(serializers.ModelSerializer):
	class Meta:
		model=ProductModel
		fields='__all__'
		