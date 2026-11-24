# Evidências de validação — [US1]

Estado: PENDENTE / EM_EXECUCAO / APROVADA / FALHOU / BLOQUEADA
Executor/ferramenta: [identificação]
Data/hora e fuso: [valor]
Commit: [hash]
Alterações não commitadas: [nenhuma ou diff preservado + hash do diff/artefato]
Ambiente, versões e dados: [detalhes e referências reproduzíveis]

| Execução | Critério/cenário | Comando ou procedimento e diretório | Esperado | Observado | Resultado | Log/artefato |
|---|---|---|---|---|---|---|
| RUN-01 | [IDs] | [exato] | [asserções] | [resultado real] | NÃO EXECUTADO | [referência ou motivo] |

Resultados permitidos: PASSOU, FALHOU, NÃO EXECUTADO. Registrar código de saída
quando houver e resultados das asserções; exit code zero sozinho pode ser insuficiente.

## Cobertura e limitações

- Critérios cobertos e ausentes:
- Integrações reais versus simuladas:
- Cenários não executados, motivo, impacto e próximo passo:
- Regressão executada:

## Rodadas após correções

[Preservar falhas anteriores. Identificar nova versão, testes repetidos e resultado.]

Somente marcar APROVADA quando todos os cenários exigidos passaram na versão
indicada. Não colar saída inventada. Remover segredos dos artefatos preservando
o necessário para comprovação. Decisões de exceção ficam no registro humano.

## Identificação do incremento e histórico

- PR previsto ou URL real: [não inventar URL de PR ainda inexistente]
- História e critérios cobertos: [IDs; cobertura parcial ou final]
- Base resolvida: [hash]
- Versão candidata: [hash e diff/artefato das alterações locais]
- Predecessores e ordem: [IDs ou nenhum]
- Escopo desta evidência: INCREMENTO / HISTORIA_INTEGRADA
- Nova rodada após correção ou mudança de base: [impacto, execuções e revisão renovadas]

Registros podem ser separados por PR ou conter rodadas identificadas no mesmo
arquivo. Manter índice por história; não sobrescrever falhas nem perder as bases.

## Condições verificáveis

Aplicar policies/PASSAGENS.md do preset instalado. Referenciar saídas de execução
reais e a revisão atual; presença de arquivo não comprova aprovação. Registrar
impeditivos, correções e revalidação. Exceções exigem condição, risco, escopo,
responsável, data, versão, decisão atribuível e ação posterior; nunca converter
NÃO EXECUTADO em PASSOU. Aprovação humana deve apontar a fonte real da decisão.

## Execução real do produto

- Versão e ambiente:
- Meio: UI / API / INTEGRACAO / MENSAGEM / JOB / CLI / BIBLIOTECA
- Inicialização e entrada exata:
- Resultado esperado e asserções:
- Resultado observado e efeitos:
- Evidência: logs, resposta, consulta, captura ou trace adequado:
- Depuração usada, se aplicável, e valores observados:
- Limites de simulação e cenários não executados:

Usar também product-execution-template.json para vincular essa execução aos gates.
Um teste automatizado pode comprovar o fluxo se efetivamente o executar; indicar
como a entrada e as asserções correspondem ao uso real.
