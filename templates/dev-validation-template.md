# Roteiro do DEV — [US1]

Versão exata a validar: [commit + artefato/diff quando aplicável]
Ambiente/endereço: [valor]
Tempo aproximado: [estimativa]

## Preparação

1. Obter a versão: [procedimento].
2. Instalar/iniciar: [comandos, diretório, versões e serviços].
3. Configurar acesso: [perfil e obtenção segura das credenciais].
4. Preparar dados isolados: [comando/procedimento e valores].
5. Confirmar estado inicial: [verificação].

## Execução

| Passo | Critério/cenário | Ação exata e entrada | Resultado esperado | Como confirmar |
|---|---|---|---|---|
| 1 | [IDs] | [ação] | [resultado] | [tela/resposta/consulta] |

Cobrir cenário principal, erros e limites previstos; incluir permissões quando
pertinentes. Para API, CLI ou biblioteca, fornecer requisição, comando ou exemplo
executável em vez de inventar uma interface gráfica.

## Limpeza e repetição

[Restaurar dados e estado sem destruir informações compartilhadas. Instruções
devem permitir nova execução com o mesmo resultado.]

## Evidências da IA e limitações

- Validação: [link relativo]
- Revisão: [link relativo]
- O que foi executado e o que ficou pendente: [resumo]
- Bloqueios conhecidos e solução: [detalhes]
- Roteiro conferido pela IA: [sim/não/parcial e evidência; nunca presumir]

## Registro da execução humana

Responsável: [DEV]
Data/hora e fuso: [valor]
Resultados e evidências: [preenchidos a partir de execução real]
Decisão: registrar em `acceptance/[US1].md`.

## Consolidação dos PRs da história

- PRs integrantes e ordem: [IDs/URLs]
- Versão final consolidada: [hash/artefato]
- Roteiro: INCREMENTO / HISTORIA_COMPLETA
- Critérios ainda pendentes: [IDs ou nenhum]

Um roteiro de incremento não substitui o roteiro integrado para aceite. Entregar
instruções completas num ponto de entrada, sem exigir combinação de passos
dispersos. Atualizar a versão e os passos após correções ou integrações relevantes.

## Estado de reprodução

- Roteiro: ESCRITO / CONFERIDO_PELA_IA / CONFERENCIA_PARCIAL / EXECUTADO_PELO_DEV
- Passos conferidos pela IA e evidência:
- Passos pendentes, motivo e impacto:
- Execução humana: responsável, data, versão, resultados e referência real.

Somente aceite normal após execução humana e decisão explícita na versão final.
Conferência parcial deve permanecer visível e exigir tratamento antes de declarar
prontidão normal. Escrita do roteiro não comprova sua reprodutibilidade.

## Execução com ou sem tela

O DEV deve conseguir iniciar e acionar o programa, API, integração, mensagem,
job, CLI ou harness de biblioteca e verificar resultado e efeitos. Incluir comando,
requisição ou entrada completos, dados, acesso, resultado esperado e observação.
Depuração pode complementar: indicar pontos úteis e valores esperados, sem tratar
atingir breakpoint como sucesso.

Se o DEV confirmar que não pode executar, preencher dev-impossibility-template,
preservar os cenários não executados e registrar AGUARDAR, REJEITAR ou
ACEITAR_COM_RESSALVAS. A IA não confirma impossibilidade nem aceite por ele.
