from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from property.forms import PropertyForm, ReviewForm
from property.models import PropertyModel, LocationModel, ReviewModel
from post.models import PostPropertyPermissionModel
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


# Write and save the details of a property
@login_required
def register_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(data=request.POST, files=request.FILES)
        picture_edited = [False, False, False]

        if property_form.is_valid():
            if request.FILES.get('picture1'):
                property_form.picture1 = request.FILES.get('picture1', False)
                picture_edited[0] = True
            if request.FILES.get('picture2'):
                property_form.picture2 = request.FILES.get('picture2', False)
                picture_edited[1] = True
            if request.FILES.get('picture3'):
                property_form.picture3 = request.FILES.get('picture3', False)
                picture_edited[2] = True

            property_form.user = request.user
            property_form.save(picture_edited=picture_edited)

            messages.success(request, "Property has been registered and posted.")
            return redirect('property:register_property')

        else:
            messages.error(request, property_form.errors)
            return redirect(request.META['HTTP_REFERER'])

    else:
        if len(PostPropertyPermissionModel.objects.filter(user_id=request.user)) > 0:
            property_form = PropertyForm()
            return render(request=request, template_name='property/register_property.html', context={'property_form': property_form})
        else:
            return redirect('post:apply_to_post_property')


# Blog dashboard view
def property_dashboard(request):
    properties = PropertyModel.objects.all().order_by('-time')

    page = request.GET.get('page', 1)
    paginator = Paginator(properties, 12)

    data = {
        'count': properties.count()
    }

    try:
        data['properties'] = paginator.get_page(page)
    except Exception:
        data['properties'] = paginator.get_page(1)

    return render(request=request, template_name='property/property_dashboard.html', context=data)


# View single property
def property_view(request, property_id):
    query = get_object_or_404(PropertyModel, property_id=property_id)
    profile = PostPropertyPermissionModel.objects.get(user_id=query.user)
    user = User.objects.get(username=query.user)
    review = ReviewModel.objects.filter(property_id=property_id)

    data = {
        'property': query,
        'access': True if request.user == query.user else False,
        'profile': profile,
        'property_user': user,
        'review_form': ReviewForm,
        'reviews': review,
        'review_users': [r.get_user() for r in review],
        'review_count': review.count(),
    }

    return render(request=request, template_name='property/property_view.html', context=data)


# Edit property
@login_required
def edit_property(request, property_id):
    if request.method == 'POST':
        old_value = get_object_or_404(PropertyModel, property_id=property_id)
        property_form = PropertyForm(data=request.POST or None, files=request.FILES, instance=old_value)
        picture_edited = [False, False, False]

        if property_form.is_valid():
            if request.FILES.get('picture1'):
                property_form.picture1 = request.FILES.get('picture1', False)
                picture_edited[0] = True
            if request.FILES.get('picture2'):
                property_form.picture2 = request.FILES.get('picture2', False)
                picture_edited[1] = True
            if request.FILES.get('picture3'):
                property_form.picture3 = request.FILES.get('picture3', False)
                picture_edited[2] = True

            property_form.user = request.user
            property_form.save(picture_edited=picture_edited, is_edited=True, pid=property_id)
            messages.success(request, "Property has been edited successfully.")
            return redirect('property:property_view', property_id)

    else:
        query = PropertyModel.objects.get(property_id=property_id)
        location = LocationModel.objects.get(name=query.location.split(" - ")[0])
        data = {
            'is_edited': True,
            'location': location.id,
            'property_form': PropertyForm(instance=query),
        }

        return render(request=request, template_name='property/register_property.html', context=data)


# Delete property
@login_required
def delete_property(request, property_id):
    PropertyModel.objects.get(property_id__exact=property_id).delete()
    messages.success(request, "Property has been deleted.")
    return redirect('property:property_dashboard')


# Converting queryset to Json data
class DataSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = LocationModel
        fields = ('name', 'bn_name')


# API to serve District List
class DistrictList(APIView):
    permission_classes = [AllowAny]

    def get(self, requests):
        result = LocationModel.objects.all().order_by('name')
        serializer = DataSerializer(result, many=True)
        return Response(serializer.data)


# Search function
def property_search(request):
    keyword = request.GET.get('keyword')
    type_ = request.GET.get('type')
    city = request.GET.get('city')
    if city == "null":
        city = ""
    bedrooms = request.GET.get('bedrooms')
    bathroom = request.GET.get('bathroom')
    price = request.GET.get('price')

    properties = (
            PropertyModel.objects.filter(status__icontains=type_) &
            PropertyModel.objects.filter(location__icontains=city) &
            PropertyModel.objects.filter(bedroom__gte=bedrooms) &
            PropertyModel.objects.filter(bathroom__gte=bathroom) &
            PropertyModel.objects.filter(amount__gte=price) &
            (
                    PropertyModel.objects.filter(title__contains=keyword) |
                    PropertyModel.objects.filter(address__contains=keyword) |
                    PropertyModel.objects.filter(property_type__icontains=keyword)
            )
    ).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(properties, 12)

    data = {
        'count': properties.count()
    }

    try:
        data['properties'] = paginator.get_page(page)
    except Exception:
        data['properties'] = paginator.get_page(1)

    return render(request=request, template_name='property/property_dashboard.html', context=data)


def save_review(request, property_id):
    star = request.POST.get('star')
    review = request.POST.get('review')

    review_object = ReviewModel.objects.create(
        property=PropertyModel.objects.get(property_id=property_id),
        star=star,
        review=review,
        user=User.objects.get(username=request.user.username),
    )

    review_object.save()

    return redirect(request.META['HTTP_REFERER'])


# Delete review made on Property
@login_required
def delete_review(request, review_id):
    specified_review = ReviewModel.objects.get(id=review_id)
    specified_review.delete()
    return redirect(request.META['HTTP_REFERER'])
