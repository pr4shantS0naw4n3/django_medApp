from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserApiView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response({"users":serializer.data})

    def post(self,request):
        user=request.data
        # User Register
        if(user['requestType'] == 'userRegister'):
            serializer=UserSerializer(data=user,many=False)
            if(serializer.is_valid(raise_exception=True)):
                user_saved=serializer.save()
            return Response({
                'responseMessage':'User Created Successfully',
                'user_Details':{
                    'id':user_saved.id,
                    'Name':user_saved.firstName+' '+user_saved.lastName,
                    'emailId':user_saved.emailId,
                    'adminRoleType':user_saved.adminRoleType
                }
            },status=status.HTTP_201_CREATED)
        # User Login
        elif(user['requestType'] == 'userLogin'):
            try:
                get_user=User.objects.get(emailId=user['emailId'],password=user['password'])
                serializer=UserSerializer(get_user,many=False)
                return Response({"responseMessgae":"User Login Successful","userData":serializer.data},status=status.HTTP_200_OK)
            except:
                return Response({"responseMessgae": "User Not Found"},status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"responseMessgae": "Invalid Request Type"},status=status.HTTP_400_BAD_REQUEST)