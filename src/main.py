"""
   Trabalho Prático 2 — Grafo do Cavalo (3×3)
   Orientador: Prof. Me Ricardo Carubbi

   Formas de execução:
       python main.py                           # lê ../dados/entrada.txt automaticamente
       python main.py ../dados/entrada.txt      # arquivo explícito
       python main.py < ../dados/entrada.txt    # stdin redirect
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph import Graph
from cc    import CC
from cycle import Cycle
from bfs   import BFS

SEP = "=" * 50

def pos_to_vertex(row, col, cols=3):
    return row * cols + col

def print_separator(title=""):
    if title:
        print("\n" + SEP)
        print("  " + title)
        print(SEP)
    else:
        print(SEP)

def build_graph_from_file(path):
    with open(path) as f:
        V = int(f.readline())
        E = int(f.readline())
        g = Graph(V)
        for _ in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)
    return g

def build_graph_from_stdin():
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Graph(V)
    for _ in range(E):
        v, w = sys.stdin.readline().split()
        g.add_edge(v, w)
    return g

def resolve_input():
    # 1) argumento explícito
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            sys.exit("Arquivo não encontrado: " + path)
        return build_graph_from_file(path)

    # 2) arquivo padrão (permite rodar sem argumento e sem redirect)
    default = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dados", "entrada.txt")
    )
    if os.path.exists(default):
        print("[info] Lendo de " + default + "\n")
        return build_graph_from_file(default)

    # 3) stdin redirect (fallback final)
    if not sys.stdin.isatty():
        return build_graph_from_stdin()

    sys.exit("Uso: python main.py [entrada.txt]  ou  python main.py < entrada.txt")


g = resolve_input()

print_separator("1. Lista de adjacência")
print(g)

print_separator("2. Componentes conexas")
cc = CC(g)
print("Número de componentes conexas: " + str(cc.count()))
for idx, group in enumerate(cc.components(g)):
    print("  Componente " + str(idx) + ": " + " ".join(str(v) for v in group))

print_separator("3. Distância mínima: (0,0) -> (2,2)")
src = pos_to_vertex(0, 0)
dst = pos_to_vertex(2, 2)
bfs = BFS(g, src)
if bfs.has_path_to(dst):
    print("  Distância (em movimentos do cavalo): " + str(bfs.dist_to(dst)))
    print("  Caminho: " + " -> ".join(str(v) for v in bfs.path_to(dst)))
else:
    print("  Não há caminho entre " + str(src) + " e " + str(dst) + " (componentes diferentes).")

print_separator("4. Existência de ciclo")
cyc = Cycle(g)
if cyc.has_cycle():
    print("  O grafo POSSUI ciclo.")
    print()
    print("  Análise de complexidade do algoritmo de detecção:")
    print("    Tempo : O(V + E)  — cada vértice e aresta visitados no máximo uma vez.")
    print("    Espaço: O(V)      — arrays marked e edge_to de tamanho V;")
    print("                        pilha de recursão com profundidade máxima V.")
    print_separator("5. Vértices do ciclo encontrado")
    print("  Ciclo: " + " -> ".join(str(v) for v in cyc.get_cycle()))
else:
    print("  O grafo NÃO possui ciclo.")
    print("    Tempo : O(V + E)")
    print("    Espaço: O(V)")

print_separator()