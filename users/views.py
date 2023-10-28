from django.shortcuts import render

from users.models import User


def users(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, "users/user_list.html", context)
