from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# import serial
# Define the serial port connection to Arduino
# arduino_port = 'COM3'  # Adjust this based on your system
# baud_rate = 9600
# ser = serial.Serial(arduino_port, baud_rate)


@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':

        sensor_data = request.POST.get('sensor_data')
        print("Received sensor data:", sensor_data)

        file_path = "data.json"
        sentData = None       
        with open(file_path, 'r') as json_file:
            # Read the JSON data from the file
            # global sentData
            sentData = json.load(json_file)
        
        print("Sending data:", sentData)
        return JsonResponse(sentData)
        
    else:
        return render(request,'sensor_data.html')
        # return JsonResponse({'status': 'error', 'message': 'GET requests are not supported - Anurag upadhyay.'})


def data_recieved(request):
    if request.method == 'POST':
        applianceObject = request.POST.get('applianceObject')
        # applianceObject = 'fan'
        intenseValue = request.POST.get('intenseValue')

        data = {'Object': applianceObject, 'value': intenseValue}

        file_path = "data.json"
        # Open the JSON file in write mode
        with open(file_path, 'w') as json_file:
            # Write the data to the file
            json.dump(data, json_file)
        
        return render(request,'sensor_data.html',{'status':'File written succesfully !'})

    return render(request,'sensor_data.html')