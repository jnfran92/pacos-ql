from pacos.models import Paco

from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType


class PacoNode(DjangoObjectType):

    class Meta:
        model = Paco
        interfaces = (Node, )


class Query(ObjectType):
    paco = Node.Field(PacoNode)
    all_pacos = DjangoConnectionField(PacoNode)


schema = Schema(query=Query)

