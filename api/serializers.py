from botapp.models import BotUsers, UserCategory, Word, Category, WordOption
from rest_framework import serializers


class BotUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = BotUsersSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = '__all__'


class WordOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOption
        fields = '__all__'
    

class WordWithOptionSerializer(serializers.ModelSerializer):
    options = WordOptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Word
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    author = BotUsersSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Word
        fields = '__all__'