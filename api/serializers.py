from rest_framework import serializers
from botapp.models import BotUsers, Category, Word, UserWord, UserCategory, WordOption


class BotUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone_number', 'username', 'created', 'updated']


class CategorySerializer(serializers.ModelSerializer):
    owner = BotUsersSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(queryset=BotUsers.objects.all(), write_only=True, source='owner')

    class Meta:
        model = Category
        fields = ['id', 'owner', 'owner_id', 'title', 'description', 'is_public', 'created', 'updated']


class UserCategorySerializer(serializers.ModelSerializer):
    user = BotUsersSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=BotUsers.objects.all(), write_only=True, source='user')
    category = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, write_only=True, source='category')

    class Meta:
        model = UserCategory
        fields = ['id', 'user', 'user_id', 'category', 'category_ids', 'is_favorite', 'is_learned', 'created', 'updated']


class WordOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOption
        fields = ['id', 'option', 'is_correct', 'created', 'updated']


class WordSerializer(serializers.ModelSerializer):
    author = BotUsersSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=BotUsers.objects.all(), write_only=True, source='author')
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, source='category')
    options = WordOptionSerializer(many=True, source='wordoption_set', read_only=True)
    options_input = WordOptionSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Word
        fields = [
            'id', 'author', 'author_id', 'category', 'category_id', 
            'word', 'meaning', 'description', 'created', 'updated', 
            'options', 'options_input'
        ]

    def create(self, validated_data):
        options_data = validated_data.pop('options_input', [])
        word = Word.objects.create(**validated_data)
        for option_data in options_data:
            WordOption.objects.create(word=word, **option_data)
        return word

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options_input', None)
        if options_data:
            # Clear existing options and create new ones
            instance.wordoption_set.all().delete()
            for option_data in options_data:
                WordOption.objects.create(word=instance, **option_data)
        return super().update(instance, validated_data)


class UserWordSerializer(serializers.ModelSerializer):
    user = BotUsersSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=BotUsers.objects.all(), write_only=True, source='user')
    word = WordSerializer(read_only=True)
    word_id = serializers.PrimaryKeyRelatedField(queryset=Word.objects.all(), write_only=True, source='word')

    class Meta:
        model = UserWord
        fields = ['id', 'user', 'user_id', 'word', 'word_id', 'is_favorite', 'is_learned', 'created', 'updated']
