import pathlib
import tempfile
from django.test import TestCase
from django.contrib.auth.models import User
from property.models import PropertyModel


class PropertyModelTest(TestCase):

    def setUp(self) -> None:
        user_ = User.objects.create(
            username="rrrrr",
            first_name="rick",
            last_name="asjidysdi",
            email="example@gmail.com",
            password="a24hellocvbc",
            is_superuser=True,
        )

        PropertyModel.objects.create(
            property_id=15,
            title="Test House",
            location="Dhaka",
            address="Block A, Road 11",
            property_type="House",
            amount=3000,

            status="Sale",
            area=7000,
            bedroom=4,
            bathroom=2,
            garage=1,

            propety_description=["<h4>Proin eget tortor risus. Donec sollicitudin molestie malesuada. Cras ultricies ligula sed magna dictum porta."],
            picture1=tempfile.NamedTemporaryFile(suffix=".jpg").name,

            latitude=23.818089,
            longitude=90.421216,
            user=user_,

            balcony=True,
            internet=False,
            parking=True,
            gym_center=False,
            swimming_pool=True,
            cable_TV=False,
            playground=True,
            laundry_services=False,
            online_rent_payments=True,
            security_guards=False,
            barbecue_areas=True,
            bike_storage=False,
            rooftop_lounge_areas=True,
        )

    def test_title(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.title, "Test House")

    def test_location(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.location, "Dhaka")

    def test_address(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.address, "Block A, Road 11")

    def test_property_type(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.property_type, "House")

    def test_amount(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.amount, 3000)

    def test_status(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.status, "Sale")

    def test_area(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.area, '7000')

    def test_bedroom(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.bedroom, 4)

    def test_bathroom(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.bathroom, 2)

    def test_garage(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.garage, 1)

    def test_propety_description(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.propety_description,"['<h4>Proin eget tortor risus. Donec sollicitudin molestie malesuada. Cras ultricies ligula sed magna dictum porta.']")

    def test_picture1(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(pathlib.Path(p.picture1.name).suffix, ".jpg")

    def test_latitude(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.latitude, 23.818089)

    def test_longitude(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(p.longitude, 90.421216)

    def test_user(self):
        p = PropertyModel.objects.get(property_id=15)
        u = User.objects.get(username="rrrrr")
        self.assertEqual(p.user, u)

    def test_balcony(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.balcony, True)

    def test_internet(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.internet, True)

    def test_parking(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.parking, True)

    def test_gym_center(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.gym_center, True)

    def test_swimming_pool(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.swimming_pool, True)

    def test_cable_TV(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.cable_TV, True)

    def test_playground(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.playground, True)

    def test_laundry_services(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.laundry_services, True)

    def test_online_rent_payments(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.online_rent_payments, True)

    def test_security_guards(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.security_guards, True)

    def test_barbecue_areas(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.barbecue_areas, True)

    def test_bike_storagee(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertFalse(p.bike_storage, True)

    def test_rooftop_lounge_areas(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertTrue(p.rooftop_lounge_areas, True)

    def test_string_present(self):
        p = PropertyModel.objects.get(property_id=15)
        self.assertEqual(str(p), str(str(p.property_id)+" - "+ str(p.user)))