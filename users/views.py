from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializers,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework import status

# Create your views here.

# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User

# class SignUpAPIView(APIView):
#     permission_classes = [AllowAny]  
#     def post(self, request, *args, **kwargs):
#         serializer = CustomUserSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response({"status": True, "message": "User created successfully"}, status=status.HTTP_201_CREATED)
#         return Response({"status": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CustomUserSerializers
    queryset = CustomUser.objects.all()


class LoginAPIView(APIView):
    """
    API view for user login.
    Accepts username and password, returns an authentication token if successful.
    """

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        # Validate input
        if not serializer.is_valid():
            return Response(
                {"status": False,
                  "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        # Authenticate user
        user_obj = authenticate(request, username=username, password=password)

        if user_obj is not None:
            # Get or create token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user_obj)

            return Response(
                {
                    "status": True,
                    "data": {"token": str(token)},
                    "message": "Login successful"
                },
                status=status.HTTP_200_OK
            )

        # Invalid credentials
        return Response(
            {
                "message": "Invalid credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
  
def login(request, *args , **kwargs):
    return render(request , 'login.html')

