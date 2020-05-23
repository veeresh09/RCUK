from rest_framework import serializers
from Rcutting.models import User, RCForm


class Userinfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Rcformviewer(serializers.ModelSerializer):
    class Meta:
        model = RCForm
        fields = '__all__'
