Explicação

O dever da infrastructure nesse quesito, é só enviar dados, com o DTO e o MANAGER importado na aplicação do Django

o DTO pegará os dados e enviará para a enteties que é a aplicação que fará toda a verificação e retornar dados ou mensagem.

E em seguida o Manager recebe a resolução da aplicação da entities por meio do DTO, que em seguida retorna uma mensageria

em repositorio, salvamos dados no BD por meio das informações que vem do DTO (DTO pega as informações por meio das nossas aplicação)

Parte do repositorio: coloca na app django, importa no views, depois chama no manager, vai no entities por meio do DTO, e para retornar mensagem manda pro storage