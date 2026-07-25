from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import (
    User,
)
from .serializer import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
    LogoutSerializer,
)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        seriailzer = ProfileSerializer(request.user)
        return Response({
            "status": True,
            "message": "Profile Fetch Successfully",
            "data": seriailzer.data
        },
            status=status.HTTP_200_OK
            )

    def put(self, request):
        serializer = ProfileSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Update Successfully",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
        )
    
    def patch(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Update Successfully",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
        )

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "You Register Successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_401_UNAUTHORIZED
        )

class LoginViewSet(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(
                request,
                email=email,
                password=password
            )
        if user is None:
            return Response(
                {
                    "message": "Invalid email or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {
                    "message": "User account is inactive."
                },
                status=status.HTTP_403_FORBIDDEN
            )
        refresh = RefreshToken.for_user(user)

        user_data = UserSerializer(user)

        return Response(
            {
                "message": "Login successful.",
                "data": user_data.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = LogoutSerializer(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            refresh = serializer.validated_data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(
                {"message": "You logged out successfully."},
                status=status.HTTP_200_OK
            )

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            user = request.user
            old_password = serializer.validated_data["old_password"]      
            new_password = serializer.validated_data["new_password"]

            if not user.check_password(old_password):
                return Response({
                    "message": "Your Old Password Doesn't Exist"
                },
                status=status.HTTP_400_BAD_REQUEST)
            if old_password == new_password:
                return Response({
                    "message": "Your Password Same as Old Password"
                },
                status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(new_password)
            user.save()
            return Response({
                "message": "Password changed successfully. Please log in again."
            },
            status=status.HTTP_200_OK)

