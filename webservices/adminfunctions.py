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
from django.db.models import Q

import random
import hashlib
import socket
import sys
import traceback
import json

class ProcessFiles(generics.ListAPIView):
    def get(self, request, file_type, pk=None, format=None):
        try:
            file_type_arr = ['song','podcast','audiobook']

            if file_type not in file_type_arr:
                raise Exception("Invalid file type provided.")

            if file_type=='song':
                model = apps.get_model('webservices','Song')

            elif file_type=='podcast':
                model = apps.get_model('webservices','Podcast')

            elif file_type=='audiobook':
                model = apps.get_model('webservices','Audiobook')

            rs_file = model.objects
            if pk!="" and pk!=None:
                rs_file = rs_file.filter(id = pk)
            
            if rs_file.count()>0:
                rs_file = rs_file.values().order_by('-id').all()
                
                str_status = HTTP_200_OK
                data = {
                    'status':str_status,
                    'data' : rs_file,
                    'message': "Success"
                }
                
            else:
                str_status = HTTP_204_NO_CONTENT
                data = {
                    'status':HTTP_204_NO_CONTENT,
                    'message': 'No data found.',
                    'data':[]
                }


        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status)

    def post(self, request, file_type, format=None):
        try:
            request_data =  request.data
            file_type_arr = ['song','podcast','audiobook']

            if file_type not in file_type_arr:
                raise Exception("Invalid file type provided.")

            if request_data['name']:
                name = request_data['name']
            else:
                raise Exception("Name Not Provided.")

            if request_data['duration']:
                duration = request_data['duration']
            else:
                raise Exception("Duration Not Provided.")

            if file_type=='podcast':
                if request_data['host']:
                    host = request_data['host']
                else:
                    raise Exception("Host Not Provided.")

                if request_data['participants']:
                    participants = request_data['participants']
                else:
                    participants = []

            if file_type=='audiobook':
                if request_data['author']:
                    author = request_data['author']
                else:
                    raise Exception("Author Not Provided.")

                if request_data['narrator']:
                    narrator = request_data['narrator']
                else:
                    raise Exception("Narrator Not Provided.")

            
            file_data = {
                'name':name,
                'duration_in_sec':duration
            }
            if file_type=='song':
                model = apps.get_model('webservices','Song')

            elif file_type=='podcast':
                file_data['host'] = host
                file_data['participants'] = participants
                model = apps.get_model('webservices','Podcast')

            elif file_type=='audiobook':
                file_data['author'] = author
                file_data['narrator'] = narrator
                model = apps.get_model('webservices','Audiobook')

            rs_file = model.objects.create(**file_data)
            file_id = rs_file.id

            if file_id:
                str_status = HTTP_200_OK
                data = {
                    'status':str_status,
                    'data' : file_id,
                    'message': "Success"
                }
            else:
                str_status = HTTP_204_NO_CONTENT
                data = {
                    'status':str_status,
                    'message': 'No data found.',
                    'data':0
                }
        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status) 

    def put(self, request, file_type, pk, format=None):
        try:
            request_data =  request.data
            file_type_arr = ['song','podcast','audiobook']

            if file_type not in file_type_arr:
                raise Exception("Invalid file type provided.")

            if request_data['name']:
                name = request_data['name']
            else:
                raise Exception("Name Not Provided.")

            if request_data['duration']:
                duration = request_data['duration']
            else:
                raise Exception("Duration Not Provided.")

            if file_type=='podcast':
                if request_data['host']:
                    host = request_data['host']
                else:
                    raise Exception("Host Not Provided.")

                if request_data['participants']:
                    participants = request_data['participants']
                else:
                    participants = []

            if file_type=='audiobook':
                if request_data['author']:
                    author = request_data['author']
                else:
                    raise Exception("Author Not Provided.")

                if request_data['narrator']:
                    narrator = request_data['narrator']
                else:
                    raise Exception("Narrator Not Provided.")

            
            file_data = {
                'name':name,
                'duration_in_sec':duration
            }
            if file_type=='song':
                model = apps.get_model('webservices','Song')

            elif file_type=='podcast':
                file_data['host'] = host
                file_data['participants'] = participants
                model = apps.get_model('webservices','Podcast')

            elif file_type=='audiobook':
                file_data['author'] = author
                file_data['narrator'] = narrator
                model = apps.get_model('webservices','Audiobook')

            rs_file = model.objects.filter(id = pk)
            if rs_file.count()>0:
                rs_file.update(**file_data)
                file_id = pk

                str_status = HTTP_200_OK
                data = {
                    'status':str_status,
                    'data' : file_id,
                    'message': "Success"
                }
                
            else:
                str_status = HTTP_204_NO_CONTENT
                data = {
                    'status':HTTP_204_NO_CONTENT,
                    'message': 'No data found.',
                    'data':0
                }
        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status) 

    def delete(self, request, file_type, pk, format=None):
        try:
            file_type_arr = ['song','podcast','audiobook']

            if file_type not in file_type_arr:
                raise Exception("Invalid file type provided.")

            if file_type=='song':
                model = apps.get_model('webservices','Song')

            elif file_type=='podcast':
                model = apps.get_model('webservices','Podcast')

            elif file_type=='audiobook':
                model = apps.get_model('webservices','Audiobook')

            rs_file = model.objects.filter(id = pk)
            if rs_file.count()>0:
                rs_file.delete()
                
                str_status = HTTP_200_OK
                data = {
                    'status':str_status,
                    'data' : pk,
                    'message': "Success"
                }
                
            else:
                str_status = HTTP_204_NO_CONTENT
                data = {
                    'status':HTTP_204_NO_CONTENT,
                    'message': 'No data found.',
                    'data':0
                }


        except Exception as error:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            str_status = status.HTTP_417_EXPECTATION_FAILED
            data = {"status": str_status, "api_status": traceback.format_exc(), "error_line": line, "error_message": str(error),"message": str(error)}        
        return Response(data,str_status)

