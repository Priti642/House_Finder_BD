from django.urls import path
from property.views import *

app_name = 'property'

urlpatterns = [
    path('', property_dashboard, name='property_dashboard'),
    path('search', property_search, name='property_search'),
    path('register_property/', register_property, name='register_property'),
    path('property_view/<property_id>', property_view, name='property_view'),
    path('property_view/<property_id>/edit', edit_property, name='edit_property'),
    path('property_view/<property_id>/delete', delete_property, name='delete_property'),

    path('save_review/<property_id>', save_review, name='save_review'),
    path('delete_review/<review_id>', delete_review, name='delete_review'),

    path('api/district', DistrictList.as_view(), name='district_api'),
]
