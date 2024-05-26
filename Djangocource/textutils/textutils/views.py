#I have created this file- Wasim Akram 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #Get the text 
    djtext=request.POST.get('text','default')

    #check checkbox value 
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    #Check which check box is on 
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        word_list = djtext.split()  # Split the input text into a list of words
        for word in word_list:
        # Remove punctuation from each word
            cleaned_word = "".join(char for char in word if char not in punctuations)
            analyzed += cleaned_word + " "  # Add a space after each cleaned word
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed


    
    elif (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Upper Case', 'analyzed_text':analyzed}
        djtext=analyzed
    
    elif (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !='\r':
                analyzed=analyzed+char
        params={'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext=analyzed
    
    
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext[:-1]):
            if not (char == " " and djtext[index + 1] == " "):
                analyzed += char


        params = {'purpose': 'Removed extraspaces', 'analyzed_text': analyzed}
        djtext=analyzed

    if removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on":
        return HttpResponse("Please select any operation")
    return render(request, 'analyze.html', params)
