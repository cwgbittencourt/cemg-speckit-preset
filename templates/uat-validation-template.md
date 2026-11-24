# Plano de Testes do Usuário Final (UAT) — [US1]

Versão em homologação a validar: [versão/release + commit quando aplicável]
Ambiente/endereço de homologação: [URL ou acesso do ambiente de homologação]
Tempo aproximado: [estimativa]

> **Objetivo**: Validar o comportamento entregue sob a perspectiva de negócio antes da publicação em **Produção**.
> A IA prepara este plano em linguagem clara e não técnica, mas **nunca** executa nem aprova em nome do Usuário Final.

## Pré-condições de negócio

1. Acesso ao ambiente de homologação: [URL/app e perfil de usuário necessário].
2. Dados ou cadastros iniciais esperados: [descrição simples dos dados disponíveis, sem credenciais em texto puro].
3. Pré-requisito de entrada: verificação e aprovação do DEV concluídas para publicação em homologação.

## Cenários de teste do Usuário Final

| Passo | Requisito / Critério | O que fazer | Resultado esperado | Resultado obtido |
|---|---|---|---|---|
| 1 | [IDs do spec.md, ex.: RF-001 / US1-AC01] | [ação em linguagem de negócio] | [comportamento visível esperado] | [PENDENTE / APROVADO / REPROVADO] |

Cobrir o fluxo principal de negócio, validações/mensagens de erro esperadas e regras de permissão relevantes ao usuário final.

## Evidências da validação em homologação

- Prints, capturas de tela, arquivos gerados ou registros observados: [links relativos ou referências]
- Divergências ou observações encontradas: [detalhes ou nenhuma]

## Registro da execução e decisão do Usuário Final

- Responsável (Usuário Final): [nome/identificação]
- Área/Perfil: [perfil de negócio]
- Data/hora e fuso: [valor]
- Versão efetivamente testada em homologação: [versão/commit]
- Decisão para publicação em Produção: PENDENTE / APROVADO / REPROVADO / APROVADO_COM_RESSALVAS
- Referência consolidada: registrar em `acceptance/[US1].md`.

## Regra de publicação em Produção

A publicação em **Produção** exige a execução deste plano e aprovação explícita por um Usuário Final na versão homologada.
Aprovação de PR ou aprovação do DEV para homologação **não** substitui o teste do Usuário Final.
Alterações após o teste invalidam a aprovação anterior e exigem nova validação dos cenários afetados.
