from accounts.models import CoreUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer

class UserSignUpView(CreateAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(data=request.data)
        else:
            return Response(serializer.errors,status=500)       
        
        user = CoreUser.objects.get(email=request.data.get("email"))
        serializer = UserSerializer(user)
        return Response(serializer.data,status=201)
        

class UserSignInView(RetrieveAPIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = CoreUser.objects.get(email=email)
        except CoreUser.DoesNotExist:
            return Response({"message":"user does not exist"}, status=404)

        is_authenticated = authenticate(email=email, password=password)
                
        if not is_authenticated:
            return Response({"message":"invalid credentials"}, status=406)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=200)




