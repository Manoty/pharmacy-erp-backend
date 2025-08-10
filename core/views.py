from django.http import JsonResponse

def landing_info(request):
    return JsonResponse({"messaage":"welcome to Equator pharmacy"})