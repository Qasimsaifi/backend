from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.conf import settings

from .models import User
from .serializers import UserSerializer

User = get_user_model()


class UserDetailView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            data = {
                'id': user.id,
                'email': user.email,
                'mobile': user.mobile,
                'username': user.username,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,
                'name': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'full_name': user.first_name + " " + user.last_name
                }
            }
            return Response(data)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)


class PublicUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']  # Add any other fields you want to filter on


class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Generate a password reset token
        token_generator = default_token_generator
        uid = urlsafe_base64_encode(user.pk.to_bytes())
        token = token_generator.make_token(user)

        # Build the password reset URL
        frontendUrl = 'http://localhost:5173'  # Replace with your frontend URL
        reset_password_url = f'{frontendUrl}/reset-password/{uid}/{token}'

        # Send a plain text email with the password reset link
        email_subject = 'Reset Password'
        email_message = f"Hello,\n\nYou have requested to reset your password. Please click on the link below:\n\n{reset_password_url}"
        send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [email])

        return Response({'message': 'Reset password link sent to your email.'}, status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    def post(self, request, uidb64, token):
        try:
            # Decode the UID and get the user
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise Http404

        # Check if the token is valid
        token_generator = default_token_generator
        if not token_generator.check_token(user, token):
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed to reset the password
        new_password = request.data.get('new_password')
        if new_password is None:
            return Response({'error': 'New password is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
