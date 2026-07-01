# Respostas das questões Teóricas

## 1.
* **git merge**: Combina o histórico de duas branches criando um novo commit de junção (merge commit).
  * **Vantagem**: Operação segura e não-destrutiva que preserva o histórico cronológico original.
* **git rebase**: Move ou "reaplica" os commits da branch atual para o topo da branch de destino, reescrevendo o histórico.
  * **Vantagem**: Mantém o histórico do projeto totalmente limpo e linear.

**Cenário prático para Rebase**: Você está desenvolvendo em uma branch `feature-X` e a `main` recebeu atualizações da equipe. Em vez de fazer um merge (gerando um commit de cruzamento desnecessário), você faz um `git rebase main` para alinhar seus commits diretamente no topo da `main` atualizada antes do Pull Request.


## 2. 
* **GET**: Usado apenas para buscar dados. Os parâmetros vão expostos na URL. Não deve alterar o estado do servidor.
* **POST**: Usado para enviar dados que criam ou modificam recursos. Os dados vão embutidos no corpo da requisição, mais seguros.

**Por que usar POST para modificações**: O método GET é indexado, salvo no histórico do navegador e sofre cache. Se uma rota GET deletar ou alterar dados (ex: `/deletar?id=1`), a ação pode ser disparada acidentalmente. O POST garante intencionalidade, segurança e impede o cache da ação.

* **Exemplo apropriado de GET**: Filtragem de produtos por tag (`/produtos?tag=promocao`).
* **Exemplo obrigatório de POST**: Envio de formulário de login (credenciais) ou finalização de uma compra.


## 3.
O request no Flask é um objeto global que armazena todas as informações que o cliente (como um navegador) envia para o servidor durante uma requisição HTTP. Ele serve para o servidor capturar e processar dados de formulários, parâmetros de URL, cabeçalhos e cookies.

## 4.
O request captura dados do cliente: via request.args (URL), request.form (formulários) ou como argumentos da função (rotas dinâmicas). Já as sessões salvam dados no navegador do usuário em cookies assinados pela secret_key para evitar fraudes. Suas limitações são o espaço de 4 KB, a falta de privacidade (o usuário lê os dados) e o gasto de banda por irem em toda requisição