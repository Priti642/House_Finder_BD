from django import forms
from property.models import PropertyModel, LocationModel, ReviewModel
from tinymce.widgets import TinyMCE


# Property Register Form
class PropertyForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingTitle', 'class': 'form-control', 'placeholder': 'Post Title'
            }
        ),
        label='Title',
    )
    location = forms.ModelChoiceField(
        required=True,
        queryset=LocationModel.objects.all().order_by('name'),
        widget=forms.Select(
            attrs={
                'id': 'floatingLocation', 'class': 'form-control', 'placeholder': 'Location'
            },
        ),
        label='Location',
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingAddress', 'class': 'form-control', 'placeholder': 'Address'
            }
        ),
        label='Title',
    )
    property_type = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingPropertyType', 'class': 'form-control', 'placeholder': 'Property Type'
            },
        ),
        label='Property Type',
    )
    amount = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingAmount', 'class': 'form-control', 'placeholder': 'Amount'
            },
        ),
        label='Amount',
    )
    status = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'floatingStatus', 'class': 'form-select',
            },
        ),
        choices=(
            ('Rent', 'Rent'),
            ('Sale', 'Sale'),
        ),
        label='Status'
    )
    area = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'floatingArea', 'class': 'form-control', 'placeholder': 'Area'
            },
        ),
        label='Area',
    )
    bedroom = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingBedroom', 'class': 'form-control', 'placeholder': 'Bedroom'
            },
        ),
        label='Bedroom',
    )
    bathroom = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingBathroom', 'class': 'form-control', 'placeholder': 'Bathroom'
            },
        ),
        label='Bathroom',
    )
    garage = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'floatingGarage', 'class': 'form-control', 'placeholder': 'Garage'
            },
        ),
        label='Garage',
    )
    propety_description = forms.CharField(
        required=True,
        widget=TinyMCE(
            attrs={
                'id': 'id_text',
            },
        ),
        min_length=10,
        label='Write Here',
    )
    picture1 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control', 'id': 'formFile', 'onchange': 'readImage(this)',
                'style': 'padding: 20px 20px 0'
            },
        ),
        allow_empty_file=False,
        label='Insert Picture',
    )
    picture2 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control', 'id': 'formFile', 'onchange': 'readImage(this)',
                'style': 'padding: 20px 20px 0'
            },
        ),
        allow_empty_file=False,
        label='Insert Picture',
    )
    picture3 = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control', 'id': 'formFile', 'onchange': 'readImage(this)',
                'style': 'padding: 20px 20px 0'
            },
        ),
        allow_empty_file=False,
        label='Insert Picture',
    )
    balcony = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'balconyCheckbox'
            }
        )
    )
    internet = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'internetCheckbox'
            }
        )
    )
    parking = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'parkingCheckbox'
            }
        )
    )
    gym_center = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'gym_centerCheckbox'
            }
        )
    )
    swimming_pool = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'swimming_poolCheckbox'
            }
        )
    )
    cable_TV = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'cable_TVCheckbox'
            }
        )
    )
    playground = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'playgroundCheckbox'
            }
        )
    )
    laundry_services = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'laundry_servicesCheckbox'
            }
        )
    )
    online_rent_payments = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'online_rent_paymentsCheckbox'
            }
        )
    )
    security_guards = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'security_guardsCheckbox'
            }
        )
    )
    barbecue_areas = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'barbecue_areasCheckbox'
            }
        )
    )
    bike_storage = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'bike_storageCheckbox'
            }
        )
    )
    rooftop_lounge_areas = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input', 'id': 'rooftop_lounge_areasCheckbox'
            }
        )
    )

    latitude = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'id': 'latitude',
            }
        )
    )

    longitude = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'id': 'longitude',
            }
        )
    )

    class Meta:
        model = PropertyModel
        fields = '__all__'
        exclude = ('user',)

    def save(self, commit=True, picture_edited=None, is_edited=False, pid=None):

        save_property = super(PropertyForm, self).save(commit=False)
        if is_edited:
            save_property.property_id = pid
        save_property.title = self.cleaned_data['title']
        save_property.location = self.cleaned_data['location']
        save_property.address = self.cleaned_data['address']
        save_property.property_type = self.cleaned_data['property_type']
        save_property.amount = self.cleaned_data['amount']
        save_property.status = self.cleaned_data['status']
        save_property.area = self.cleaned_data['area']
        save_property.bedroom = self.cleaned_data['bedroom']
        save_property.bathroom = self.cleaned_data['bathroom']
        save_property.garage = self.cleaned_data['garage']
        save_property.property_description = self.cleaned_data['propety_description']

        if picture_edited[0]:
            save_property.picture1 = self.picture1
        if picture_edited[1]:
            save_property.picture2 = self.picture2
        if picture_edited[2]:
            save_property.picture3 = self.picture3

        save_property.balcony = self.cleaned_data['balcony']
        save_property.internet = self.cleaned_data['internet']
        save_property.parking = self.cleaned_data['parking']
        save_property.gym_center = self.cleaned_data['gym_center']
        save_property.swimming_pool = self.cleaned_data['swimming_pool']
        save_property.cable_TV = self.cleaned_data['cable_TV']
        save_property.playground = self.cleaned_data['playground']
        save_property.laundry_services = self.cleaned_data['laundry_services']
        save_property.online_rent_payments = self.cleaned_data['online_rent_payments']
        save_property.security_guards = self.cleaned_data['security_guards']
        save_property.barbecue_areas = self.cleaned_data['barbecue_areas']
        save_property.bike_storage = self.cleaned_data['bike_storage']
        save_property.rooftop_lounge_areas = self.cleaned_data['rooftop_lounge_areas']

        save_property.latitude = self.cleaned_data['latitude']
        save_property.longitude = self.cleaned_data['longitude']

        save_property.user = self.user

        if commit:
            if is_edited:
                PropertyModel.objects.get(property_id=save_property.property_id).delete()

            save_property.save(picture_edited)
            print("Form saved")
        return save_property


# Rating Form
class ReviewForm(forms.ModelForm):
    review = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'id': 'textMessage', 'class': 'form-control', 'placeholder': 'Write your Review here', 'rows': '8', 'cols': '45'
            },
        ),
        min_length=10,
        label='Write your Review here',
    )

    class Meta:
        model = ReviewModel
        fields = ('review',)
