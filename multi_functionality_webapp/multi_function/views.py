from multiprocessing import context
from pyclbr import Class
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .models import Quizzes,Question,Patients,Doctor1
from .serializers import UserRegisterationSerial, UserLoginSerial, UserProfileSerial, ChangePasswordSeial, SendPasswordResetMailSerial,UserPasswordResetSerial, ContactSerial,QuestionSerial,RandomQuestionSerial,QuizSerial,PatientAppointmentSerial,DoctorSerial,PatientSerialView
from rest_framework.generics import ListAPIView
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from.utils import Util


# Create your views here.
'''class UserList(ListAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializers'''
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserRegistration(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegisterationSerial(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ContactView(APIView):
    def post(self,request,format=None):
        serializer=ContactSerial(data=request.data)
        if serializer.is_valid(raise_exception=True):
            contact=serializer.save()
            return Response({'msg':"Contact Saved, Our Team contact you very shortly"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerial(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password = serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                body='Account Login Successfully, Team MFW'
                data={'subject':'Account Login successfully, Team MFW','body':body,'to_email':email}
                Util.sendEmail(data)
                return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'Non_field_errors' : ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerial(request.user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePassword(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=ChangePasswordSeial(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            
            return Response({'msg':'Change Password Success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetMail(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=SendPasswordResetMailSerial(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link is Sent Successful in your mail'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserPasswordReset(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer=UserPasswordResetSerial(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Quiz(ListAPIView):
        serializer_class=QuizSerial
        queryset=Quizzes.objects.all()
class RandomQuestion(APIView):
    def get(self,request,format=None,**kwargs):
        question=Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer=RandomQuestionSerial(question,many=True)
        return Response(serializer.data)
class QuizQuestion(APIView):
    def get(self,request,format=None,**kwargs):
        question=Question.objects.filter(quiz__title=kwargs['topic'])
        serializer=QuestionSerial(question,many=True)
        return Response(serializer.data)

class DoctorView(APIView):
    
    def get(self,request,format=None):
        datas=Doctor1.objects.all()
        serializer=DoctorSerial(datas,many=True)
        print (serializer)
        return Response(serializer.datas, status=status.HTTP_200_OK)

class PatientView(APIView):
    def get(self,request,format=None):
        data=Patients.objects.all()
        serializer=PatientSerialView(data,many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
class PatientAppointment(APIView):
    def post(self,request,format=None):
        serializer=PatientAppointmentSerial(data=request.data)
        if serializer.is_valid(raise_exception=True):
            contact=serializer.save()
            return Response({'msg':"Appointment Successfully, Please check your mail, if any query please contact us"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)