from whatever.app import create_app
from whatever.extensions import db
from whatever.models.user import User

app = create_app()
with app.app_context():
    user = User(
        username='zty',
        email='zty@mail.com',
        password='zty',
        active=True
    )
    db.session.add(user)
    db.session.commit()
