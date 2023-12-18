from rest_framework.response import Response
from rest_framework import generics
from .serializers import urlShortenSerializer
from apps.urls_short.models import Urls, UrlVistors
from apps.urls_short.utils import UrlShortner
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication

class AccessShorUrlView(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    serializer_class = urlShortenSerializer

    def get(self, request, token):
        url = Urls.objects.filter(shortend_url=token).first()
        serializer = urlShortenSerializer(data=url, many=True)
        if url:
            visitors = UrlVistors.objects.filter(url=url).exists()
            if visitors:
                visitors.url = url
                visitors.user = self.request.user
            UrlVistors.objects.create(url=url, user=self.request.user)
            return Response(serializer.data)
        return Response({"error": 'No Matching Url'})


class UrlView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    queryset = Urls.objects.all()
    serializer_class = urlShortenSerializer

                                    

class UrlDetailView(generics.RetrieveDestroyAPIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    queryset = Urls.objects.all()
    serializer_class = urlShortenSerializer
    lookup_field = 'pk'
