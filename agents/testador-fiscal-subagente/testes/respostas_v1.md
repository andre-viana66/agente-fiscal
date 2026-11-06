## T1

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Incorreta
* Diagnóstico da Rejeição / Regra Fiscal: Na devolução, a tributação deve espelhar a nota original. O CST não é fixo: depende do regime do emitente e de como a mercadoria entrou. CST 00 só vale se a nota original foi tributada integralmente, sem ST, sem redução de base e com emitente do Regime Normal (CRT 3). Se o emitente for do Simples (CRT 1/4), usa-se CSOSN (em geral 900), não CST. A NF-e de devolução exige finNFe = 4 e a chave da nota original referenciada (refNFe). Quanto ao CFOP: para devolução de compra para comercialização, 5202/6202 (5411/6411 se houver ST).

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Emitir NF-e com finalidade "Devolução", referenciar a chave da nota original e replicar CST/CSOSN, base e alíquotas dela, proporcionalmente à quantidade devolvida. O caminho de tela exato deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: MOC da NF-e (finNFe = 4 e grupo NFref); Ajuste SINIEF 07/05; tabela CST/CSOSN do Convênio s/nº de 1970 (Anexo).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Corrigir a resposta: "CST 00" não pode ser afirmado sem dados.
* Pedir ao cliente: o regime (CRT), se é devolução de compra ou de venda, a chave/XML da nota original e se a nota original teve ST ou redução de base.
* A tabela base_produtos (Supabase) não pôde ser consultada (não há chave de API configurada), então não há complemento por produto.

### 5. Alertas Internos para o Agente Principal
* CST divergente da nota original gera inconsistência no crédito ou débito de ICMS.
* Recomendar validação com o contador do cliente.

## T2

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Parcialmente Correta
* Diagnóstico da Rejeição / Regra Fiscal: O Lucro Presumido é Regime Normal (CRT 3), então o certo é usar CST. CST 60 com CFOP 5405 está correto quando a empresa é **substituída**, ou seja, revende mercadoria comprada com o ICMS-ST já retido. Se a empresa for **substituta** (indústria, importador ou responsável pela retenção), o correto é CST 10 com CFOP 5401 (produção própria) ou 5403 (mercadoria de terceiros). Em operação interestadual, os CFOPs passam para 6xxx. Lembrar que o CST no XML é composto pela origem + 2 dígitos (ex.: 0 + 60).

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Configurar a tributação do produto com CST 60 e CFOP 5405 (cenário substituído) ou CST 10 e CFOP 5401/5403 (cenário substituto), além do CEST correspondente ao NCM. O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e / SEFAZ da UF do cliente
* Fundamento: Tabela CST do ICMS; Convênio ICMS 142/2018 (ST e CEST); Tabela CFOP (Convênio s/nº 1970).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Manter CST 60 + CFOP 5405 somente se o cliente compra o produto com ST retido pelo fornecedor.
* Confirmar a UF do cliente, se a operação é interna ou interestadual, e se o produto está sujeito à ST naquela UF.
* A base_produtos não pôde ser consultada (sem chave de API).

### 5. Alertas Internos para o Agente Principal
* A ST varia por UF e por produto (protocolos e convênios). Validar com o contador.
* Informar o CEST é obrigatório quando o produto consta do Conv. 142/18 (risco de rejeição).

## T3

### 1. Parecer Técnico
* Status da Dúvida: Resolvida
* Avaliação da Resposta Prévia: Parcialmente Correta
* Diagnóstico da Rejeição / Regra Fiscal: CFOP 1102 (compra para comercialização, operação interna) está correto se o item for revenda. Para fornecedor de outra UF, usar 2102. Para uso e consumo, 1556/2556; para industrialização, 1101/2101. Para um emitente do Simples (CRT 1), o CSOSN 400 ("não tributada pelo Simples Nacional") é o código usado para isenção. Ressalva: na escrituração de uma entrada de compra, o código fiscal que vale é o informado pelo fornecedor no XML. O cliente não "escolhe" o CSOSN da compra, e o regime do fornecedor pode trazer CST 40 em vez de CSOSN.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Lançar a nota de entrada (importação do XML ou lançamento manual), conferir o CFOP de entrada conforme a finalidade (1102/2102) e manter a tributação conforme o XML do fornecedor. O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: Tabela CFOP (Convênio s/nº 1970); tabela CSOSN (Ajuste SINIEF 03/2010); LC 123/2006.

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Confirmar que a mercadoria é para revenda e que o fornecedor é da mesma UF (senão, usar 2102).
* Acrescentar que o CST/CSOSN da entrada segue o XML do fornecedor.
* A base_produtos não pôde ser consultada (sem chave de API).

