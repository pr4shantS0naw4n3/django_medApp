from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('firstName','lastName','emailId','password','dateOfBirth','city','state','country','adminRoleType','isActive')
        extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self, validated_data):
        return User.objects.create(**validated_data)
