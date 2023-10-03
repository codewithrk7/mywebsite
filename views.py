from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
def index(request):
     return render(request,'index.html')


def analyze (request):
     dgtext= request.POST.get('text','default')
     # check checkbox values
     removepunc = request.POST.get('removepunc','off')
     fullcaps = request.POST.get('fullcaps','off')
     newlineremover = request.POST.get('newlineremover','off')
     extraspaceremover = request.POST.get('extraspaceremover','off')
     # charcount = request.GET.get('charcount','off')
     # print(removepunc)

     if removepunc == "on":
          # analyzed = dgtext
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed = ""
          for char in dgtext:
               if char not in punctuations:
                    analyzed = analyzed+char
          params = {'purpose':'removed punctuations','analyzed_text':analyzed}
          dgtext = analyzed
          # return render(request,'analyze.html',params)

     if(fullcaps=="on"):
          analyzed = ""
          for char in dgtext:
               analyzed = analyzed + char.upper()
          params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
          dgtext = analyzed
          # return render(request, 'analyze.html', params)

     if(newlineremover=='on'):
          analyzed = ""
          for char in dgtext:
               if char !="\n" and char!="\r":
                    analyzed = analyzed + char
          params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
          dgtext = analyzed
          # return render(request, 'analyze.html', params)

     if (extraspaceremover=='on'):
          analyzed = ""
          for index, char in enumerate(dgtext):
               if not (dgtext[index] == " " and dgtext[index+1]==" "):
                    analyzed = analyzed + char
          params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
          dgtext = analyzed

     if(removepunc !="on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps!="on"):
          return HttpResponse("Please select and operation and try again")
     return render(request,'analyze.html',params)
