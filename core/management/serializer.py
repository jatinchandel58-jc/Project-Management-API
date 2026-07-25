from rest_framework import serializers
from .models import (
    User,
)

import re
from rest_framework import serializers
from .models import User

# validation

def validate_strong_password(value):
    if not re.search(r"[A-Z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one uppercase letter."
        )

    if not re.search(r"[a-z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one lowercase letter."
        )

    if not re.search(r"\d", value):
        raise serializers.ValidationError(
            "Password must contain at least one digit."
        )

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise serializers.ValidationError(
            "Password must contain at least one special character."
        )

    return value

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        validators=[validate_strong_password]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "bio",
            "phone_number",
            "created_at",
            "updated_at",
            "is_active",
        ]

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "is_active",
        )
        extra_kwargs = {
        "first_name": {"required": True},
        "phone_number": {"required": True},
        "bio": {"required": False},
        "last_name": {"required": False},
    }

    def validate_email(self, value):
        """
        Check if email already exists.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def validate_first_name(self, value):
        """
        First name cannot be empty.
        """
        if not value.strip():
            raise serializers.ValidationError(
                "First name cannot be empty."
            )
        return value

    def validate_phone_number(self, value):
        """
        Phone number must contain exactly 10 digits.
        """
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
        validators=[validate_strong_password])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "bio",
            "phone_number",
            "created_at",
            "updated_at",
            "is_active",
        ]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "bio",
            "phone_number",
            "profile_picture",
            "created_at",
            "is_active",
        ]
        read_only_fields = [
        "email",
        "created_at",
        "is_active",
    ]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
