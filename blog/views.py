from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import BlogForm
from blog.models import BlogModel


# Save Blog
@login_required
def save_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(data=request.POST, files=request.FILES)
        print(blog_form.errors)

        if blog_form.is_valid():
            blog_form.first_picture = request.FILES.get('picture1', False)
            if request.FILES.get('picture2'):
                blog_form.second_picture = request.FILES.get('picture2', False)
            if request.FILES.get('picture3'):
                blog_form.third_picture = request.FILES.get('picture3', False)

            blog_form.user = request.user
            blog_form.save()
            return redirect('home')

        else:
            messages.error(request, "Error occured. Please try again")

    blog_form = BlogForm()
    return render(request=request, template_name='save_blog.html', context={'blog_form': blog_form})


# Blog dashboard view
def blog_dashboard(request):
    blogs = BlogModel.objects.order_by('time')

    data = {
        'blogs': blogs,
        'count': blogs.count()
    }
    return render(request=request, template_name='blog.html', context=data)


# View Blog
def blog_view(request, blog_id):
    query = BlogModel.objects.get(blog_id=blog_id)

    data = {
        'blog': query,
    }

    return render(request=request, template_name='blog_view.html', context=data)
