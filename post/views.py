from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from post.forms import PostPropertyPermissionForm
from post.models import PostPropertyPermissionModel

# Apply to be able to post property
@login_required
def apply_to_post_property(request):
    if len(PostPropertyPermissionModel.objects.filter(user_id=request.user)) > 0:
        return  redirect('post:edit_profile')

    if request.method == 'POST':
        post_property_form = PostPropertyPermissionForm(data=request.POST)
        print(post_property_form.errors)
        if post_property_form.is_valid():
            post_property_form.user = request.user
            post_property_form.save()
            messages.success(request, "You will be able to post property")

            return redirect('property:register_property')

        else:
            messages.error(request, "Error occured . Please try again")


    post_property_form = PostPropertyPermissionForm()
    return render(request=request, template_name='post/apply_post_property.html', context={'post_property_form': post_property_form})


# Edit profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        old_value = get_object_or_404(PostPropertyPermissionModel, user=request.user)
        profile_form = PostPropertyPermissionForm(data=request.POST or None, instance=old_value)

        if profile_form.is_valid():

            profile_form.user = request.user
            profile_form.save(is_edited=True)
            messages.success(request, "Profile has been edited successfully.")
            return redirect('home')

    else:
        query = PostPropertyPermissionModel.objects.get(user_id=request.user)
        post_property_form = PostPropertyPermissionForm(instance=query)
        return render(request=request, template_name='post/apply_post_property.html', context={'post_property_form': post_property_form})