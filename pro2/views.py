from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request , 'index.html')

def analyze(request):
    # return HttpResponse('<h1>Hello! How are you?</h1>')
    djtext = request.GET.get('text' , 'no value had given')
    removepunc = request.GET.get('removepunc' , 'Off')
    removenewline = request.GET.get('removenewline' , 'Off') 
    spaceremover = request.GET.get('spaceremover' , 'Off')
    charcount = request.GET.get('charcount' , 'Off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'\\'",<>./?@#$%|^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'removepunc':'removing punctuations' , 'analyzing':analyzed}
        djtext = analyzed           
    if(removenewline == "on"):
        analyzed = ""
        for char in djtext:
            if(char!='\n' and char!='\r'):
                analyzed+=char
        params = {'removepunc':'removing new lines' , 'analyzing':analyzed}
        djtext = analyzed
    if(spaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params = {'removepunc':'removing extra spaces' , 'analyzing':analyzed}
        djtext = analyzed
    if(charcount == "on"):
        i=0
        for char in djtext:
            i+=1
        analyzed = i
        params = {'removepunc':'counting characters' , 'analyzing':analyzed}

    if(charcount != "on" and spaceremover != "on" and removenewline != "on" and removepunc != 'on'):
        return HttpResponse('error')
    return render(request , 'Removepunc.html' , params) 
    
