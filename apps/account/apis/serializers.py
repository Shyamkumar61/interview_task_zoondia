import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.account.models import Account
from apps.urls_short.apis.serializers import urlVisitSerializer

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=10)



class AccountSerialzer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=8)
    confirm_password = serializers.CharField(required=True, max_length=8, write_only=True)


    def validate_first_name(self, attrs):
        if not attrs:
            raise serializers.ValidationError({"First Name Cannot be Empty. Please Enter you first name Please"})
        if attrs and not re.match(r'^[a-zA-Z/s]*$', attrs):
            raise serializers.ValidationError({"First Name Cannot Contain Numbers and Special Letters"})
        return attrs
    
    def validate_email(self, attrs):
        if not attrs:
            raise serializers.ValidationError({"Please Enter Your Email Address"})
        return attrs
    
    def validate_password(self, attrs):
        if attrs and len(attrs) ==  8 and not re.match(r'^[a-zA-Z_@]+$', attrs):
            raise serializers.ValidationError({"error":"password should have atleast 1 special character, 1 uppercase, 1 number, minlength 8", "special Charters": "_ and @ is allowed"})
        return attrs

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        email = attrs.get("email")
        if password != confirm_password:
            raise serializers.ValidationError({"Password Not Matching"})
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Email Already Exists"})
        return attrs

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        account = User.objects.create(first_name=validated_data['first_name'], last_name=
                                      validated_data['last_name'], username=validated_data['first_name'], email=validated_data['email'], 
                                      password=validated_data['password'])
        return account


class UserSerializer(serializers.ModelSerializer):

    url_vistitors = urlVisitSerializer(many=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'url_vistitors')