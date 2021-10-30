from django.urls import path
from playground.api import viewset

app_name ='playground'
#URL CONFIGURATION
urlpatterns = [
    path('', viewset.upload_file_view,name='upload-view')
]



