from flaskvue import (
    create_app,
    todo,
    user
)

from flaskvue.extensions import (
    db,
    bcrypt
)

app = create_app()

with app.app_context():
    db.create_all()

    Todo = todo.models.Todo
    User = user.models.User
    
    # user creation
    users = [
        'user1',
        'user2'
    ]

    # task creation
    tasks = [
        'do the dishes',
        'ace the interview'
    ]
    
    for i in range(len(users)):
        u = User(
            username = users[i],
            password = bcrypt.generate_password_hash('secret').decode('utf-8')
        )

        t = Todo(task=tasks[i])
        
        u.todos.append(t)
        
        db.session.add(u)

    
    db.session.commit()

    print(Todo.query.all())