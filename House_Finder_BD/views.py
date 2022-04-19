from django.shortcuts import render
from blog.models import BlogModel
from property.models import PropertyModel


# Homepage
def HomePage(request):
    blogs = BlogModel.objects.all().order_by('-time')[:7]
    properties = PropertyModel.objects.all().order_by('-time')[:7]

    data = {
        'blogs': blogs,
        'properties': properties
    }

    return render(request=request, template_name='index.html', context=data)
