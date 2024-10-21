from django.shortcuts import HttpResponse

# Create your views here.
def order_list(request):
    return HttpResponse('Order list.')

def order_details(request):
    return HttpResponse('Order details.')