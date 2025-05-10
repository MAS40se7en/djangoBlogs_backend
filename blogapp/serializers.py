from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Blog

class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        
        user = get_user_model()
        new_user = user.objects.create(
            email = email,
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        
        new_user.set_password(password)
        new_user.save()
        
        return new_user
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "bio", "profile_image", "facebook", "twitter", "instagram", "youtube", "github"]
        
class UserInfoSerializer(serializers.ModelSerializer):
    author_posts = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "job_title", "bio", "profile_image", "author_posts"]
    
    def get_author_posts(self, user):
        blogs = Blog.objects.filter(author=user)
        serializer = BlogSerializer(blogs, many=True)
        return serializer.data
    
class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "profile_image", "first_name", "last_name"]
    
class BlogSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["id", "title", "content", "author", "category", "published_at", "is_draft", "featured_image"]

class BlogListSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["id", "title", "author", "category", "published_at", "is_draft", "featured_image", "slug"]