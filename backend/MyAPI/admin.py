from django.contrib import admin
from .models import homepage,ImageModel,ConversationModel,ProductModel

@admin.register(homepage)
class homepageAdmin(admin.ModelAdmin):pass

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):pass

@admin.register(ConversationModel)
class ConversationModelAdmin(admin.ModelAdmin):pass

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):pass