# Junta os CSVs de "Base de produtos (códigos fiscais)" em base-produtos.csv, com a coluna Categoria.
import csv, re
from pathlib import Path

PASTA = Path(__file__).parent / "Base de produtos (códigos fiscais)"
SAIDA = Path(__file__).parent / "base-produtos.csv"

cabecalho, linhas = None, []
for arq in sorted(PASTA.glob("*.csv")):
    categoria = re.search(r"\((.+)\)", arq.stem).group(1).strip()
    with arq.open(encoding="cp1252", newline="") as f:  # arquivos exportados do Excel em ANSI
        leitor = csv.reader(f)
        cab = next(leitor)
        assert cabecalho in (None, cab), f"cabeçalho diferente em {arq.name}"
        cabecalho = cab
        lidas = [[categoria, *l] for l in leitor if any(c.strip() for c in l)]
        linhas += lidas
        print(f"{categoria}: {len(lidas)}")

with SAIDA.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows([["Categoria", *cabecalho], *linhas])
print(f"Total: {len(linhas)} produtos -> {SAIDA.name}")
