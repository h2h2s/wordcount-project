from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordsinsentence = fulltext.split()

    wordsdictionary = {}

    for word in wordsinsentence:
        if word in wordsdictionary:
            wordsdictionary[word] += 1
        else:
            wordsdictionary[word] = 1
    
    sortedwords = sorted(wordsdictionary.items(),key=operator.itemgetter(1), reverse=True)
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordsinsentence),'sortedwords':sortedwords})


def about(request):
    return render(request, 'about.html')