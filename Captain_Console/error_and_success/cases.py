from users.models import Customer


def error(context, message):
    context['error'] = True
    context['message'] = message

    return context

def get_profile(context, request):
    if request.user.is_authenticated:
        context['profile'] = Customer.objects.get(user=request.user)
    return context

def success(context, message):
    context['success'] = True
    context['message'] = message

    return context