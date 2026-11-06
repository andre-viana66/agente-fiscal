# 📄 Subagente Fiscal - Yooga

## 🎯 Visão Geral
O **Subagente Fiscal** (`subagente-fiscal-yooga`) é um consultor técnico de segundo nível que trabalha nos bastidores para o **Agente Principal**. Ele analisa dúvidas fiscais (SEFAZ Nacional e Estadual, Receita Federal) com o conhecimento de um analista do sistema Yooga e **nunca fala com o cliente final**: tudo o que ele devolve é informação técnica para o Agente Principal confirmar a própria resposta.

## 📁 Estrutura do Repositório
```
agents/
├── subagente-fiscal-yooga/
│   └── agent-v1.md                  # Prompt do subagente fiscal (versão atual)
├── testador-fiscal-subagente/
│   ├── agent.md                     # Agente que testa o subagente fiscal
│   └── testes/
│       ├── respostas_v1.md          # Respostas do subagente nos 11 cenários
│       └── relatorio_testes_fiscal.md
└── fontes/
    └── base_produtos.py             # Junta os CSVs de códigos fiscais em um arquivo único
```

## ⚙️ Principais Responsabilidades
* Analisar as dúvidas fiscais trazidas pelo cliente por meio do Agente Principal.
* Avaliar se a resposta preliminar do Agente Principal está correta e segura.
* Devolver um parecer técnico completo e fundamentado, sem nenhum texto pronto para o cliente.

## 🔍 Fontes de Consulta e Hierarquia
1. **Conhecimento do analista + Wiki Interna:** a Wiki Interna fica com o Agente Principal, que repassa ao subagente o que for necessário. O subagente não acessa nenhuma wiki em disco.
2. **SEFAZ e Receita Federal:** portal nacional da NF-e, SVRS, Receita Federal, SPED e a SEFAZ da UF do cliente, para embasar regras tributárias, rejeições e obrigatoriedades.
3. **Tabela de códigos fiscais (Supabase):** tabela `base_produtos` (445 produtos, 12 categorias) com NCM, CEST, CFOP, CST/CSOSN e campos de IBS/CBS por produto.
4. **Apoio:** a Central de Ajuda (`ajuda.yooga.com.br`) é feita para o cliente. Serve só para confirmar caminhos de tela e como link de referência, nunca como base da análise.

Regras de transparência:
* Pesquisas fora dos domínios permitidos não podem ser usadas.
* A seção 3 informa se a fonte foi **consultada** (página aberta) ou **citada de memória**.
* O link de referência é **obrigatório** e precisa ter sido aberto na análise. Nenhuma URL pode ser inventada.
* Se a base de produtos estiver indisponível, o subagente não inventa códigos e registra isso nos Alertas Internos.

## 📋 Estrutura de Retorno (Output)

### 1. Parecer Técnico
Status da dúvida, avaliação da resposta prévia do Agente Principal e diagnóstico técnico.

### 2. Passo a Passo no Sistema Yooga
Ajuste prático no sistema e **link de referência obrigatório** (artigo da Central de Ajuda ou, se não houver, a página da SEFAZ consultada).

### 3. Base Legal / SEFAZ Consultada
Órgão, fundamento legal ou nota técnica, e se a fonte foi consultada ou citada de memória.

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
Pontos corretos, pontos a ajustar e dados que faltam, em tom técnico e dirigidos ao Agente Principal.

### 5. Alertas Internos para o Agente Principal
Riscos fiscais, ressalvas e lembrete de validação com o contador.

## 🧪 Testes
O `testador-fiscal-subagente` roda 11 cenários (devoluções, ST, CST 90, falta de dados, produtos da base e tentativa de quebrar o guardrail). Ele avalia seções, hierarquia de fontes, guardrail e códigos fiscais. O último resultado está em [`agents/testador-fiscal-subagente/testes/relatorio_testes_fiscal.md`](agents/testador-fiscal-subagente/testes/relatorio_testes_fiscal.md).

## ⚠️ Pendências
* **Acesso à `base_produtos` no n8n:** o workflow ainda precisa de uma ferramenta Supabase com credencial para o subagente consultar a tabela.
* **CSVs de origem:** o `base_produtos.py` espera a pasta `Base de produtos (códigos fiscais)` ao lado dele. Ela não está no repositório, e os dados vivem no Supabase.
