
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ImgSerializer
from PIL import Image





class ResizeView(APIView):
		def post(self, request):
				serializer = ImgSerializer(data=request.data)

				if serializer.is_valid(raise_exception=True):
						serializer.save()
						imgName = str(request.FILES["mainImg"])
						# print(request.FILES["mainImg"])
						# mainImg=os.path.join(settings.MEDIA_URL,"uploads", imgName)

						path = "media/uploads/"+imgName
						print(path)

						# print(resizedImg)
						# resizedImg.save("media/uploads/1.jpeg")
						serializer.is_valid(raise_exception=True)
						serializer.save()

						img = Image.open(path)
						thumbnail = img
						medium = img
						large = img
						thumbnail = thumbnail.resize((200, 300))
						thumbnail.save("media/uploads/1.jpeg")

						medium = medium.resize((500, 500))
						medium.save("media/uploads/2.jpeg")
						large = large.resize((1024, 768))
						large.save("media/uploads/3.jpeg")
						return Response({'data': serializer.data, "thumbnail": "/media/uploads/1.jpeg",
										"medium": "/media/uploads/2.jpeg",
										"large": "/media/uploads/3.jpeg", 'msg': 'Conversion  Successful'}, status=status.HTTP_201_CREATED)

				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
				