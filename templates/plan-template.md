# Plano de implementação: [FUNCIONALIDADE]

**Branch**: [branch] | **Data**: [data] | **Spec**: [caminho]

## Resumo

[Requisito principal e abordagem técnica.]

## Contexto técnico

- Linguagem/versão: [valor]
- Dependências: [valor]
- Armazenamento: [valor ou não aplicável]
- Ferramentas de teste: [valor]
- Plataforma e tipo de projeto: [valor]
- Metas de desempenho, restrições e escala: [valores]

## Verificação da constituição

[Princípios aplicáveis, conformidade, exceções e justificativas. Reavaliar após design.]

## Estrutura e artefatos

[Estrutura concreta de código e testes. Preservar pesquisa, modelo de dados,
contratos e quickstart exigidos pela versão instalada. Este plan não gera tasks.]

Artefatos por história em `specs/[feature]/`:
- `evidence/US1-validation.md` e `evidence/US1-review.md`
- `validation/US1-dev.md` e `acceptance/US1.md`
- logs em localização persistente referenciada, quando necessários.

## Matriz de validação

Cobrir todos os critérios; acrescentar múltiplas linhas quando necessário.

| História | Critério/cenário | Nível de teste | Teste existente ou a criar | Execução | Resultado esperado | Evidência |
|---|---|---|---|---|---|---|
| US1 | US1-AC01 / US1-S01 | [unidade/integração/E2E/manual] | [arquivo/caso] | [comando/procedimento] | [asserção] | [caminho] |

## Ambiente e dados

- Instalação e inicialização: [comandos completos com diretório de execução]
- Variáveis necessárias: [nomes e obtenção segura, nunca segredos]
- Serviços reais de teste e versões: [valores]
- Criação de dados/fixtures, isolamento e limpeza: [procedimentos]
- Acesso do DEV e observação dos resultados: [instruções]
- Simulações e limites do que elas comprovam: [detalhes]

## Viabilidade por história

| História | IA consegue executar? | DEV consegue reproduzir? | Impedimento | Trabalho para resolver |
|---|---|---|---|---|
| US1 | [sim/não/parcial] | [sim/não/parcial] | [causa ou nenhum] | [ação/dependência] |

Não prometer execução sem ferramenta/acesso. Incluir nas tasks o trabalho
necessário para remover impedimentos. Limitação persistente mantém validação pendente.

## Estratégia de revisão

- Base do diff e forma de identificar a versão final: [procedimento]
- Escopo e áreas de risco: [requisitos, integração, regressão, segurança pertinente]
- Modalidade prevista: [autorrevisão/revisão por outro agente/revisão humana]
- Registro de achados: arquivo, linha, impacto, prioridade e resolução.
- Achados impeditivos: [critérios objetivos de bloqueio do projeto]
- Revalidação após correções: [testes afetados e atualização da revisão]

## Dependências e sequência de entrega

[Histórias e infraestrutura necessárias; evitar referências circulares.]

## Complexidade e exceções

[Justificativa, alternativas e decisão humana quando exigida.]

## Estratégia de entrega em PRs

Aplicar `.specify/presets/cemg-speckit-preset/policies/POLITICA-PRS.md`. Planejar incrementos coerentes e verificáveis. Não
confundir fases internas com PRs nem exigir um PR por task.

| PR previsto | Objetivo e escopo | US e critérios parciais ou finais | Tasks previstas | Base e dependências | Testes e evidências | Revisor e modalidade | Condição de integração | Completa a história? |
|---|---|---|---|---|---|---|---|---|
| PR-A | [incremento] | [IDs e cobertura] | [áreas; resolver IDs ao gerar tasks] | [base/ordem] | [execução e caminhos] | [papel] | [checks e compatibilidade] | [sim/não] |

Por PR, prever estado intermediário seguro, regressão e tratamento de mudança
de base. Justificar a divisão por escopo, complexidade e possibilidade de teste,
sem estabelecer metas de linhas ou duração da revisão. A matriz de tasks deve
resolver o mapeamento sem exigir IDs prematuros.
O último incremento deve prever teste integrado, roteiro final e aceite humano.

## Preservação do planejamento técnico

Produzir research.md, data-model.md, contracts/ e quickstart.md conforme as
fases e condições do comando oficial. Resolver dúvidas técnicas antes do design.
As evidências propostas não substituem esses artefatos.

## Condição de saída da etapa plan

Aplicar policies/PASSAGENS.md do preset instalado. Registrar prontidão e pendências
com stage-status-template.json. Não declarar READY com decisão material pendente,
critério sem verificação ou dependência não resolvida para a etapa em questão.
Na próxima etapa, reavaliar estas condições contra os artefatos atuais.

## Plano de execução do produto

Por incremento, definir como iniciar o programa, acionar o comportamento real,
fornecer entrada e verificar resposta, dados e efeitos esperados. Incluir requisição,
comando, mensagem ou harness conforme o produto e opção de depuração quando útil.
Prever execução pela IA, reprodução pelo DEV, dados, acessos e limpeza. Testes
isolados não substituem a demonstração funcional. Planejar resolução de impedimentos.
