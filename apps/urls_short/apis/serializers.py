from rest_framework import serializers
from apps.urls_short.models import Urls, UrlVistors
from apps.urls_short.utils import UrlShortner



class urlShortenSerializer(serializers.ModelSerializer):




    class Meta:
        model = Urls
        exclude = ('created', 'modified', 'shortend_url')

    def create(self, validated_data):
        short_url = UrlShortner
        url = Urls.objects.create(name=validated_data.get('name'), 
                                  shortend_url = short_url.generate_url(),
                                  creator= self.request.user,
                                  actual_url= validated_data.get('actual_url'))
        return url


class urlVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlVistors
        exclude = ('created', 'modified')
