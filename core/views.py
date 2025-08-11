from django.http import JsonResponse

def landing_info(request):
    return JsonResponse({"messaage":"welcome to Equator pharmacy"})

def api_root(request):
    return JsonResponse({"message": "Welcome to Pharmacy ERP Backend API!"})