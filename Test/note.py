from fastapi.testclient import TestClient
class Note:

   @staticmethod
   def test_get_all_note(client: TestClient, url: str):
      query = """
      query{
         getAllNotes{
            name
            description
            id
         }
      }
      """
      response = client.post(url, json={"query": query})
      assert response.status_code == 200
      assert type(response.json()["data"]["getAllNotes"]) == list
      assert type(response.json()["data"]["getAllNotes"][0]) == dict
      assert "name" in response.json()["data"]["getAllNotes"][0]
      assert "description" in response.json()["data"]["getAllNotes"][0]
      assert "id" in response.json()["data"]["getAllNotes"][0]


   """
   Need to create data first
   """
   @staticmethod
   def test_get_note_by_id(client: TestClient, url: str):
      query = """
      query{
         getNote(id: 3){
            name
            description
            id
         }
      }
      """
      response = client.post(url, json={"query": query})
      assert response.status_code == 200
      assert "data" in response.json()
      assert "getNote" in response.json()["data"]
      assert "name" in response.json()["data"]["getNote"]
      assert "description" in response.json()["data"]["getNote"]
      assert "id" in response.json()["data"]["getNote"]

   @staticmethod
   def test_create_note(client: TestClient, url: str):
      query = """
      mutation{
         createNote(note: {
            name: "Test",
            description: "Test"
         }){
            name
            description
            id
         }
      }
      """
      response = client.post(url, json={"query": query})
      assert response.status_code == 200
      assert "data" in response.json()
      assert "createNote" in response.json()["data"]
      assert "name" in response.json()["data"]["createNote"]
      assert "description" in response.json()["data"]["createNote"]
      assert "id" in response.json()["data"]["createNote"]

   @staticmethod
   def test_update_note(client: TestClient, url: str):
      query = """
      mutation{
         updateNote(id: 2, note: {
            name: "Test",
            description: "Test"
         }){
            success
         }
      }
      """
      response = client.post(url, json={"query": query})
      assert response.status_code == 200
      assert "data" in response.json()
      assert "updateNote" in response.json()["data"]
      assert "success" in response.json()["data"]["updateNote"]
      assert response.json()["data"]["updateNote"]["success"] == False # because id 2 is not exist


   @staticmethod
   def test_delete_note_by_id(client: TestClient, url: str):
      query = """
      mutation{
         deleteNote(id: 2){
            success
         }
      }
      """
      response = client.post(url, json={"query": query})
      assert response.status_code == 200
      assert "data" in response.json()
      assert "deleteNote" in response.json()["data"]
      assert "success" in response.json()["data"]["deleteNote"]
      assert response.json()["data"]["deleteNote"]["success"] == False # because id 2 is not exist