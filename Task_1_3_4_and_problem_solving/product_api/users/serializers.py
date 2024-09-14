from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken 

User = get_user_model() 


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password','confirm_password','role']


    def save(self):
        username = self.validate_data['username']
        first_name = self.validate_data['first_name']
        last_name = self.validate_data['last_name']
        email = self.validate_data['email']
        password = self.validate_data['password']
        confirm_password = self.validate_data['confirm_password']
        role = self.validate_data['role']
       
        #email and password validation
        if password != confirm_password:
            raise serializers.ValidationError({"Error": "Password Doesn't match."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Error": "Email Already Registered."})
        
        account = User(username=username, first_name=first_name, last_name=last_name, email=email, role=role)
        account.set_password(password)
        account.save()
        print(account)
        return account

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'password']

    #checking user authentication
    def validate(self, data):
        user = authenticate(username = data['username'], password = data['password'])
        
        if user is None:
            raise serializers.ValidationError({"Error": "Invalid Credential"})
        return data

    #Generating a JWT
    def create(self, validated_data):
        user = authenticate(username = validated_data['username'], password = validated_data['password'])
        
        if user:
            refresh = RefreshToken.for_user(user)
            return {
                'access_token': str(refresh.access_token),
                'refresh' : str(refresh)
            }

        return {}