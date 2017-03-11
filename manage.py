if __name__ == '__main__':
    from app import create_app, db

    app = create_app()

    with app.app_context():
        from app import Models
        db.create_all()

