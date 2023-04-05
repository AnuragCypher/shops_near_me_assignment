from django import forms


class LocationDistanceForm(forms.Form):
    latitude = forms.FloatField(label="enter the latitude")
    longitude = forms.FloatField(label="enter the longitude")
    distance = forms.IntegerField(label="enter the distance")