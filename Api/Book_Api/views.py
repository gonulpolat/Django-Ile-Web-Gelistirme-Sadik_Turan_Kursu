from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Book_Api.models import Book
from Book_Api.serializer import BookSerializer


def book_list2(request):
    books = Book.objects.all()
    books_list = list(books.values())
    return JsonResponse({
        'books': books_list,
    })


def book_list1(request):
    books = Book.objects.all()
    print(type(books))                   # <class 'django.db.models.query.QuerySet'>
    return JsonResponse({
        'books': [
            {'id':1, 'title':'Kitap 1'},
            {'id':2, 'title':'Kitap 2'},
        ]
    })


###############################################################################################################


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    


@api_view(['GET', 'POST'])
def books(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

###############################################################################################################


@api_view(['GET'])
def book_get(request, id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        content = {"error": "Eşleşen bir kayıt bulunamadı."}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def book_update(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['DELETE'])
def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    # return Response({'delete': True})
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def book(request, id):
    try:
        book = Book.objects.get(pk=id)
    except:
        content = {"error": "Eşleşen bir kayıt bulunamadı."}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    