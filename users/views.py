from rest_framework import generics, views, status
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "User created successfully"
        })

class UserLoginView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        
        if user is not None:
            try:
                employee = CustomUser.objects.get(username=user.username)
                refresh = RefreshToken.for_user(user)
                return Response({
                    "username": username,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "message":"User login successfully",
                    "role":employee.role,
                    "user_id": employee.id
                })
            except CustomUser.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response({
                "message": "Invalid credentials",
            }, status=status.HTTP_401_UNAUTHORIZED)

class TokenRefreshView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            return Response({"message": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({"access": access_token})
        except Exception as e:
            return Response({"message": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)