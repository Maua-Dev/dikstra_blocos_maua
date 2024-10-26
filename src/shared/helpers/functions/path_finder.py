def path_finder(graph: dict[str, dict[str, int]], start: str, end: str) -> list[str]:
    """
    Função para encontrar o caminho mais curto de um ponto inicial a um ponto final em um grafo bidirecional usando o algoritmo de Dijkstra.
    
    Parâmetros:
    - graph (dict[str, dict[str, int]]): O grafo representado como um dicionário. 
        - A chave do dicionário é o nome do vértice (str).
        - O valor é um outro dicionário onde as chaves são os vértices adjacentes e os valores são os pesos das arestas (distâncias).
    - start (str): O vértice de início do caminho (ponto de partida).
    - end (str): O vértice de destino do caminho (ponto de chegada).
    
    Retorno:
    - list[str]: Uma lista que representa o caminho mais curto do ponto de partida ao ponto de chegada, 
                 incluindo os vértices intermediários e o destino. Caso não exista um caminho, retorna uma lista vazia.
    """
    # Passo 1: Inicializar as distâncias e o dicionário de predecessores
    distances = {}  # Armazena a menor distância conhecida de cada vértice até o ponto inicial.
    predecessors = {}  # Armazena o predecessor de cada vértice para reconstruir o caminho.
    
    # Passo 2: Inicializar a lista de vértices não visitados
    unvisited = set(graph.keys())
    
    # Passo 3: Definir a distância do ponto inicial como 0 e as demais como infinito
    for vertex in unvisited:
        distances[vertex] = float('inf')
    distances[start] = 0
    
    # Passo 4: Iterar até que todos os vértices tenham sido visitados ou que o destino tenha sido alcançado
    while unvisited:
        # Escolher o vértice com a menor distância conhecida
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        # Se o vértice atual é o destino, termina a busca
        if current_vertex == end:
            break
        
        # Se a menor distância é infinita, significa que os vértices restantes são inacessíveis
        if distances[current_vertex] == float('inf'):
            break
        
        # Passo 5: Atualizar as distâncias dos vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            if neighbor in unvisited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
        
        # Marcar o vértice atual como visitado
        unvisited.remove(current_vertex)
    
    # Passo 6: Reconstruir o caminho do ponto inicial ao ponto final
    path = []
    current_vertex = end
    while current_vertex in predecessors:
        path.insert(0, current_vertex)
        current_vertex = predecessors[current_vertex]
    
    # Se chegamos ao ponto inicial, adicionar ele ao caminho
    if path and current_vertex == start:
        path.insert(0, start)
    
    # Retornar o caminho encontrado ou uma lista vazia se não houver caminho
    return path if path else []
