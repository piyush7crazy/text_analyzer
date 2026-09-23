from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Analyzer 
from .serializers import AnalyzerSerializer


@api_view(['POST'])
def create_analyzer_api(request):
    serializer=AnalyzerSerializer(data=request.data)
    t=request.data['text']

    word_cnt = 0              #word_cnt ko badhaya jaise 'Emma' , 'Emily'
    words =t.split()
    for single_word in words:
        word_cnt +=1

    char_cnt = 0         #char_cnt ko badhaya jaise E,m,m,a  E,m.i,l,y
    for letter in t:
        char_cnt +=1


    sent_cnt = 0
    for each in t :
        if each in  ["." , "?" , "!"]:
            sent_cnt +=1

    word_freq={}
    for single_word in words :
        if single_word  in word_freq:
            word_freq[single_word]+=1
        else:
            word_freq[single_word] =1


    if word_cnt == 0:
        word_length = 1
    else:
        word_length = char_cnt / word_cnt

    if sent_cnt == 0:
        sentence_length = 1
    else:
        sentence_length = word_cnt / sent_cnt

    a = 4.71 * word_length
    b = 0.5 * sentence_length
    c = a + b
    read_score = c - 21.43


    if serializer.is_valid():
        serializer.save(word_count=word_cnt , character_count=char_cnt  , sentence_count=sent_cnt , word_frequencies=word_freq , readability_score=read_score)
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_analyzer_api(request):
    a=Analyzer.objects.all()
    serializer=AnalyzerSerializer(a , many=True)
    return Response(serializer.data , status=200)

@api_view(['GET'])
def detail_analyzer_api(request,id):
    a=Analyzer.objects.get(id=id)
    serializer=AnalyzerSerializer(a)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_analyzer_api(request, id):
    a=Analyzer.objects.get(id=id)
    serializer=AnalyzerSerializer(a , data=request.data)
    t=request.data['text']

    word_cnt = 0              #word_cnt ko badhaya jaise 'Emma' , 'Emily'
    words = t.split()
    for single_word in words:
        word_cnt +=1

    char_cnt = 0         #char_cnt ko badhaya jaise E,m,m,a  E,m.i,l,y
    for letter in t:
        char_cnt +=1


    sent_cnt = 0
    for each in t :
        if each in  ["." , "?" , "!"]:
            sent_cnt +=1

    word_freq={}
    for single_word in words :
        if single_word  in word_freq:
            word_freq[single_word]+=1
        else:
            word_freq[single_word] =1

                
    if word_cnt == 0:
        word_length = 1
    else:
        word_length = char_cnt / word_cnt

    if sent_cnt == 0:
        sentence_length = 1
    else:
        sentence_length = word_cnt / sent_cnt

    a = 4.71 * word_length
    b = 0.5 * sentence_length
    c = a + b
    read_score = c - 21.43


    if serializer.is_valid():
        serializer.save(word_count=word_cnt, character_count=char_cnt, sentence_count=sent_cnt, word_frequencies=word_freq, readability_score=read_score)
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)



@api_view(['DELETE'])
def delete_analyzer_api(request , id):
    a=Analyzer.objects.get(id=id)
    a.delete()
    return Response(status=204)