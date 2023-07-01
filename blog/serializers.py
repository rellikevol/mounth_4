from rest_framework import serializers
from blog.models import Post, Comment
from users.models import GeekUser


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = ['id', 'email', 'is_staff', 'is_active', 'date_joined']

class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["username", "text", "created"]


class PostDetailSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created', 'status', 'cover', 'post_comment']