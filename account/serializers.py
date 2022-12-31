from rest_framework import serializers
from account.models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
	class Meta:
		model=MyUser
		fields=['email','name','password','password2','city']
		extra_kwargs={
		'password':{'write_only':True}
			}
		  # Validating Password and Confirm Password while Registration
	def validate(self, attrs):
		password = attrs.get('password')
		password2 = attrs.get('password2')
		if password != password2:
			raise serializers.ValidationError("Password and Confirm Password doesn't match")
		return attrs

	def create(self, validate_data):
		return MyUser.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=200)
	class Meta:
		model=MyUser
		fields=['email','password']		