from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='João',  max_length=50)]
    cpf: Annotated[str, Field(description='12345678900',max_length=11)]
    idade: Annotated[int, Field(description= 25, )]
    peso: Annotated[PositiveFloat, Field(description=75.5)]
    altura: Annotated[PositiveFloat, Field(description=1.70)]
    sexo: Annotated[str, Field(description='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description=25)]