# Para acrescentar mais um campo de armazenar dados

> Camada interna da arquitetura
1. Acrescentar no DTO (adicionando campo status)

```py

class EstampagensDto(object):
    iniciado: datetime 
    concluido: datetime
    tipo: Placas
    status: str

    def to_dto(self, estampagens: Estampagens):
        estoque_dto = self.tipo.to_dto(estampagens.customer)
        estampagens_dto = EstampagensDto(
            iniciado=estampagens.iniciado, 
            concluido=estampagens.concluido, 
            tipo=estoque_dto,
        )
        estampagens_dto.status = estampagens.status.name
        estampagens_dto.id = estampagens.id
        return estampagens_dto

```

> Para transformar em DTO e chegar no repositorio, para que eu salve a informação "status"...

Esse campo que foi adicionado na camadas interna, adicionar na camada externa também, ou seja, em seguida

2. Adicionar este campo ao models do Django

3. Editar o repositorio para armazenar o valor status

```py

    def _estampagens_dto_to_model(self, estampagemDto: EstampagensDto):
        estampagem = Estampagens()
        estampagem.iniciado = estampagemDto.iniciado
        estampagem.concluido = estampagemDto.concluido
        estampagem.status = estampagemDto.status

        return estampagem
        
```