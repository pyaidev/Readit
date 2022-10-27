from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .serializer import ArticleSerializer, ArticleGetSerializer
from ..models import Article


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        queryset = Article.objects.all()
        serializer = ArticleGetSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error: Method net allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def article_create(request):
    if request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': "Successfully created", 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'detail': 'credentialed are not valid'}, status=status.HTTP_400_BAD_REQUEST_METHOD)


@api_view(['GET'])
def article_detail(request, pk):
    if request.method == 'GET':
        try:
            queryset = Article.objects.get(id=pk)
        except Exception as e:
            return Response({'detail': f'{e.args}'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ArticleGetSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT','PATCH'])
def article_update(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Exception.Does.Not.Exist:
        return HttpResponse(status=404)
    if request.method=='PUT' or request.method=='PATCH':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def article_delete(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Exception.Does.Not.Exist:
        return HttpResponse(status=404)

    if request.method=='DELETE':
        article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

