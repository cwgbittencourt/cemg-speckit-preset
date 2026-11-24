# PR [identificador] — [objetivo]

Estado: RASCUNHO / EM_VALIDACAO / EM_REVISAO / PRONTO_PARA_INTEGRACAO / BLOQUEADO / INTEGRADO
Tipo: INTERMEDIARIO / FECHAMENTO_DE_HISTORIA
História e critérios: [IDs e cobertura parcial/final]
Tasks incluídas: [IDs]
Base resolvida e versão candidata: [hashes; identificar diff local se aplicável]
Predecessores, ordem e diff incremental: [referências]

## Problema e comportamento entregue

[Gatilho, efeito observável e por que o incremento existe.]

## Escopo e estado intermediário

- Incluído e excluído: [detalhes]
- Compatibilidade e invariantes preservadas: [evidência]
- Proteção de comportamento incompleto, quando necessária: [mecanismo e testes]
- Justificativa da divisão por escopo, complexidade e possibilidade de teste: [detalhes]

## Testes e evidências

| Critério/cenário | Execução e versão | Resultado real | Evidência |
|---|---|---|---|
| [IDs] | [comando/procedimento] | NÃO EXECUTADO | [motivo/referência] |

## Review da IA

Modalidade, revisor, versão, registro de achados, resoluções e limites: [referência].
Mudanças posteriores e revalidações: [referências].

## Reprodução pelo revisor ou DEV

[Ambiente, dados, ações e resultados ou link para roteiro completo do incremento.]
Limitações, bloqueios e riscos pendentes: [detalhes].

## Aprovação humana e integração

- Aprovação humana: PENDENTE / APROVADO / ALTERACOES_SOLICITADAS
- Responsável, data, versão e referência à decisão: [preencher com fonte real]
- Condições da política `.specify/presets/cemg-speckit-preset/policies/POLITICA-PRS.md` atendidas: [avaliação e pendências]
- Prontidão para integração normal: NAO / SIM
- Exceção explícita, se houver: [decisor, motivo, risco e escopo]
- Integração efetiva: [referência e versão, ou pendente]

A IA não infere aprovação humana nem integração. Não abrir, integrar ou publicar
PR com base apenas no preenchimento deste template; respeitar a autorização real.

## Fechamento funcional

Se intermediário, manter história pendente. Se completar a história, apontar
validação integrada, roteiro consolidado e registro de aceite do DEV separado.

## Condições verificáveis

Aplicar policies/PASSAGENS.md do preset instalado. Referenciar saídas de execução
reais e a revisão atual; presença de arquivo não comprova aprovação. Registrar
impeditivos, correções e revalidação. Exceções exigem condição, risco, escopo,
responsável, data, versão, decisão atribuível e ação posterior; nunca converter
NÃO EXECUTADO em PASSOU. Aprovação humana deve apontar a fonte real da decisão.

## Demonstração executável do incremento

- Como iniciar e acionar o comportamento:
- Entrada, resultado esperado e observação real:
- Evidência da execução pela IA:
- Como o DEV reproduz ou depura:
- Se impossível: referência ao registro e decisão do DEV, com estado real preservado.

Não declarar prontidão normal de integração com execução obrigatória não comprovada.
