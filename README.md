# Script de Automação de Conexões do LinkedIn (Propósito Educacional)

Este script Python (`linkedin_selenium.py`) foi desenvolvido puramente para **fins educacionais**, demonstrando como a automação web pode ser alcançada usando Selenium. Ele automatiza o processo de envio de solicitações de conexão no LinkedIn.

**Aviso:** Este script destina-se ao aprendizado e à compreensão dos princípios de automação web. Por favor, use-o de forma responsável e em conformidade com os Termos de Serviço do LinkedIn. O uso indevido de ferramentas de automação pode levar a restrições de conta ou outros problemas. O autor não se responsabiliza por qualquer uso indevido.

## Funcionalidades

-   **Login Automatizado:** Utiliza cookies pré-salvos (`cookies.json`) para fazer login no LinkedIn, ignorando o login manual.
-   **Navegação para Minha Rede:** Vai automaticamente para a página "Minha Rede".
-   **Envio de Solicitações de Conexão:** Identifica e clica nos botões "Conectar" para conexões sugeridas.
-   **Conexões Configuráveis:** Permite definir o número de conexões a serem enviadas.
-   **Atraso de Tempo:** Inclui um atraso configurável entre as tentativas de conexão para simular o comportamento humano e reduzir o risco de detecção.

## Pré-requisitos

Antes de executar este script, certifique-se de ter o seguinte instalado:

-   Python 3.x
-   `pip` (gerenciador de pacotes Python)

## Instalação

1.  **Clone este repositório (ou baixe os arquivos):**

    ```bash
    git clone <url_do_repositorio>
    cd <diretorio_do_repositorio>
    ```

2.  **Instale os pacotes Python necessários:**

    ```bash
    pip install selenium webdriver-manager
    ```

3.  **Prepare `cookies.json`:**

    Este script depende de um arquivo `cookies.json` para autenticação. Você precisa exportar manualmente seus cookies do LinkedIn do seu navegador e salvá-los em um arquivo chamado `cookies.json` no mesmo diretório do script. Certifique-se de que esses cookies sejam válidos e permitam que você permaneça logado.

    *Como exportar cookies (guia geral - pode variar por navegador):*
    1.  Faça login no LinkedIn em seu navegador.
    2.  Use uma extensão do navegador (por exemplo, "EditThisCookie" para Chrome) para exportar seus cookies.
    3.  Salve o conteúdo JSON exportado em um arquivo chamado `cookies.json`.

## Uso

1.  **Abra `linkedin_selenium.py`** em um editor de texto.
2.  **Ajuste `num_connections_to_send`:** Modifique a variável `num_connections_to_send` no início do script para definir quantas solicitações de conexão você deseja enviar.

    ```python
    num_connections_to_send = 5 # Altere este valor conforme necessário
    ```

3.  **Execute o script:**

    ```bash
    python linkedin_selenium.py
    ```

    O script abrirá uma janela do navegador Chrome, tentará fazer login usando seus cookies, navegará para a página "Minha Rede" e começará a enviar solicitações de conexão.

## Observações Importantes

-   **Compatibilidade do Navegador:** Este script está configurado para usar o Chrome. Certifique-se de ter o Chrome instalado.
-   **`webdriver-manager`:** A biblioteca `webdriver-manager` lida automaticamente com o download e a configuração do executável ChromeDriver correto para a versão do seu navegador.
-   **Tratamento de Erros:** O tratamento básico de erros está incluído, mas o script pode falhar se a estrutura da página do LinkedIn mudar significativamente ou se ocorrerem problemas de rede.
-   **Uso Ético:** Novamente, este projeto é para fins educacionais. Esteja ciente das políticas do LinkedIn e evite automação excessiva que possa ser disruptiva ou levar à sinalização de sua conta.

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório, sugerir melhorias ou relatar problemas. Contribuições são bem-vindas, especialmente aquelas que aprimoram o valor educacional ou a robustez do script dentro dos limites éticos.

## Licença

Este projeto é de código aberto e está disponível sob a [Licença MIT](LICENSE)."# linkedin" 