### 5. Alertas Internos para o Agente Principal
* A isenção precisa ter previsão na legislação da UF. Se ela não existir, a saída posterior pode ser tributada.
* Validar com o contador.

## T4

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Parcialmente Correta
* Diagnóstico da Rejeição / Regra Fiscal: CFOP 1202 (devolução de venda de mercadoria adquirida de terceiros, operação interna) está correto para revenda. Ajustes conforme o caso:
  * 2202 se o cliente que devolve é de outra UF.
  * 1201/2201 se a mercadoria é de produção própria.
  * 1411/2411 se a venda original foi com ST (CFOP 5405).

  CSOSN 900 é aceito na devolução do Simples, principalmente quando é preciso destacar ICMS. A orientação técnica, porém, é espelhar a tributação da venda original (ex.: venda com 102 ou 500). Quem emite também importa: se o comprador for contribuinte com NF-e, ele emite a devolução e a empresa só registra a entrada. Se for consumidor ou não contribuinte, a própria empresa emite a NF-e de entrada, com finNFe = 4 e a chave da NF-e/NFC-e original referenciada.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Emitir a NF-e de entrada com finalidade "Devolução", referenciar a chave original e usar o CFOP 1202 (ou a variação aplicável). Copiar o CSOSN da venda original ou usar 900. O caminho de tela deve ser confirmado na Wiki Interna. Para NFC-e, verificar o artigo "Nota de estorno para NFC-e no App".
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: MOC NF-e (finNFe/NFref); Tabela CFOP; Ajuste SINIEF 03/2010 (CSOSN).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Confirmar: houve ST na venda original? O devolvente é de outra UF? O documento original é NF-e ou NFC-e? Quem emite a devolução?
* A base_produtos não pôde ser consultada (sem chave de API).

### 5. Alertas Internos para o Agente Principal
* Ao usar CSOSN 900 com destaque, os valores devem ser proporcionais aos da nota original.
* Validar com o contador.

## T5

### 1. Parecer Técnico
* Status da Dúvida: Resolvida
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: CST 90 ("Outras") é residual. Só se usa quando nenhum outro CST (00, 10, 20, 30, 40, 41, 50, 51, 60, 70) descreve a operação. Vale apenas para o Regime Normal (CRT 3). O Simples usa o equivalente CSOSN 900. Usos típicos:
  * operações com tratamento específico previsto na legislação estadual (ex.: crédito presumido, regimes especiais);
  * algumas remessas, retornos e devoluções cuja tributação não se encaixa nos demais códigos;
  * casos em que a UF orienta expressamente o uso do CST 90.

  Não deve ser usado como "coringa" para evitar a classificação correta.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Configurar CST 90 na tributação do produto ou da operação apenas quando o contador confirmar o enquadramento, preenchendo base, alíquota e valor de ICMS quando houver. O caminho de tela deve ser confirmado na Wiki Interna.

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: Tabela B do CST (Anexo do Convênio s/nº 1970, redação do Ajuste SINIEF 20/2012); MOC NF-e (grupo ICMS90).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Responder que o CST 90 é residual e exclusivo do Regime Normal.
* Pedir o contexto da operação do cliente para indicar o CST específico, se houver.

### 5. Alertas Internos para o Agente Principal
* O uso indevido do CST 90 é apontado em fiscalização e cruzamento de dados (EFD).
* Validar com o contador.

