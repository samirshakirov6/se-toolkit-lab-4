"""End-to-end tests for the GET /interactions endpoint."""

import pytest

BASE_URL = "http://localhost:5050"  # Default, will be overridden by fixture


def test_get_interactions_returns_200(client) -> None:
    """Test 1: GET /interactions/ returns HTTP status code 200."""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_items_have_expected_fields(client) -> None:
    """Test 2: GET /interactions/ response items contain the expected fields."""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        item = data[0]
        assert "id" in item
        assert "item_id" in item
        assert "created_at" in item


def test_get_interactions_filter_includes_boundary(client) -> None:
    """Test 3: GET /interactions/?max_item_id=1 returns items with item_id <= 1."""
    response = client.get("/interactions/", params={"max_item_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Should return non-empty list
    for item in data:
        assert item["item_id"] <= 1
