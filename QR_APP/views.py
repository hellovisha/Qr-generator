from django.shortcuts import render
import qrcode

from base64 import  b64encode
from io import BytesIO
# Create your views here.


def HomePage(request):
    if request.method == "POST":
        memory = BytesIO()
        data = request.POST['link']
         
        print(data)
        img =qrcode.make(data)
       
        img.save(memory)
        memory.seek(0)


        base64_img = "data:image/png;base64," + \
            b64encode(memory.getvalue()).decode('ascii')
        
    
       
        return render (request,'index.html',{'data': base64_img})
    return render(request,'index.html')


