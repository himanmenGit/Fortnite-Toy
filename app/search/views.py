from django.http import JsonResponse

from utils.test_fortnite_search import getFortnite


def get_search_player(request):
    context = getFortnite()
    return JsonResponse(context)
