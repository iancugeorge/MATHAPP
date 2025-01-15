import pytest
from fastapi import status
from backend.models.user import User
def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "testpass123"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["username"] == "newuser"
    assert "id" in data

def test_login_user(client, db):
    # First register a user
    client.post(
        "/auth/register",
        json={
            "email": "logintest@example.com",
            "username": "loginuser",
            "password": "testpass123"
        }
    )
    
    # Try logging in
    response = client.post(
        "/auth/login",
        data={
            "username": "logintest@example.com",
            "password": "testpass123"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client, db):
    # First register a user
    client.post(
        "/auth/register",
        json={
            "email": "wrongpass@example.com",
            "username": "wrongpassuser",
            "password": "testpass123"
        }
    )
    
    # Try logging in with wrong password
    response = client.post(
        "/auth/login",
        data={
            "username": "wrongpass@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_get_current_user(client, db):
    # Register a user
    register_response = client.post(
        "/auth/register",
        json={
            "email": "current@example.com",
            "username": "currentuser",
            "password": "testpass123"
        }
    )
    
    # Login to get token
    login_response = client.post(
        "/auth/login",
        data={
            "username": "current@example.com",
            "password": "testpass123"
        }
    )
    token = login_response.json()["access_token"]
    
    # Get current user info
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "current@example.com"
    assert data["username"] == "currentuser"