# I have created this file- Ravi Jain

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse(''' <h1> This is Personal Navigator Assignment</h1>
        Ravi1 <a href='https://www.javatpoint.com/django-model' target="blank"> JT</a>
       <br><br> Ravi2 <a href="https://www.facebook.com" target="blank"> FB</a>
       <br><br> Ravi3 <a href="https://www.cricbuzz.com" target="blank"> Cricbuzz</a>
       <br><br> Ravi4 <a href="https://www.instagram.com" target="blank"> Insta</a>
       <br><br> Ravi5 <a href="https://www.twitter.com" target="blank"> Twitter</a>
    ''')

def home(request):
    # print('hello')
    return render(request,'index2.html')
    # return HttpResponse("This is Home");

def index2(request):
    # print('hello')
    return render(request,'index2.html')
    # return HttpResponse("This is Home");

def analyse(request):
    djText = request.GET.get('text','Ravi Jain')
    print(djText)
    #check Box Values
    removepunc = request.GET.get('removepunc', 'off')
    removespace = request.GET.get('removespace', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    lowercase = request.GET.get('lowercase', 'off')
    newlineremover=request.GET.get('newlineremover','off')
    analyzed = ""
    print(lowercase)
    if removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char  in djText:
            if char not in punc:
                analyzed=analyzed+char
        params={'purpose' :'Remove Pucntuataions' , 'data':djText,'analyzed_text':analyzed}
        return render(request,'analyse2.html',params)
    elif removespace=="on":
        space=" "
        for index in range(0,len(djText)-1):
            if djText[index]==" " and djText[index+1]==" ":
                pass
            else:
                analyzed=analyzed+djText[index]
        params={'purpose':'Remove Spaces' ,'data':djText,'analyzed_text':analyzed}
        return render(request,'analyse2.html',params)
    elif newlineremover=="on":
        for char in djText:
            if char !="\n":
                analyzed=analyzed+char

        params={'purpose':'To New Line Remover', 'data':djText, 'analyzed_text':analyzed }
        return  render(request,'analyse2.html',params)
    elif uppercase=="on":
        print("Hello in Upper")
        for char in djText:
             analyzed=analyzed+char.upper()
        params={'purpose':'To UpperCase', 'data':djText, 'analyzed_text':analyzed }
        return  render(request,'analyse2.html',params)
    elif lowercase == "on":
        for char in djText:
             analyzed=analyzed+char.lower()
        params={'purpose':'To UpperCase', 'data':djText, 'analyzed_text':analyzed }
        return  render(request,'analyse2.html',params)
    # return HttpResponse("Analyze")
    else:
        return HttpResponse("Error Found")
# def removepunc(request):
#     # Get the Text
#     djtext = request.GET.get('text', 'defualt')
#     print(djtext)
#     # render(request,'removepunc')
#     return HttpResponse("This is punc");
# def removespace(request):
#     return HttpResponse("This is space");
#
# def pipeling(request):
#     # render has threee arg  request , page, params i.e dictionary
#     return render(request,'index.html')
#     # return HttpResponse('''Ravi2 <a href="www.facebook.com"> FB</a>''')
