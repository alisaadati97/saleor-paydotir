import graphene

from graphene_django import DjangoObjectType
from ...paydotir.models import Paydotir
import requests
import urllib
from django.shortcuts import redirect

class PaydotirType(DjangoObjectType):
    class Meta:
        model = Paydotir

class PaydotirQuery(graphene.ObjectType):
    paydotirs = graphene.List(PaydotirType)

    def resolve_paydotirs(self, info, **kwargs):
        return Paydotir.objects.all()

class CreatePaydotir(graphene.Mutation):
    id = graphene.Int()
    amount = graphene.Int()
    
    username = graphene.String()
    next_url = graphene.String()
    token = graphene.String()

    
    class Arguments:
        
        username = graphene.String()
        amount = graphene.Int()
        
    
    def mutate(self, info,username,amount):
        
    
        api = "test" 
        redirect_url = 'localhost:8000/paydotir/'
        url = 'https://pay.ir/pg/send'

        data = {
                'api':api,
                'amount':amount,
                'redirect':redirect_url
                }

        req = requests.post(url,data=data)
        
        token = req.json()['token']
        paydotir = Paydotir(username=username,amount=amount,token=token )
        paydotir.save()
        redirect_url = 'https://pay.ir/pg/{0}'.format(token)
        
     
        return CreatePaydotir(
            id=paydotir.id,
            username=paydotir.username,
            next_url = redirect_url,
            token=token,
        )

class PaydotirMutation(graphene.ObjectType):
    create_paydotir = CreatePaydotir.Field()