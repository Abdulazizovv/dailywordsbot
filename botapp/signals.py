from django.db.models.signals import post_save
from django.dispatch import receiver
from botapp.models import Category, UserCategory

# Signal to create a UserCategory object when a new Category is created
@receiver(post_save, sender=Category)
def create_user_category(sender, instance, created, **kwargs):
    if created:
        UserCategory.objects.create(user=instance.owner, category=instance)
    