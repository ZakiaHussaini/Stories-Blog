from rest_framework import serializers
from .models import Story, Category
from likes.models import Like


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ReadOnlyField(source='category.name')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
            
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value
    
    
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner = user, story = obj
            ).first()
            like = Like.id if like else None
        return None
    
    class Meta:
        model = Story
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'content','image',
            'category', 'like_id', 'like_count','comment_count'
        ]
        
