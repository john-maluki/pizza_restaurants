from app import app


class TestAPI:
    def test_homepage_view(self):
        """
        Test homepage url is reachable
        """
        client = app.test_client(self)
        response = client.get("/")
        assert response.status_code == 200

    def test_fetching_all_restaurants_api(self):
        """
        Test fetching all restaurants
        """
        client = app.test_client(self)
        response = client.get("/restaurants")
        assert response.status_code == 200

    def test_fetching_restaurant_by_id_api(self):
        """
        Test fetching restaurants by id
        """
        client = app.test_client(self)
        response = client.get("/restaurants/1")
        assert response.status_code == 200

    def test_fetching_restaurant_by_id_api_not_in_db(self):
        """
        Test fetching restaurants by id which is not in db
        """
        client = app.test_client(self)
        response = client.get("/restaurants/100")
        assert response.status_code == 404
        # assert response.data["error"] == "Restaurant not found"
