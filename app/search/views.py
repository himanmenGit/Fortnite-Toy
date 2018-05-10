from django.http import HttpResponse, JsonResponse

from utils.test_fortnite_search import getFortnite


def get_search_player(request):
    context = getFortnite()
    print(context)
    return JsonResponse(context)
