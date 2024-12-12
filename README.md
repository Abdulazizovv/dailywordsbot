
# WordWise

this project help to users for learn new words or memorize this words using quiz


## Run Locally

Clone the project

```bash
git clone https://github.com/Abdulazizovv/dailywordsbot.git
```

Go to the project directory

```bash
  cd dailywordsbot
```
Create .env file and write this lines:
```bash
ADMINS=12345678,12345677,12345676
BOT_TOKEN=123452345243:Asdfasdfasf
ip=localhost
```

Install requirements

```bash
  pip install -r requirements.txt
```

Start the bot

```bash
  python manage.py app
```
or
```bash
  python3 manage.py app
```



## API Reference

#### Get all bot users

```http
  GET /api/bot-users/
```
**Example response body**
```json
[
  {
        "id": int,
        "user_id": string,
        "first_name": string,
        "last_name": string,
        "phone_number": string | null,
        "username": string,
        "created": timestamp,
        "updated": timestamp
  }
]
```

#### Get item

```http
  GET /api/bot-users/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. ID of bot user *not telegram user id* |

**Example response body**
```json
{
      "id": int,
      "user_id": string,
      "first_name": string,
      "last_name": string,
      "phone_number": string | null,
      "username": string,
      "created": timestamp,
      "updated": timestamp
}
```


