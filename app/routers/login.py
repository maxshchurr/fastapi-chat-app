# import firebase_admin
from fastapi import APIRouter


from app.users_countries_data.extract_countries import COUNTRIES
from app.firebase_conn.models import ChatUser
import app.firebase_conn.connections
from firebase_admin import db

login_router = APIRouter()


# db_reference = db.reference('chatapp/')
HANDLE_USERS = db.reference('chatapp/users/')


@login_router.get("/login")
def login():
    countries = COUNTRIES
    return {'username': "", 'countries': countries}


@login_router.post("/login")
def login(user: ChatUser):
    if user.check_if_country_is_valid():
        # Save user data to Firebase
        user_data = {
            'username': user.username,
            'country': user.country,
        }
        HANDLE_USERS.child(user.id).set(user_data)

        return {'user_id': user.id}
    else:
        return {"msg": "Not valid country!"}


@login_router.get('/login/interests')
def choose_chats_from_interests():
    """
    TODO: handle_topics is a list and db.reference('chatapp/topics').get().not_equal_to('General') doesn't work.
    TODO: probably it's better to have a dictionary inside db to handle it easier.
    TODO: (also we don't pass id of topic, only it's name, can be a problem too)
    TODO: get id of the user
    """
    handle_topics = db.reference('chatapp/topics').get()
    handle_topics.remove('General')

    return {'interests': handle_topics}


@login_router.post('/login/interests')
def choose_chats_from_interests(selected_topics: list[str]):
    """
    TODO: get id of the user
    :return: existing + user_id
    """
    handle_topics = db.reference('chatapp/topics')
    db_topics = handle_topics.get()

    for topic in selected_topics:
        if topic not in db_topics:
            return {"msg": f"Unknown topic - {topic}"}

    selected_topics.append('General')
    return {'interests': selected_topics}
