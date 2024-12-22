from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Article, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core import serializers
from .serializers import ArticleSerializer, ArticleDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

class ArticleListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
    tags=["Articles"],
    description="Article 목록 조회를 위한 API",
    )
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    @extend_schema(
    tags=["Articles"],
    description="Article 생성을 위한 API",
    request=ArticleDetailSerializer,
    )
    def post(serlf, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ArticleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        # user=request.user
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(
            article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, article_pk):
        article=get_object_or_404(Article, pk=article_pk)
        comments=article.comments.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, article_pk):
        article=get_object_or_404(Article, pk=article_pk)
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, comment_pk):
        comment=get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, comment_pk):
        comment=get_object_or_404(Comment, pk=comment_pk)
        serializer=CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)