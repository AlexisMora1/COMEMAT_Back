from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone
from .models import *

# Create your views here.

class Course_List_DB(APIView):
    def get(self, request):
        print(request)
        data = [
            {
                'name': 'pedro',
                'saludo': 'hey'
            }
        ]
        return Response(data)
    
    def post(self, request):
        try:
            course = request.data
            try:
                # First lets save the page data of the new course
                cpg = course['page_data']
                # Calculating the current day
                created_at_naive = datetime.today()
                created_at = timezone.make_aware(created_at_naive)
                # Registering the JSON data in the Cursos_Page table
                cpg_register = Cursos_Page(
                                    name = cpg['name'],
                                    created_at = created_at,
                                    image = cpg['image']
                                )
                # Saving the cpg_register
                cpg_register.save()
            except Exception as e: 
                print(e)
                return Response({'status':500,"Error":"Error in page_data format"})
            
            # Now lets save the Course info in its respective table:
            try:
                cinfo = course['course_info']
                # Registering the JSON data in the Curso_info table
                cinfo_register = Curso_info(
                                    course_id = cpg_register,
                                    des = cinfo['des'],
                                    opinions = cinfo['opinions'],
                                    valuation = cinfo['valuation'],
                                    count_mod = cinfo['count_mod'],
                                )
                # Saving the register
                cinfo_register.save()

            except Exception as e:
                print(e)
                return Response({'status':500,"Error":"Error in course data format"})
            
            # Finally we save the modules info:
            try:
                c_modules = course['course_modules']
                # Registering the JSON data in the Curso_info table
                register = Modules(module_id = cinfo_register,
                                    url = c_modules['url'],
                                )
                
                # Saving the register
                register.save()

            except Exception as e:
                print(e)
                return Response({'status':500,"Error":"Error in module data format"})

            return Response({'status':200})
        
        except Exception as e:
            return Response({"status":500,"Error":"Error in POST method"})