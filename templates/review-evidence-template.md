# Code review — [US1]

Estado: PENDENTE / EM_REVISAO / CONCLUIDA / BLOQUEADA
Revisor e ferramenta: [identificação]
Modalidade: AUTORREVISAO / OUTRO_AGENTE / HUMANA
Data/hora e fuso: [valor]
Base do diff: [commit/referência resolvida]
Versão revisada: [commit + identificação de alterações não commitadas]
Diff preservado ou link estável: [referência]
Escopo: [arquivos, critérios de aceite e exclusões]

## Análise dos critérios

| Critério | Código relevante: arquivo/linha | Teste/evidência consultada | Conclusão e limites |
|---|---|---|---|
| [US1-AC01] | [referência] | [referência] | [análise] |

## Achados

| ID | Prioridade/impacto | Arquivo/linha | Problema e evidência | Correção | Situação | Revalidação |
|---|---|---|---|---|---|---|
| [REV-01] | [valor] | [referência] | [descrição] | [referência] | [aberto/resolvido] | [resultado] |

Se nenhum achado for identificado, registrar isso e o escopo realmente examinado;
não inventar achados. Ausência de achados não garante ausência de defeitos.

## Conclusão

- Achados impeditivos ainda abertos:
- Regressões e integrações consideradas:
- Limitações do acesso e análise:
- Versão final confirmada após correções:

Não apresentar autorrevisão como revisão independente. Uma revisão por outro
agente só pode ser registrada se realmente ocorreu e foi autorizada no ambiente.

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

## Revisão da demonstração funcional

Conferir execução do comportamento pelo meio real de uso, suficiência das
asserções e caminho reproduzível pelo DEV. Sem tela não significa sem execução.
Breakpoint isolado e resposta qualquer não comprovam o requisito. Se impossível,
verificar o registro atribuído ao DEV e preservar os resultados não comprovados.
