from django.http import HttpResponse
from django.template import loader
from webservices.models import *
from webservices.serializers import *
from django.apps import apps
#import webservices.functions as f1
from django.views import generic
from django.core import serializers
from django.http import JsonResponse

from rest_framework import generics, permissions, status, views, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_204_NO_CONTENT)
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db.models import Q,F,Count,Sum,Avg

import random
import hashlib
import socket
import sys
import traceback
import json


class StudentMarks(generics.ListAPIView):
    def post(self, request, format=None):
        try:
            request_data =  request.data
            
            if 'student' not in request_data.keys():
                raise Exception("Student name not provided.")

            if request_data['student'] and request_data['student']!="" and request_data['student']!=None:
                student = request_data['student']
            else:
                raise Exception("Name Not Provided.")

            if 'marks' not in request_data.keys():
                raise Exception("Student marks not provided.")

            if request_data['marks'] and request_data['marks']!="" and request_data['marks']!=None:
                marks = request_data['marks']
            else:
                raise Exception("Marks Not Provided.")

            studentObj = Students.objects.filter(name__iexact = student,status=1)
            if studentObj.count()>0:
                studentObj = studentObj.values("id").first()
                student_id = studentObj['id']
            else:
                studentObj = Students.objects.create(name = student)
                student_id = studentObj.id

            for obj in marks:
                if 'subject' in obj.keys():
                    subObj = Subjects.objects.filter(id = obj['subject'],status=1)
                    if subObj.count()>0:
                        if 'mark' in obj.keys() and isinstance(obj['mark'],int):
                            markObj = Marks.objects.filter(subject_id = obj['subject'],student_id = student_id)
                            if markObj.count()>0:
                                markObj.update(marks = obj['mark']) 
                            else:
                                Marks.objects.create(subject_id = obj['subject'],student_id = student_id, marks = obj['mark'])
            
            str_status = HTTP_200_OK
            data = {
                'status':str_status,
                'data' : request_data,
                'message': "Success"
            }
        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status) 

    def get(self, request, pk=None, format=None):
        try:
            studentObj = Students.objects.filter(id = pk,status=1)
            if studentObj.count()>0:
                studentname = studentObj.values('name').first()
                marksObj = Marks.objects.filter(student_id = pk).values('marks').annotate(subject_name = F('subject_id__name')).order_by('subject_id').all()
                
                str_status = HTTP_200_OK
                data = {
                    'status':str_status,
                    'student':studentname['name'],
                    'data' : marksObj,
                    'message': "Success"
                }
                
            else:
                str_status = HTTP_204_NO_CONTENT
                data = {
                    'status':HTTP_204_NO_CONTENT,
                    'message': 'No data found.',
                    'student':"",
                    'data':[]
                }


        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status) 

class TotalMarks(generics.ListAPIView):
    def get(self, request, format=None):
        try:
            marksObj = Marks.objects.values('student_id').annotate(student_name = F('student_id__name'), total_marks=Sum('marks')).order_by('-total_marks')
            str_status = HTTP_200_OK
            data = {
                'status':str_status,
                'data' : marksObj,
                'message': "Success"
            }
        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status)

class AverageMarks(generics.ListAPIView):
    def get(self, request, format=None):
        try:
            marksObj = Marks.objects.values('subject_id').annotate(subject_name = F('subject_id__name'), average_marks=Avg('marks')).order_by('-average_marks')
            str_status = HTTP_200_OK
            data = {
                'status':str_status,
                'data' : marksObj,
                'message': "Success"
            }
        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status)