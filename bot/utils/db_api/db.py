from botapp.models import BotUsers, Word, Category
import logging


# for adding new user
def add_bot_user(**data):
    if not BotUsers.objects.filter(user_id=data.get("user_id")).exists():
        try:
            BotUsers.objects.create(
                **data
            )
            return True
        except Exception as err:
            logging.error(err)
            return False
        
# for adding new word
def add_word(**data):
    try:
        BotUsers.objects.get(user_id=data.get("author"))
        Category.objects.get(id=data.get("category"))
        Word.objects.create(
            **data
        )
        return True
    except Exception as err:
        logging.error(err)
        return False
    

# for adding new category
def add_category_db(**data):
    try:
        user = BotUsers.objects.get(user_id=data.get("author_id"))
        data["owner"] = user
        Category.objects.create(
            **data
        )
        return True
    except Exception as err:
        logging.error(err)
        return False

# for getting all words
def get_words():
    return Word.objects.all()

# for getting all categories
def get_categories():
    return Category.objects.all()

# for getting all users
def get_users():
    return BotUsers.objects.all()

# for getting word by id
def get_word_by_id(word_id):
    return Word.objects.get(id=word_id)

# for getting category by id
def get_category_by_id(category_id):
    return Category.objects.get(id=category_id)

# for getting user by id
def get_user_by_id(user_id):
    return BotUsers.objects.get(user_id=user_id)