## T6

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: Sem o regime não é possível definir o código. Simples ou MEI (CRT 1/4) usam CSOSN; Lucro Real ou Presumido (CRT 3) usam CST. O regime pode ser confirmado no cadastro fiscal da empresa ou no XML de qualquer nota emitida (tag emit/CRT). Para devolução de compra com ST:
  * CFOP 5411/6411.
  * No Regime Normal, normalmente CST 10, com devolução do ICMS-ST destacado na nota original.
  * No Simples, CSOSN 900, para permitir o destaque do ICMS e do ICMS-ST.

  Em todos os casos é preciso finNFe = 4, a chave original referenciada e valores proporcionais aos da nota de compra.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: 1) Confirmar o CRT no cadastro da empresa. 2) Emitir a NF-e de devolução com CFOP 5411/6411, referenciando a chave original. 3) Replicar a base de cálculo de ST e o valor de ST da nota original, proporcionalmente. O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e / SEFAZ da UF do cliente
* Fundamento: MOC NF-e; Tabela CFOP; Convênio ICMS 142/2018 (ST).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Pedir o CRT (ou o XML de uma nota emitida), a chave da nota original e a UF do fornecedor.
* A base_produtos não pôde ser consultada (sem chave de API).

### 5. Alertas Internos para o Agente Principal
* O tratamento do ressarcimento de ST na devolução varia por UF.
* Validação contábil obrigatória antes da emissão.

## T7

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: Não existe um "CST de devolução": o código espelha a nota original. Para definir, são necessários:
  1. O tipo: devolução de **compra** (saída, CFOP 5202/6202 ou 5411/6411 com ST) ou de **venda** (entrada, CFOP 1202/2202 ou 1411/2411 com ST).
  2. O regime (CRT): CST para o Regime Normal, CSOSN para Simples/MEI.
  3. A nota original (chave/XML), que é obrigatória no grupo NFref e da qual vêm o CST e os valores.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Com os dados acima, emitir NF-e com finalidade "Devolução", referenciando a chave original e espelhando a tributação dela. O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: MOC NF-e (finNFe = 4, NFref); Tabela CFOP; tabelas CST/CSOSN.

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Não indicar CST agora. Solicitar ao cliente os 3 dados acima. O CRT pode ser visto no XML de qualquer nota emitida (emit/CRT).

### 5. Alertas Internos para o Agente Principal
* Indicar um código sem esses dados gera risco de rejeição ou de erro de apuração.

## T8

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Incorreta
* Diagnóstico da Rejeição / Regra Fiscal: CST 00 indica tributação integral e não serve quando a nota original teve crédito parcial. O enquadramento depende da origem do "crédito parcial":
  * **Redução de base de cálculo** na nota original: devolver com CST 20, replicando o percentual de redução (pRedBC).
  * **Fornecedor do Simples com crédito permitido** (CSOSN 101, pCredSN/vCredICMSSN): se o devolvente é do Regime Normal, ele devolve destacando ICMS limitado ao crédito aproveitado, normalmente com CST 90 conforme a orientação da UF.
  * **Devolvente do Simples**: usa CSOSN 900, com destaque proporcional ao crédito.

  Em qualquer caso, a base e o ICMS devem ser proporcionais à quantidade devolvida.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Emitir NF-e de devolução (finNFe = 4) referenciando a chave original e ajustar o CST (20/90) ou o CSOSN 900, a base reduzida e a alíquota conforme a nota original. O caminho de tela deve ser confirmado na Wiki Interna.

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e / SEFAZ da UF do cliente
* Fundamento: Tabela CST; LC 123/2006, art. 23 (crédito do Simples); legislação da UF sobre redução de base.

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Corrigir: não indicar CST 00.
* Pedir o XML da nota original (verificar pRedBC ou pCredSN) e o regime do cliente.
* A base_produtos não pôde ser consultada (sem chave de API).

### 5. Alertas Internos para o Agente Principal
* Estornar crédito acima do aproveitado gera divergência na EFD.
* Validação contábil obrigatória.

