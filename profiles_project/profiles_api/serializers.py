from rest_framework.serializers import ModelSerializer
from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type': 'password'},
            },
            'id':{
                'read_only':True,
            }
        }