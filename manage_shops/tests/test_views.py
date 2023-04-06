
import json
import pytest
from django.urls import reverse
from rest_framework import status
from manage_shops.forms import LocationDistanceForm

class TestFindShopsNearMe:

    @pytest.mark.django_db
    def test_find_shops_view(self,client):

        data = {'latitude': 19.267939, 'longitude': 72.971153, 'distance' : 2}
        form = LocationDistanceForm(data=data)

        response = client.post(reverse('find shops'), data)

        assert response.status_code == 200
        assert str(type(response.content)) == "<class 'bytes'>"