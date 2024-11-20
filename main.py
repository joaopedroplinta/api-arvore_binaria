from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from binary_tree import BinaryTree

app = FastAPI()

# Instância da Árvore Binária
binary_tree = BinaryTree()

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get("/")
def read_root():
    return {"message": "API de Árvore Binária"}

@app.post("/insert/{value}")
def insert_value(value: int):
    try:
        binary_tree.insert(value)
        values = binary_tree.in_order_traversal()
        return {"message": f"Valor {value} inserido com sucesso!", "current_values": values}
    except Exception as e:
        return {"message": f"Erro ao inserir valor: {str(e)}"}

@app.get("/search/{value}")
def search_value(value: int):
    result = binary_tree.search(value)
    if result:
        return {"message": f"Valor {value} encontrado!"}
    else:
        return {"message": f"Valor {value} não encontrado!"}

@app.get("/values")
def get_values():
    values = binary_tree.in_order_traversal()  # Você pode usar qualquer método de travessia que retorne os valores
    return {"values": values}


@app.get("/traverse")
def traverse_in_order():
    traversal = binary_tree.in_order_traversal()
    return {"in_order": traversal}

@app.get("/height")
def get_height():
    height = binary_tree.height()
    return {"height": height}

@app.get("/structure")
def get_tree_structure():
    def node_structure(node):
        if node is None:
            return None
        return {
            "value": node.value,
            "left": node_structure(node.left),
            "right": node_structure(node.right)
        }

    return node_structure(binary_tree.root)

@app.delete("/clear")
def clear_tree():
    global binary_tree
    binary_tree = BinaryTree()  # Reinicializa a árvore binária
    return {"message": "Árvore binária limpa com sucesso!"}
