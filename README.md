# API Árvore Binária

## Descrição
Esta API fornece funcionalidades para manipulação de árvores binárias, incluindo inserção, remoção, busca e travessia de nós.

## Endpoints

### Inserir Nó
- **URL:** `/api/nodes`
- **Método:** `POST`
- **Descrição:** Insere um novo nó na árvore binária.
- **Corpo da Requisição:**
    ```json
    {
        "valor": "int"
    }
    ```
- **Resposta de Sucesso:**
    - **Código:** `201 Created`
    - **Corpo:**
        ```json
        {
            "mensagem": "Nó inserido com sucesso"
        }
        ```

### Remover Nó
- **URL:** `/api/nodes/{valor}`
- **Método:** `DELETE`
- **Descrição:** Remove um nó da árvore binária.
- **Parâmetros de URL:**
    - `valor`: Valor do nó a ser removido.
- **Resposta de Sucesso:**
    - **Código:** `200 OK`
    - **Corpo:**
        ```json
        {
            "mensagem": "Nó removido com sucesso"
        }
        ```

### Buscar Nó
- **URL:** `/api/nodes/{valor}`
- **Método:** `GET`
- **Descrição:** Busca um nó na árvore binária.
- **Parâmetros de URL:**
    - `valor`: Valor do nó a ser buscado.
- **Resposta de Sucesso:**
    - **Código:** `200 OK`
    - **Corpo:**
        ```json
        {
            "valor": "int",
            "encontrado": true
        }
        ```

### Travessia da Árvore
- **URL:** `/api/nodes/traverse`
- **Método:** `GET`
- **Descrição:** Realiza a travessia da árvore binária.
- **Parâmetros de Query:**
    - `tipo`: Tipo de travessia (`preorder`, `inorder`, `postorder`).
- **Resposta de Sucesso:**
    - **Código:** `200 OK`
    - **Corpo:**
        ```json
        {
            "nós": ["int", "int", ...]
        }
        ```

## Instalação
1. Clone o repositório:
     ```sh
     git clone https://github.com/joaopedroplinta/api-arvore_binaria.git
     ```
2. Instale as dependências:
     ```sh
     cd api-arvore_binaria
     npm install
     ```

## Uso
1. Inicie o servidor:
     ```sh
     npm start
     ```
2. Acesse a API em `http://localhost:3000`.

## Contribuição
1. Faça um fork do projeto.
2. Crie uma nova branch:
     ```sh
     git checkout -b minha-nova-feature
     ```
3. Faça suas alterações e commit:
     ```sh
     git commit -m 'Adiciona nova feature'
     ```
4. Envie para o repositório remoto:
     ```sh
     git push origin minha-nova-feature
     ```
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.