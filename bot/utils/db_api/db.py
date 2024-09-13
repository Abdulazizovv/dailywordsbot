from botapp.models import BotUsers
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
        

    
    