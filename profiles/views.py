from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profiles = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=profiles)
    orders = profiles.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)
