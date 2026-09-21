
import sqlite3
import pytest

import app as cafe_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a separate temporary database for testing.
    test_db = tmp_path / "test_cafe.db"

    def get_test_db_connection():
        return sqlite3.connect(str(test_db))

    # Make the application use the test database.
    monkeypatch.setattr(
        cafe_app,
        "get_db_connection",
        get_test_db_connection
    )

    # Create the bookings table in the test database.
    cafe_app.init_db()

    cafe_app.app.config["TESTING"] = True

    with cafe_app.app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_menu_page(client):
    response = client.get("/menu")
    assert response.status_code == 200


def test_gallery_page(client):
    response = client.get("/gallery")
    assert response.status_code == 200


def test_our_story_page(client):
    response = client.get("/our-story")
    assert response.status_code == 200


def test_booking_is_saved(client, tmp_path, monkeypatch):
    test_db = tmp_path / "test_cafe.db"

    def get_test_db_connection():
        return sqlite3.connect(str(test_db))

    monkeypatch.setattr(
        cafe_app,
        "get_db_connection",
        get_test_db_connection
    )

    response = client.post(
        "/booking",
        data={
            "name": "Test Customer",
            "phone": "9876543210",
            "date": "2026-10-10",
            "time": "18:30",
            "guests": "2",
            "message": "Automated test booking"
        }
    )

    assert response.status_code == 200

    # Verify that the booking was actually inserted.
    connection = sqlite3.connect(str(test_db))
    booking = connection.execute(
        "SELECT name, phone, date, time, guests, message "
        "FROM bookings WHERE name = ?",
        ("Test Customer",)
    ).fetchone()
    connection.close()

    assert booking == (
        "Test Customer",
        "9876543210",
        "2026-10-10",
        "18:30",
        "2",
        "Automated test booking"
    )