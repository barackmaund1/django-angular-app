from rest_framework import serializers
from tutorial import models

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'title',
            'description',
            'author',
            'image', 
            'published',
            'created_at',
            'updated_at'

        )
        model=models.Tutorial
      