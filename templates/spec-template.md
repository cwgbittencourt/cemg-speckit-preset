# Especificação: [FUNCIONALIDADE]

**Branch**: [identificador] | **Data**: [data] | **Estado**: RASCUNHO
**Solicitação original**: [texto]

## Objetivo e escopo

[Problema, usuários, resultado esperado, limites e exclusões.]

## Cenários de uso e teste — obrigatório

Repetir a seção abaixo para cada história. IDs únicos dentro da feature.
Evitar dependência de histórias futuras para demonstrar o comportamento.
Dependências anteriores inevitáveis devem estar explícitas.

### US1 — [Título] — Prioridade [P1/P2/P3]

**História**: Como [perfil], quero [ação], para [resultado].
**Justificativa da prioridade**: [valor]
**Dependências e estado inicial**: [condições de negócio]
**Teste independente**: [ação e resultado observável que demonstram a história]

#### Critérios de aceite

- US1-AC01: [comportamento observável]
- US1-AC02: [erro ou condição de limite relevante]

#### Cenários de aceite

| Cenário | Critério | Dado | Quando | Então |
|---|---|---|---|---|
| US1-S01 | US1-AC01 | [estado] | [ação] | [resultado observável] |
| US1-S02 | US1-AC02 | [estado] | [ação] | [resultado observável] |

#### Condições para reprodução pelo DEV

- Perfil/permissões necessários: [perfil]
- Dados de entrada e estado inicial: [dados não sensíveis]
- Integrações e acessos necessários: [condições]
- Como observar e confirmar o resultado: [meio de verificação]
- Restrições conhecidas: [limitações ou nenhuma]

O plan deve tornar essas condições executáveis; não definir ferramentas internas
na spec sem necessidade do requisito.

## Casos de borda

[Limites, entradas inválidas, concorrência, permissões e indisponibilidade relevantes.]

## Requisitos funcionais e não funcionais

Usar prefixos consistentes com o idioma da especificação (ex.: `FR-001` / `NFR-001` ou `RF-001` / `RNF-001`). Os mesmos IDs e prefixos definidos aqui serão preservados integralmente no `tasks.md`.

- RF-001 (ou FR-001): O sistema deve [capacidade], coberta por [US1-AC01].

## Entidades principais

[Entidades e relações de domínio, quando aplicável.]

## Critérios de sucesso mensuráveis

- SC-001: [resultado mensurável e condição de medição].

## Premissas, dependências e questões abertas

[Registrar incertezas sem inventar decisões. Resolver as que impedem planejar.]

## Política de aceite

Exigir validação inicial pela IA, code review documentado e roteiro reproduzível
pelo DEV. Aceite humano é uma decisão separada, nunca inferida de checkboxes.

## Entrega incremental da história

Por história, indicar incrementos de comportamento possíveis, invariantes que
precisam valer desde o início e o que constitui o fluxo completo para aceite.
Não fixar detalhes de branches ou contagem de PRs na spec; o plan define a divisão.
História parcialmente implementada permanece sem aceite funcional.

## Condição de saída da etapa spec

Aplicar policies/PASSAGENS.md do preset instalado. Registrar prontidão e pendências
com stage-status-template.json. Não declarar READY com decisão material pendente,
critério sem verificação ou dependência não resolvida para a etapa em questão.
Na próxima etapa, reavaliar estas condições contra os artefatos atuais.

## Demonstração da história

Para cada história, descrever como o usuário ou DEV aciona o comportamento e
observa a resposta/efeito, com ou sem tela. Identificar critérios não observáveis
e esclarecer antes de prontidão. Não restringir a validação a interface gráfica.