## T9

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: A tabela base_produtos não pôde ser consultada (sem chave de API configurada). A referência vem da legislação:
  * **NCM:** 2203.00.00 (cervejas de malte). Cerveja sem álcool usa 2202.91.00.
  * **CEST:** 03.021.00 (cerveja), 03.022.00 (cerveja sem álcool) e 03.023.00 (chope), conforme o Anexo III do Conv. ICMS 142/2018. Confirmar a descrição exata de cada CEST na versão vigente.
  * **CSOSN, revendedor que compra com ST retido** (cenário comum): 500, com CFOP 5405.
  * **CSOSN, se o cliente for o fabricante** (cervejaria) e responsável pela ST: 201/202, com CFOP 5401.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: No cadastro do produto, informar NCM 22030000, CEST 0302100, CSOSN 500 e CFOP 5405 (cenário de revenda). O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e / SEFAZ da UF do cliente
* Fundamento: TIPI/NCM; Convênio ICMS 142/2018, Anexo III; Ajuste SINIEF 03/2010 (CSOSN).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Confirmar se o cliente é revendedor ou fabricante, se o produto é com ou sem álcool e se é chope.
* Confirmar a UF, pois a ST de bebidas depende do protocolo de cada estado.

### 5. Alertas Internos para o Agente Principal
* Os dados não foram cruzados com a base_produtos.
* O tratamento de PIS/COFINS de bebidas frias pode exigir segregação de receitas no PGDAS-D.
* Validar com o contador.

## T10

### 1. Parecer Técnico
* Status da Dúvida: Requer Informações Adicionais
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: "Fermento" corresponde a mais de um NCM, conforme o tipo:
  * 2102.10.00: leveduras vivas (fermento biológico fresco ou seco).
  * 2102.20.00: leveduras mortas e outros microrganismos monocelulares mortos.
  * 2102.30.00: pós para levedar preparados (fermento químico em pó).

  A tabela base_produtos não pôde ser consultada (sem chave de API configurada), então não houve conferência por produto.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: Após confirmar o tipo, informar o NCM correspondente (sem pontos) no cadastro do produto. O caminho de tela deve ser confirmado na Wiki Interna.

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e (tabela NCM vigente)
* Fundamento: TIPI / Nomenclatura Comum do Mercosul, posição 21.02.

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Perguntar ao cliente se o fermento é biológico ou químico em pó antes de indicar o NCM.

### 5. Alertas Internos para o Agente Principal
* Conferir se o NCM escolhido exige CEST ou ST na UF do cliente.
* Validar com o contador.

## T11

### 1. Parecer Técnico
* Status da Dúvida: Resolvida
* Avaliação da Resposta Prévia: Não Aplicável
* Diagnóstico da Rejeição / Regra Fiscal: A rejeição 778 ("Informado NCM inexistente") ocorre quando o NCM de algum item não consta da tabela NCM vigente usada pela SEFAZ. As causas são: NCM digitado errado, NCM incompleto (diferente de 8 dígitos), NCM em branco ou NCM extinto em atualização da tabela. Um NCM extinto pode ser rejeitado mesmo que notas anteriores com ele tenham sido autorizadas. A nota rejeitada não é autorizada, então a numeração pode ser reaproveitada no reenvio.

### 2. Passo a Passo no Sistema Yooga
* Ajuste Prático: 1) Identificar o item da nota rejeitada. 2) Corrigir o NCM no cadastro do produto (8 dígitos, vigente). 3) Reemitir a nota. O caminho de tela deve ser confirmado na Wiki Interna.
* Link de Referência (opcional): https://ajuda.yooga.com.br/fiscal

### 3. Base Legal / SEFAZ Consultada
* Órgão: Portal Nacional da NF-e
* Fundamento: MOC NF-e (regra de validação 778); tabela NCM vigente (Portal NF-e, Documentos > Diversos).

### 4. Sugestão de Confirmação da Resposta para o Agente Principal
* Não posso redigir a mensagem final para o cliente, pois atuo apenas nos bastidores. Seguem os pontos técnicos para a resposta do Agente Principal:
  * a causa é o NCM inválido ou extinto em algum item;
  * corrigir o NCM no cadastro do produto e reenviar a nota;
  * se o NCM já parecer correto, conferir se ele está vigente na tabela do Portal NF-e.
* Pedir ao cliente o produto ou item afetado, se ele não souber qual é.

### 5. Alertas Internos para o Agente Principal
* Trocar o NCM pode mudar o CEST, a ST e a tributação do produto.
* Recomendar validação com o contador antes de definir o novo NCM.
