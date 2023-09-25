from fastapi.testclient import TestClient
from App.main import app

from Test import Main, Note
from App.Config.Database import DatabaseSession


client = TestClient(app)
graph_url = "/graphql"

db = DatabaseSession("sqlite+aiosqlite:///database.db")
app.dependency_overrides[DatabaseSession] = db

def test_read_main():
   	Main.test_read_main(client)

def test_get_all_note():
   	Note.test_get_all_note(client, graph_url)

def test_get_note_by_id():
   	Note.test_get_note_by_id(client, graph_url)

def test_create_note():
   	Note.test_create_note(client, graph_url)

def test_update_note():
   	Note.test_update_note(client, graph_url)

def test_delete_note():
    Note.test_delete_note_by_id(client, graph_url)

"""
WARNING: test still error because run time error from pytest
"""