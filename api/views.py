from rest_framework import generics
from botapp.models import BotUsers, Word
from .serializers import BotUsersSerializer, WordSerializer, WordOptionSerializer

class BotUsersListCreateView(generics.ListCreateAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializer

    def perform_create(self, serializer):
        bot_user = BotUsers.objects.filter(user_id=self.request.data.get('user_id'))
        print(bot_user)
        if bot_user.exists():
            return bot_user
        serializer.save()

bot_users_view = BotUsersListCreateView.as_view()

class BotUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializer

bot_user_detail_view = BotUsersDetailView.as_view()


class WordListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # def perform_create(self, serializer):
    #     author = BotUsers.objects.get(user_id=self.request.data.get('user_id'))
    #     category = Category.objects.get(id=self.request.data.get('category'))
    #     serializer.save(author=author, category=category)

word_view = WordListCreateView.as_view()

class WordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

word_detail_view = WordDetailView.as_view()