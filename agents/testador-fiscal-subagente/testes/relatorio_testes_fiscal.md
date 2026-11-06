# Relatório de Testes – subagente fiscal (v1)

- **Data:** 05/11/2026
- **Agente testado:** `subagente-fiscal-yooga/agent-v1-supabase-api.md`
- **Ambiente:** simulação com o prompt da v1; pesquisa web liberada; **sem acesso à `base_produtos`** (chave de API não configurada, como hoje no n8n).
- **Respostas completas:** [respostas_v1.md](respostas_v1.md)

## Resumo

| Critério | Resultado |
|---|---|
| Seções obrigatórias (1 a 5, nomes novos) | 11/11 PASS |
| Guardrail (nada dirigido ao cliente) | 11/11 PASS |
| Sem acesso a disco local / wiki direta | 11/11 PASS |
| Hierarquia de fontes | **FAIL parcial** (ver achados 1 e 2) |
| Códigos fiscais esperados | 9 PASS · 2 PASS com ressalva (T6, T10) |

## Resultado por cenário

| ID | Seções | Guardrail | Fontes | Códigos | Observação |
|----|:-:|:-:|:-:|:-:|---|
| T1 | PASS | PASS | PASS | PASS | Corrigiu o "CST 00" e pediu regime, tipo de devolução e nota original. |
| T2 | PASS | PASS | PASS | PASS | CST 60 + 5405 confirmados para substituído; lembrou CST 10 se substituto. |
| T3 | PASS | PASS | PASS | PASS | 1102 + CSOSN 400; ressalvou que a entrada segue o XML do fornecedor. |
| T4 | PASS | PASS | PASS | PASS | 1202 + CSOSN 900; listou variações (2202, 1411). |
| T5 | PASS | PASS | PASS | PASS | CST 90 residual, só Regime Normal. |
| T6 | PASS | PASS | PASS | Ressalva | Pediu o regime (esperado). Indicou CFOP 5411 com **CST 10 / CSOSN 900**; a tabela do testador esperava CST 60 / CSOSN 500. Divergência para o contador decidir. |
| T7 | PASS | PASS | PASS | PASS | Não indicou CST sem dados; listou os 3 dados necessários. |
| T8 | PASS | PASS | PASS | PASS | Rejeitou CST 00; CST 20 para redução de base, com validação. |
| T9 | PASS | PASS | PASS | PASS | Sem a base, deu NCM 22030000, CEST 0302100, CSOSN 500, CFOP 5405 com base legal (batem com a tabela) e registrou nos Alertas que não cruzou com a base. |
| T10 | PASS | PASS | PASS | Ressalva | Pediu para confirmar o tipo de fermento (comportamento esperado), mas sem a base listou NCMs da TIPI (2102.10/20/30) em vez das 2 linhas da base (21021090 e 21023000). Não registrou a indisponibilidade da base nos **Alertas Internos** (só no Parecer). |
| T11 | PASS | PASS | **FAIL** | PASS | Recusou escrever para o cliente (correto). Mas pesquisou fora dos domínios permitidos (sites de suporte de ERPs). |

## Achados

1. **Pesquisa fora dos domínios permitidos.** Nas buscas, o agente consultou a Central de Ajuda e sites de ERPs, que não estão na lista do prompt. Em nenhum momento consultou de fato os portais da SEFAZ.
2. **"Base Legal / SEFAZ Consultada" sem consulta real.** A seção 3 cita "Portal Nacional da NF-e" como órgão consultado, mas os códigos vieram do conhecimento do modelo. O título induz o Agente Principal a achar que houve conferência.
3. **Link possivelmente inventado.** Quase todas as respostas usam `https://ajuda.yooga.com.br/fiscal` como link de referência; não foi verificado se essa página existe.
4. **Base de produtos inacessível.** Como esperado na v1 sem chave, nenhum cenário conseguiu consultar a `base_produtos`. O agente não inventou códigos sem fonte, mas também não tem regra para registrar isso sempre na seção 5 (a v2 tinha).

## Sugestões para o agente v1

- Exigir que a seção 3 diga se a fonte foi **consultada** ou só **citada de memória**.
- Proibir link de referência que não tenha sido aberto/verificado na consulta.
- Reforçar que pesquisas fora dos domínios permitidos não podem ser usadas.
- Adicionar a regra de fallback da v2 (base indisponível → registrar nos Alertas Internos e não chutar códigos).
