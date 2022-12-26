#created by Faizan

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={"name": "faizan", "place": "mars"}
    return render(request,'index.html',params)

def analyze(request):
    #get the text
   # retext=request.GET.get('text',"its default value")
    retext=request.POST.get('text',"its default value")
    removepunctext=request.POST.get('removepunc',"off")
    uppercase=request.POST.get('uppercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount=request.POST.get('charcount','off')
    # print(retext)
    # print(removepunctext)
    #analyze the text
    punctuations='''!@#$%^&*<.>?:";',./}|:([])'",./;:{\|}'''
    if(removepunctext=="on"):
        analyzed="" 
        for char in retext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations','analyzed_text': analyzed}
        retext= analyzed
        #return render(request,'analyze.html', params)
        #return HttpResponse(f"Remove pun <a href='/'>Go to Home</a>")
    if(uppercase=="on"):
        analyzed=""
        for char in retext:
            analyzed =analyzed + char.upper()
        params = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        retext= analyzed
        #return render(request, 'analyze.html',params )
    
    if(newlineremover=='on'):
        analyzed = ""
        for char in retext:
            if char !="\n" and char !='\r':
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        retext= analyzed
        #return render(request,'analyze.html',params)   
    
    if(charcount=='on'):
        lengthoftext = len(retext)
        analyzed = analyzed + f" \nthere are {str(lengthoftext)} in text"
        params={'purpose':'Character Count','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
    
    if(removepunctext !="on" and uppercase !="on" and newlineremover !='on' and charcount !='on'):
        return HttpResponse("error")

    return render(request, 'analyze.html',params)

# def removepunc(request):
#     #get the text
#     retext=request.GET.get('text','default')
#     print(retext)
#     #analyze the text
#     return HttpResponse(f"Remove pun <a href='/'>Go to Home</a>")


# def captilizefirst(request):
#     return HttpResponse("captilize first <a href='/'>Go to Home</a>")


# def newlineremover(request):
#     return HttpResponse("Newline remover <a href='/'>Go to Home</a>")


# def spaceremover(request):
#     return HttpResponse("spaceremover <a href='/'>Go to Home</a>")
















#code of video 6
# def index(request):
#     return HttpResponse("<h1>hello Faizan its index</>")

# def about(request):
#     return HttpResponse("its our about")

# def personalnav(request):
#     return HttpResponse("<a href='https://www.facebook.com'>Click here for facebook</a>")

#lecture of video 7
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return HttpResponse("Home")


# def removepunc(request):
#     return HttpResponse(f"Remove pun <a href='/'>Go to Home</a>")


# def captilizefirst(request):
#     return HttpResponse("captilize first <a href='/'>Go to Home</a>")


# def newlineremover(request):
#     return HttpResponse("Newline remover <a href='/'>Go to Home</a>")


# def spaceremover(request):
#     return HttpResponse("spaceremover <a href='/'>Go to Home</a>")



