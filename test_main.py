from fastapi.testclient import TestClient
from main import app

from Test.main import Main



client = TestClient(app)


def test_read_main():
   Main.test_read_main(client)