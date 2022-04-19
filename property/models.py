from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField

User = get_user_model()


# Serve distrct data
class LocationModel(models.Model):
    id = models.AutoField(primary_key=True)
    division_id = models.IntegerField(null=False)
    name = models.TextField(null=False, unique=True)
    bn_name = models.TextField(null=False, unique=True)
    lat = models.TextField()
    lon = models.TextField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'districts'

    def __str__(self):
        return self.name+" - "+self.bn_name


# Property Model
class PropertyModel(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    location = models.TextField(null=False)
    address = models.TextField(null=False)
    property_type = models.TextField(null=False)
    amount = models.IntegerField(null=False)

    status = models.CharField(max_length=10, null=False)
    area = models.TextField(null=False)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)

    propety_description = HTMLField()
    picture1 = models.ImageField(null=False, upload_to='property_images/%Y/%m/%d/')
    picture2 = models.ImageField(upload_to='property_images/%Y/%m/%d/')
    picture3 = models.ImageField(upload_to='property_images/%Y/%m/%d/')

    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User, db_column='email', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=False)

    balcony = models.BooleanField(verbose_name='Balcony', default=False)
    internet = models.BooleanField(verbose_name='Internet', default=False)
    parking = models.BooleanField(verbose_name='Parking', default=False)
    gym_center = models.BooleanField(verbose_name='Gym Center', default=False)
    swimming_pool = models.BooleanField(verbose_name='Swimming Pool', default=False)
    cable_TV = models.BooleanField(verbose_name='Cable TV', default=False)
    playground = models.BooleanField(verbose_name='Playground', default=False)
    laundry_services = models.BooleanField(verbose_name='Laundry Services', default=False)
    online_rent_payments = models.BooleanField(verbose_name='Online Rent Payments', default=False)
    security_guards = models.BooleanField(verbose_name='Security Guards', default=False)
    barbecue_areas = models.BooleanField(verbose_name='Barbecue Areas', default=False)
    bike_storage = models.BooleanField(verbose_name='Bike Storage', default=False)
    rooftop_lounge_areas = models.BooleanField(verbose_name='Rooftop Lounge Areas', default=False)

    # Default string representation
    def __str__(self):
        return str(str(self.property_id)+" - "+ str(self.user))


# Review Model
class ReviewModel(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.OneToOneField(PropertyModel, on_delete=models.CASCADE)
    star = models.IntegerField()
    review = models.CharField(max_length=3000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=False)

    # Default string representation
    def __str__(self):
        return str(self.user) + "-" + str(self.property_id) + "=" + str(self.star)

    # Helper function to get usernames of the reviewers
    def get_user(self):
        return self.user