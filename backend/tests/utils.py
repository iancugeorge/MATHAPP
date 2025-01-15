from typing import Dict
from app.models import User
from app.auth.security import get_password_hash

def create_test_user(db) -> User:
    """Create a test user in the database"""
    user = User(
        email="test@example.com",
        username="testuser",
        password_hash=get_password_hash("testpass123"),
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_auth_headers(client, email: str, password: str) -> Dict[str, str]:
    """Get authentication headers for a user"""
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password
        }
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}