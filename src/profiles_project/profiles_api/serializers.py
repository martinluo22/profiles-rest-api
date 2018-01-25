from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #Make password field to be write only
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
        )

        user.set_password(validated_data['password'])

        user.save()

        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializer for profile feed items"""

    class Meta:

        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
