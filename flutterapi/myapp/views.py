from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#Get Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()  
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#POST Data
@api_view(['POST'])
def post_todolist(request):
    if request.method =='POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
        
    

@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/11
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)
    
    if request.method == 'DELETE':
        delete = todo.delete()
        data ={}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)
    


data = [
    {
        "title":"แล็บท็อปคืออะไร?",
        "subtitle":"แล็บท็อป คือ ปุกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ ในปี 2021",
        "image_url":"https://github.com/mrothai/BasicAPI/blob/main/computer.jpg?raw=true",
        "detail":"เครื่องคำนวณอิเล็กทรอนิกส์โดยใช้วิธีทางคณิตศาสตร์ประกอบด้วยฮาร์ดแวร์ (ส่วนตัวเครื่องและอุปกรณ์) และซอฟต์แวร์ (ส่วนชุดคำสั่ง หรือโปรแกรมที่สั่งให้คอมพิวเตอร์ทำงาน) สามารถทำงานคำนวณผล และเปรียบเทียบค่าตามชุดคำสั่งด้วยความเร็วสูงอย่างต่อเนื่อง และอัตโนมัติ"
    },
    {
        "title":"มาเขียนโปรแกรม",
        "subtitle":"แนะนำการเริ่มต้นเขียนโปรแกรม",
        "image_url":"https://github.com/mrothai/BasicAPI/blob/main/coding.jpg?raw=true",
        "detail":"การเขียนโปรแกรมมีขั้นตอน ดังนี้ 1เขียนคำสั่ง (Coding) คือ ขั้นตอนการเขียนชุดคำสั่งให้ถูกต้องตามโครงสร้างและไวยากรณ์ของแต่ละภาษาโปรแกรม"
    },{
        "title":"Flutter คือ?",
        "subtitle":"Tools สำหรับการออกแบบ",
        "image_url":"https://github.com/mrothai/BasicAPI/blob/main/mobileapp.jpg?raw=true",
        "detail":"Flutter คือ Cross-Platform Framework ที่ใช้ในการพัฒนา Native Mobile Application (Android/iOS) พัฒนาโดยบริษัท Google Inc. โดยใช้ภาษา Dart ในการพัฒนา ที่มีความคล้ายกับภาษา C# และ Java"
    },{
        "title":"Python คือ?",
        "subtitle":"Python ภาษาใหม่",
        "image_url":"https://github.com/mrothai/BasicAPI/blob/main/python.png?raw=true",
        "detail":"ภาษาไพธอน (Python) เป็นภาษาการเขียนโปรแกรมระดับสูง ที่นำข้อดีของภาษาต่างๆ มารวมไว้ด้วยกัน ถูกออกแบบมาให้เรียนรู้ได้ง่าย และมีไวยากรณ์ที่ช่วยให้เขียนโค้ดสั้นกว่าภาษาอื่นๆ มีความสามารถใช้ชนิดข้อมูลแบบไดนามิก จัดการหน่วยความจำอัตโนมัติ"
    },{
        "title":"Docker  คือ?",
        "subtitle":"Docker",
        "image_url":"https://github.com/mrothai/BasicAPI/blob/main/docker.png?raw=true",
        "detail":"แพลตฟอร์มซอฟต์แวร์ที่ช่วยให้คุณสร้าง ทดสอบ และติดตั้งแอปพลิเคชันใช้จริงได้อย่างรวดเร็ว Docker จะบรรจุซอฟต์แวร์ลงไปในหน่วยที่เป็นมาตรฐานเรียกว่า คอนเทนเนอร์ ซึ่งจะมีทุกสิ่งที่ซอฟต์แวร์ต้องใช้ในการเรียกใช้งาน"
    }
]

def  Home(response):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})
    