from database import db, User
from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
    
def get_users(limit=10):
    users = User.query.limit(limit).all()
    for user in users:
        return object_as_dict(user)

def create_user(current_user):
    user = User(username=current_user["id"])
    db.session.add(user)
    db.session.commit()
    return "User successfully created !"

def get_user(username):
    user = User.query.filter_by(username=username).first_or_404(description="User not found")
    return object_as_dict(user)

def delete_user(current_user):
    user = User(username=current_user["id"])
    db.session.delete(user)
    db.session.commit()
