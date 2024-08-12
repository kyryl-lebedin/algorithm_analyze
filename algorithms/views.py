from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the algorithms index.")

def arg_test(request, arg: int): # arg into func comes from the url
    return HttpResponse(f"Hello, world. You're at the algorithms index. You passed in {arg} " )
    
def send_to_alg_setup(request):
    return render(request, 'algorithms/alg_setup.html')

def receive_alg(request):
    # Prepare data to be returned as JSON
    data = {
        'arg1': 'Value1',
        'arg2': 'Value2'
    }
    # Return response as JSON
    return JsonResponse(data)
