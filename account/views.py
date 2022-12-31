from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import RegistrationSerializer , LoginSerializer
from django.contrib.auth import authenticate



from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationView(APIView):
	def post(self,request):
		serializer=RegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			user=serializer.save()
			token = get_tokens_for_user(user)
			return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	
			


class LoginView(APIView):
  
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':'Email or Password is not Valid'}, status=status.HTTP_404_NOT_FOUND)			