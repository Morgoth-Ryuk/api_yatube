from rest_framework import serializers
from posts.models import Post, Group, Comment



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    publication_date = serializers.DateTimeField(source='pub_date', read_only=True)
    group = serializers.SlugRelatedField(slug_field='slug',
            queryset=Group.objects.all(), required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'publication_date', 'group')
        model = Post
        read_only_fields = ('author',)
