from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Tasks, TascsUAccount


class TaskSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = TascsUAccount
        fields = ('name', 'lastname', 'Uemail', 'residence', 'country_of_origin', 'password1', 'password2')
        depth = 1

    def create(self, validated_data):
        Uemail = self.validated_data['Uemail']
        lastname = self.validated_data['lastname']
        name = self.validated_data['name']
        residence = self.validated_data['residence']
        country_of_origin = self.validated_data['country_of_origin']
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        # photo = self.validated_data['photo']

        if password1 != password2:
            return Response({"Message": "Passwords Dont match Correct this"})

        tascsuser = TascsUAccount(lastname=lastname, name=name, password=password1,
                                  Uemail=Uemail,
                                  country_of_origin=country_of_origin,
                                  residence=residence)
        tascsuser.save()
        uname = str(lastname) + ' ' + str(name)
        user = User(email=Uemail, username=uname)
        user.set_password(password2)
        user.save()
        Token.objects.create(user=user)

        return tascsuser
