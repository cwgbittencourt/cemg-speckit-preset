# Tasks: [FUNCIONALIDADE]

**Entradas**: spec.md, plan.md e artefatos aplicáveis.

## Regras de geração

- Gerar tasks concretas, IDs únicos e caminhos reais; mapear cada task a um PR previsto. Substituir os exemplos.
- Formato: `- [ ] T001 [P?] [US1?] (ID-001, ID-002) Descrição com caminho`.
- **Rastreabilidade de requisitos**: priorizar a leitura do `spec.md` e usar exatamente os mesmos IDs e prefixos já definidos nele (ex.: `FR-xxx`/`NFR-xxx` ou `RF-xxx`/`RNF-xxx`), sem impor siglas às cegas. Toda tarefa de entrega que implemente comportamento ou critério de aceite deve citar explicitamente os códigos correspondentes na própria linha do checkbox no formato `(ID-001, ID-002)` logo após os marcadores da tarefa (ex.: `- [ ] T011 [US1] (RF-001, RF-002) ...` ou `- [ ] T011 [US1] (FR-001, FR-002) ...`). Se o `spec.md` não possuir códigos explícitos, definir identificadores consistentes e aplicar o mesmo padrão uniformemente em todo o `tasks.md`. Tarefas puramente de setup, infraestrutura ou configuração sem requisito direto podem omitir o código ou citar um requisito não funcional aplicável.
- `[P]` só quando não há dependência nem conflito de arquivos.
- Agrupar por história e declarar dependências.
- Validação por história é obrigatória. Reusar testes adequados e criar os faltantes.
- Para cada task, definir entrega, origem, dependências e verificação objetiva.
- Uma task pode depender de anteriores; sua verificação não pode exigir futuras.
- Se não houver verificação significativa, agrupá-la com o incremento necessário.
- Setup/documentação podem ter verificação objetiva sem novo teste automatizado.
- Critérios de aceite funcional exigem evidência de comportamento.

## Fase 1 — Preparação

- [ ] T001 Preparar ambiente de teste conforme plan.md e verificar inicialização.
- [ ] T002 Preparar dados isolados e verificar limpeza conforme plan.md.

## Fase 2 — Fundação necessária

[Somente infraestrutura realmente compartilhada, com verificações próprias.]

## Fase 3 — US1: [Título]

**Critérios**: [US1-AC01, US1-AC02]
**Dependências**: [IDs]
**Teste independente**: [procedimento resumido]

- [ ] T003 [US1] (RF-001, RF-002) Criar/adaptar testes dos cenários US1-S01 e US1-S02 em [caminho].
- [ ] T004 [US1] (RF-001) Implementar comportamento US1-AC01 em [caminhos] e verificar [caso].
- [ ] T005 [US1] (RF-002) Implementar comportamento US1-AC02 em [caminhos] e verificar [caso].
- [ ] T006 [US1] (RF-001, RF-002) Executar cenários e regressão relacionada; registrar evidências em evidence/US1-validation.md.
- [ ] T007 [US1] (RF-001, RF-002) Revisar diff e critérios de aceite; registrar evidence/US1-review.md.
- [ ] T008 [US1] (RF-001, RF-002) Resolver achados impeditivos e renovar validação/revisão afetadas nos respectivos registros.
- [ ] T009 [US1] (RF-001, RF-002) Preparar e conferir plano de testes técnico do DEV em validation/US1-dev.md.
- [ ] T010 [US1] (RF-001, RF-002) Preparar plano de testes do Usuário Final (UAT) em linguagem de negócio em validation/US1-uat.md.
- [ ] T011 [US1] (RF-001, RF-002) Verificar prontidão e registrar estado em acceptance/US1.md, mantendo decisões do DEV (homologação) e do Usuário Final (produção) pendentes.

Se testes forem escritos antes da implementação, observar a falha esperada e
registrá-la; teste que falha por ambiente quebrado não comprova o cenário.
T008 pode encerrar como “nenhum achado impeditivo”, com referência à revisão real.

### Contrato de cada task

| ID | Origem | Depende de | Entrega | Como verificar | Resultado esperado |
|---|---|---|---|---|---|
| T004 | US1-AC01 | T003 e preparação aplicável | [resultado] | [comando/procedimento] | [resultado] |

Preencher para todas as tasks. Detalhes extensos podem ser vinculados ao plan.

## Demais histórias

[Repetir implementação e fechamento, preservando IDs únicos.]

## Regressão e integração da feature

[Verificações transversais necessárias; não deixar o único teste funcional aqui.]

## Dependências e paralelismo

[Ordem concreta; revisão deve preceder fechamento. Correções exigem nova validação.]

## Checkpoint por história

Implementação, validação, revisão, roteiro e aceite são estados separados.
Não incluir uma checkbox de aceite humano que o agente possa concluir sozinho.
Não confundir conclusão das tasks com aceite da história.

## Mapeamento de tasks para PRs

Preservar o formato original de checkbox. Usar esta matriz para associar PRs;
não introduzir marcadores novos que o parser do agente desconheça.

| PR previsto | Tasks incluídas | Objetivo | Predecessor/base | Validação própria | Evidência de review | Fechamento da história |
|---|---|---|---|---|---|---|
| PR-A | [IDs únicos] | [incremento] | [referência] | [tasks/comandos] | [registro] | [não/sim] |

Para CADA PR, gerar tasks concretas para execução de testes, revisão da IA,
resolução/revalidação de achados e preparação da descrição usando pr-template.md.
Acrescentar IDs únicos após resolver a divisão. As tasks de fechamento por
história não substituem esses ciclos por PR e podem reutilizar suas evidências.
Não duplicar tasks quando o último PR já incluir o fechamento completo.

Não criar checkbox de aprovação humana que a IA possa marcar autonomamente.
Registrar essa aprovação no registro do PR. Sem ela, prontidão para integração
normal permanece pendente, ainda que as tasks executadas pela IA tenham acabado.

## Caminhos de saída

Os caminhos evidence/, validation/ e acceptance/ são relativos ao FEATURE_DIR
identificado pelo script do comando, não à raiz do repositório. Gerar tasks com
caminhos concretos e usar os modelos instalados em
`.specify/presets/cemg-speckit-preset/templates/`.

## Condição de saída da etapa tasks

Aplicar policies/PASSAGENS.md do preset instalado. Registrar prontidão e pendências
com stage-status-template.json. Não declarar READY com decisão material pendente,
critério sem verificação ou dependência não resolvida para a etapa em questão.
Na próxima etapa, reavaliar estas condições contra os artefatos atuais.

## Tasks de execução e reprodução

Gerar tasks explícitas de iniciar/executar o incremento, comparar resultado real
ao esperado e registrar evidência, além dos testes adequados. Gerar roteiro com
o mesmo caminho para o DEV e fechamento integrado. Se a IA não puder executar,
manter a comprovação pendente e preparar registro de impossibilidade para decisão
do DEV; não marcar execução como aprovada.
