import graphene
from graphene_django.types import DjangoObjectType

from pacos.models import Paco


class PacoType(DjangoObjectType):
    class Meta:
        model = Paco


class PacoQuery(object):
    pacos = graphene.List(PacoType)
    paco = graphene.Field(PacoType, paco_id=graphene.String())

    def resolve_pacos(self, info, **kwargs):
        # Querying a list
        return Paco.objects.all()

    def resolve_paco(self, info, paco_id):
        # Querying a single question
        return Paco.objects.get(pk=paco_id)


class CreatePacoMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    paco = graphene.Field(PacoType)

    def mutate(self, info, first_name, last_name):
        paco = Paco(first_name=first_name,
                    last_name=last_name)
        paco.save()
        return CreatePacoMutation(paco=paco)


class Query(PacoQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_paco = CreatePacoMutation.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)

