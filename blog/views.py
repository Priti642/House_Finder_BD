from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from blog.forms import BlogForm, BlogCommentForm
from blog.models import BlogModel, BlogCommentModel


# Write and Save Blog
@login_required
def save_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(data=request.POST, files=request.FILES)

        if blog_form.is_valid():
            blog_form.picture = request.FILES.get('picture', False)
            blog_form.user = request.user
            blog_form.save()
            messages.success(request, "Blog has been saved.")
            return redirect('blog:save_blog')

        else:
            messages.error(request, "Error occured. Please try again")

    blog_form = BlogForm()
    return render(request=request, template_name='blog/write_blog.html', context={'blog_form': blog_form})


# Blog dashboard view
def blog_dashboard(request):
    blogs = BlogModel.objects.all().order_by('time')

    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 12)

    data = {
        'count': blogs.count()
    }

    try:
        data['blogs'] = paginator.get_page(page)
    except Exception:
        data['blogs'] = paginator.get_page(1)

    return render(request=request, template_name='blog/blog_dashboard.html', context=data)


# View single blog
def blog_view(request, blog_id):
    query = BlogModel.objects.get(blog_id=blog_id)
    comments = BlogCommentModel.objects.filter(blog=query)
    comment_count = comments.count()
    data = {
        'blog': query,
        'comment_form': BlogCommentForm,
        'comments': comments,
        'comment_count': comment_count,
        'access': True if request.user == query.user else False
    }

    return render(request=request, template_name='blog/blog_view.html', context=data)


# Edit blog
@login_required
def edit_blog(request, blog_id):
    if request.method == 'POST':
        old_value = get_object_or_404(BlogModel, blog_id=blog_id)
        blog_form = BlogForm(data=request.POST or None, files=request.FILES, instance=old_value)
        picture_edited = False

        if blog_form.is_valid():
            if request.FILES.get('picture1'):
                blog_form.picture1 = request.FILES.get('picture', False)
                picture_edited = True

            blog_form.user = request.user
            blog_form.save(picture_edited=picture_edited)
            messages.success(request, "Blog has been edited successfully.")
            return redirect('blog:blog_view', blog_id)

    else:
        query = BlogModel.objects.get(blog_id=blog_id)
        data = {
            'is_edited': True,
            'blog_form': BlogForm(instance=query),
        }

        return render(request=request, template_name='blog/write_blog.html', context=data)

# Delete Blog
@login_required
def delete_blog(request, blog_id):
    BlogModel.objects.get(blog_id__exact=blog_id).delete()
    messages.success(request, "Blog has been deleted.")
    return redirect('blog:blog_dashboard')


# Save comment made on Blog Page
@login_required
def save_comment(request, blog_id):
    comment_form = BlogCommentForm(request.POST or None)

    if request.method == 'POST':
        comment_form.comment = request.POST['comment']
        comment_form.blog_id = blog_id
        comment_form.user = request.user
        comment_form.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, "Error occured. Please try again")
        return redirect(request.META['HTTP_REFERER'])


# Delete comment made on Blog Page
@login_required
def delete_comment(request, comment_id):
    specified_comment = BlogCommentModel.objects.get(comment_id=comment_id)
    specified_comment.delete()
    return redirect(request.META['HTTP_REFERER'])
