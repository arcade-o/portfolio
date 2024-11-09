from rest_framework import serializers
from .models import profile,project

class project_serializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields = ("name","github","username","hidden")

    def update(self,instance,validated_data):
        instance.name = validated_data('name',instance.username)
        instance.github = validated_data('github',instance.github)
        instance.username = validated_data('username',instance.github)

        
class profile_serializer(serializers.ModelSerializer):

    class Meta:
        model= profile
        fields = ("username","email","password", "github","id","projects")
        extra_kwargs = {"password": {"write_only":True },
                        'projects' : {'read_only':True},
                        }

    def create(self,validated_data):
        user= profile.objects.create_user(**validated_data)
        return user
    
    def update(self,instance,validated_data):
        instance.username = validated_data('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.github = validated_data.get('github',instance.email )