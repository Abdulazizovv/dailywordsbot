from django.db import models


class BotUsers(models.Model):
    user_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name
    
    def full_name(self):
        return self.first_name + self.last_name if self.last_name else self.first_name
    

class Category(models.Model):
    owner = models.ForeignKey(BotUsers, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Word(models.Model):
    author = models.ForeignKey(BotUsers, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    meaning = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.word


class UserWord(models.Model):
    user = models.ForeignKey(BotUsers, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    is_learned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.word.word
    

class UserCategory(models.Model):
    user = models.ForeignKey(BotUsers, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    is_learned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.category.title
    

class WordOption(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Word Option"
        verbose_name_plural = "Word Options"
        unique_together = ('word', 'option')
    
    def save(self, *args, **kwargs):
        if self.is_correct:
            WordOption.objects.filter(word=self.word, is_correct=True).update(is_correct=False)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.option
    

    

