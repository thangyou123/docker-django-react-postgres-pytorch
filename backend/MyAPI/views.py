from django.shortcuts import render



from rest_framework import viewsets

from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import homepage,ImageModel,ConversationModel,ProductModel
from . serializers import approvalsSerializers,ImageModelSerializers,ConversationModelSerializers,ProductModelSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.http import HttpResponse
from underthesea import word_tokenize
import string
import regex as re
from rest_framework.permissions import AllowAny


class ApprovalsView(viewsets.ModelViewSet):
	queryset = homepage.objects.all()
	serializer_class = approvalsSerializers
	permission_classes = [AllowAny]

class ImageModelView(viewsets.ModelViewSet):
	queryset = ImageModel.objects.all()
	serializer_class = ImageModelSerializers
	permission_classes = [AllowAny]
class ConversationView(viewsets.ModelViewSet):
	queryset = ConversationModel.objects.all()
	serializer_class = ConversationModelSerializers
	permission_classes = [AllowAny]
class ProductView(viewsets.ModelViewSet):
	queryset = ProductModel.objects.all()
	serializer_class = ProductModelSerializers
	permission_classes = [AllowAny]
	