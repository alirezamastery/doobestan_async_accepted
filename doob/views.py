import asyncio
from asgiref.sync import sync_to_async
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import DeliveryReport, Hospital, Company, Sick, Employee
from .serializer import NameSerializer, NationalIDSerializer
from .SMS import get_phone_number, sms


@api_view(['POST'])
def get_sick_employee_by_hospital(request):
    response_dict = dict()
    if request.method == 'POST':
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            hospital_name = serializer.validated_data.get('name')
            try:
                hospital_obj = Hospital.objects.filter(name=hospital_name).first()
            except:
                hospital_obj = None
            if hospital_obj is None:
                return Response(status=400)
            patients = Sick.objects.filter(hospital=hospital_obj)
            patients_list = list()
            for patient in patients:
                try:
                    employee_obj = Employee.objects.get(nationalID=patient.nationalID)
                except:
                    employee_obj = None
                if employee_obj and patient.illName == 'Covid19':
                    patients_list.append(f"({employee_obj.name}, {employee_obj.nationalID})")
            for i, p in enumerate(patients_list):
                response_dict[i + 1] = p
        else:
            return Response(status=400)
    print(response_dict)

    return Response(response_dict)


@api_view(['POST'])
def get_sick_employee_by_company(request):
    response_dict = dict()
    if request.method == 'POST':
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            company_name = serializer.validated_data.get('name')
            try:
                company_obj = Company.objects.filter(name=company_name).first()
            except:
                company_obj = None
            if company_obj is None:
                return Response(status=400)
            employees = Employee.objects.filter(company=company_obj)
            employees_list = list()
            for employee in employees:
                try:
                    patient_obj = Hospital.objects.get(nationalID=employee.nationalID)
                except:
                    patient_obj = None
                if patient_obj and patient_obj.illName == 'Covid19':
                    employees_list.append(f'({employee.name}, {employee.nationalID})')
            for i, p in enumerate(employees_list):
                response_dict[i + 1] = p
        else:
            return Response(status=400)

    return Response(response_dict)


async def send_sms(phone_number):
    print(f'sending to {phone_number}')
    await asyncio.create_task(sms(phone_number))
    print(f'saving {phone_number}')
    loop = asyncio.get_event_loop()
    async_function = sync_to_async(DeliveryReport.objects.create)
    loop.create_task(async_function(phone_number=phone_number))


async def sms_link(request):
    print(request)
    # ---- DO NOT REMOVE THIS -----
    request.META['CONTENT_LENGTH'] = 35
    # ---- DO NOT REMOVE THIS -----
    if request.method == 'POST':
        print(request.POST)
        data = JSONParser().parse(request)
        print(data)
        serializer = NationalIDSerializer(data=data)
        if serializer.is_valid():
            national_ids = serializer.validated_data.get('national_id')
            print(national_ids)
            phone_numbers = [get_phone_number(national_id) for national_id in national_ids]
            sms_calls = [send_sms(phone_number) for phone_number in phone_numbers]
            await asyncio.gather(*sms_calls)
            return HttpResponse(status=200)

    return HttpResponse(status=400)
