
from django.urls import path,include
from .models import  homepage,ImageModel,ConversationModel,ProductModel
from . import views
from django.views.decorators.csrf import csrf_exempt 
from rest_framework import routers
app_name="MyAPI"
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)
router.register('Image', views.ImageModelView)

router.register('Conversation', views.ConversationView)
router.register('Product', views.ProductView)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

#	path('form/', views.AboutView.as_view(), name='cxform'),
    path('api/', include(router.urls)),
]

urlpatterns += static("/media/",
                              document_root=settings.MEDIA_ROOT)