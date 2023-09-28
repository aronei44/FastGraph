from fastapi.testclient import TestClient
from App.main import app

from Test import Main
from App.Config.Database import DatabaseSession


client = TestClient(app)
graph_url = "/graphql"

db = DatabaseSession("sqlite+aiosqlite:///database.db")
app.dependency_overrides[DatabaseSession] = db

def clientMap(func):
	def wrapper(*args, **kwargs):
		func(client, graph_url, *args, **kwargs)
	return wrapper

def test_read_main():
   	Main.test_read_main(client)
	   
email = "test3@mail.com"
password = "test"
@clientMap
def test_auth(client, url):
	
	query = '''
	mutation {
		register(registerInput: {
			username: "test", email: "''' + email + '''", password: "''' + password + '''"
		}) {
			success
			message
		}
	}
	'''
	response = client.post(url, json={"query": query})
	assert response.status_code == 200
	assert "data" in response.json()
	assert "register" in response.json()["data"]
	assert "success" in response.json()["data"]["register"]

@clientMap
def test_login(client, url):
	query = '''
	mutation {
		login(loginInput: {
			email: "''' + email + '''", password: "''' + password + '''"
		}) {
			email
			token
		}
	}
	'''

	response = client.post(url, json={"query": query})
	assert response.status_code == 200
	assert "data" in response.json()
	assert "login" in response.json()["data"]
	assert "email" in response.json()["data"]["login"]
	assert "token" in response.json()["data"]["login"]