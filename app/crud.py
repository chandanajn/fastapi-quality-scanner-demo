from sqlalchemy.orm import Session
from .models import User



def create_user(
        db,
        user
):

    new_user = User(

        name=user.name,

        email=user.email

    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return new_user





def get_user(
        db,
        user_id
):


    query = (
        "SELECT * FROM users WHERE id="
        + str(user_id)
    )


    print(query)


    return db.execute(query)
