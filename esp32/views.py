from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

x = ''

# @csrf_exempt
# def sensor_data(request):
#     if request.method == 'POST':
#         # Retrieve sensor data from the request
#         data = request.POST.get('data')
#         # Process the data as needed (save to database, etc.)
#         print("Received sensor data:", data)
#         # Send a response
#         global x
#         x = JsonResponse({'status': 'success'})
#         print(x)
#         print("The value of data is ",data)
#         return JsonResponse({'status': 'success'})
#     else:
#         # Return an error response for other request methods
#         return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})
# print("The value of x is ",x)

from django.http import JsonResponse

# @csrf_exempt
# def sensor_data(request):
#     if request.method == 'POST':
#         # Handle POST requests
#         data = request.POST.get('data')
#         # Process the data as needed
#         print("Received sensor data:", data)
#         # Return a success response
#         return JsonResponse({'status': 'success'})
#     elif request.method == 'GET':
#         # Handle GET requests
#         return JsonResponse({'status': 'error', 'message': 'GET requests are not supported.'})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# @csrf_exempt
# def sensor_data(request):
#     if request.method == 'POST':
#         # Retrieve sensor data from the request body
#         data = json.loads(request.body)
#         # data = {
#         #     'data':'data received'
#         # }
#         # Process the data as needed
#         # print("Received sensor data:", data)
#         # Return a success response
#         return JsonResponse({'status': 'success'})
#         # return render(request,'sensor_data.html',data)
#     elif request.method == 'GET':
        
#         # data = {
#         #     'data':'No data recieved'
#         # }
#         # return render(request,'sensor_data.html',data)

#         # Handle GET requests
#         return JsonResponse({'status': 'error', 'message': 'GET requests are not supported.'})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        # print("data received is ",data)

        data = request.POST.get('sensor_data')
        print("Received sensor data:", data)

        # Handle POST request
        return JsonResponse(
            {
            'object': 'fan',
            'data': '0.5'
            }
        )
    else:
        return JsonResponse({'status': 'error', 'message': 'GET requests are not supported - Anurag upadhyay.'})
