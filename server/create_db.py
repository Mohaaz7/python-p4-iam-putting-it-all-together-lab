#!/usr/bin/env python3

from config import app, db

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database tables created successfully!")