from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .models import Profile


def get_profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist as exception_alias:
        response = JsonResponse({'error': f'{exception_alias}'})
        response.status_code = 200
        return response
    json_data = {
        'id': profile.id,
        'user': user.id,
        'e-mail': profile.e_mail_field,
        'phone_number': profile.phone_number
    }
    return JsonResponse({'profile': json_data})


