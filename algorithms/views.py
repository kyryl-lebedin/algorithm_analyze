from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404, JsonResponse
import json

from . import alg_processing

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the algorithms index.")

def arg_test(request, arg: int): # arg into func comes from the url
    return HttpResponse(f"Hello, world. You're at the algorithms index. You passed in {arg} " )
    
def send_to_alg_setup(request):
    context = {'algorithm_types': list(alg_processing.algorithm_types.keys()),
               'input_types': alg_processing.input_types}
    return render(request, 'algorithms/alg_setup.html', context)

def receive_alg_type(request):
    if request.method == 'POST':
        try:
            # Decode request.body (byte string) and parse it as JSON
            data = json.loads(request.body.decode('utf-8'))
            algorithm_type = data.get('algorithm_type')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        responce_data = alg_processing.algorithm_types[algorithm_type]
        return JsonResponse(responce_data)
    
def receive_alg(request):
    if request.method == 'POST':
        try:
            # Decode request.body (byte string) and parse it as JSON
            data = json.loads(request.body.decode('utf-8'))
            algorithm = data.get('algorithm')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        responce_data = {'algorithm': alg_processing.algorithms[algorithm]}
        return JsonResponse(responce_data)



def send_alg(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            algorithm = data.get('alg_code')
            input_type = data.get('input_type')
            algorithm = alg_processing.get_function_object(algorithm)
            if type(algorithm) == type('string'):
                return JsonResponse({'error': algorithm}, status=400)

            print(input_type)
            buf, predicitons = alg_processing.algorithm_analyze(algorithm, input_type)
            print(predicitons)
            return HttpResponse(buf.getvalue(), content_type='image/png')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        

