# T2 — Grafo do Cavalo (3×3)

**Disciplina:** Resolução de Problemas com Grafos  
**Orientador:** Prof. Ricardo Carubbi  
**Video** https://youtu.be/I4Onroxqk3o

## Descrição

Este projeto modela os movimentos válidos de um **cavalo de xadrez** em um
tabuleiro **3×3** como um grafo não-direcionado e responde às seguintes
perguntas:

1. Lista de adjacência do grafo.
2. Componentes conexas.
3. Distância mínima (em movimentos) entre a casa (0,0) e a casa (2,2).
4. O grafo possui ciclo? (com análise de complexidade)
5. Quais são os vértices de um ciclo encontrado?

## Estrutura do projeto

```
t2-cavalo/
├── README.md
├── dados/
│   └── entrada.txt          # 9 vértices, 8 arestas do grafo do cavalo 3×3
└── src/
    ├── main.py              # ponto de entrada
    ├── graph.py             # estrutura Graph com lista de adjacência (Bag)
    ├── bag.py               # Bag (inserção no início — ordem LIFO)
    ├── cc.py                # Componentes Conexas (DFS)
    ├── cycle.py             # Detecção de Ciclo (DFS) com reconstrução do caminho
    └── bfs.py               # BFS para distância mínima
```

## Numeração dos vértices

```
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
```

`(linha, coluna) → vértice = linha × 3 + coluna`

## Arestas do grafo do cavalo

As arestas foram construídas manualmente aplicando os deslocamentos
`(±1, ±2)` e `(±2, ±1)` a cada casa do tabuleiro:

| Aresta | Origem | Destino |
|--------|--------|---------|
| 0–5    | (0,0)  | (1,2)   |
| 0–7    | (0,0)  | (2,1)   |
| 1–6    | (0,1)  | (2,0)   |
| 1–8    | (0,1)  | (2,2)   |
| 2–3    | (0,2)  | (1,0)   |
| 2–7    | (0,2)  | (2,1)   |
| 3–8    | (1,0)  | (2,2)   |
| 5–6    | (1,2)  | (2,0)   |

> O vértice 4 (casa central) **não possui arestas**, pois nenhum movimento
> válido do cavalo a partir do centro cabe no tabuleiro 3×3.

## Como executar

```bash
cd src
python main.py < ../dados/entrada.txt
```

## Saída esperada

```
==================================================
  1. Lista de adjacência
==================================================
9 vertices, 8 edges
0: 7 5
1: 8 6
2: 7 3
3: 8 2
4:
5: 6 0
6: 5 1
7: 2 0
8: 3 1

==================================================
  2. Componentes conexas
==================================================
Número de componentes conexas: 2
  Componente 0: 0 1 2 3 5 6 7 8
  Componente 1: 4

==================================================
  3. Distância mínima: (0,0) → (2,2)
==================================================
  Distância (em movimentos do cavalo): 4
  Caminho: 0 → 7 → 2 → 3 → 8

==================================================
  4. Existência de ciclo
==================================================
  O grafo POSSUI ciclo.
  ...

==================================================
  5. Vértices do ciclo encontrado
==================================================
  Ciclo: 0 → 7 → 2 → 3 → 8 → 1 → 6 → 5 → 0
```

## Complexidade dos algoritmos

| Algoritmo          | Tempo    | Espaço |
|--------------------|----------|--------|
| Construção do grafo | O(V + E) | O(V + E) |
| CC (DFS)           | O(V + E) | O(V)   |
| Ciclo (DFS)        | O(V + E) | O(V)   |
| Dist. mínima (BFS) | O(V + E) | O(V)   |
