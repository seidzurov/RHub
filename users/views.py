from django.shortcuts import render
from .models import Profile


def profiles_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "users/profiles_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    follows_count = profile.follows.all().count()
    followers_count = profile.followers.all().count()
    data = {"profile": profile, 
            "follows_count": follows_count, 
            "followers_count": followers_count}
    
    return render(request, "users/profile.html", context=data)

# def my_profile(request, pk):
#     profile = Profile.objects.get(pk=request.id)
#     follows_count = profile.follows.all().count()
#     followers_count = profile.followers.all().count()
#     data = {"profile": profile, 
#             "follows_count": follows_count, 
#             "followers_count": followers_count}
    
#     return render(request, "users/profile.html", context=data)
