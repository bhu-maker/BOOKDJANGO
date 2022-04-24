from dataclasses import fields
from .models import bookmodel
from dataclasses import fields
from rest_framework.serializers import ModelSerializer
class bookser(ModelSerializer):
    class Meta:
        model=bookmodel
        fields=('id','title','author','price','pages')
