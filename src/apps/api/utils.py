
def get_user_request(request):
    user = None
    if request and hasattr(request, 'user'):
        user = request.user
    return user

