# Adoção por projeto

1. Inspecionar preset.yml, políticas, templates e comandos. O manifesto declara
   cada contribuição; os dez comandos incluem o fluxo oficial mais os adendos.
2. Confirmar `specify --version` e integração ativa. Este pacote requer Spec Kit `>=1.1.3`.
3. Preparar branch e preservar alterações locais antes da instalação futura.
4. Instalar com --dev apontando à pasta extraída que contém preset.yml.
5. Conferir `specify preset list`, `info` e `resolve` para templates e comandos.
6. Revisar o diff do projeto. Overrides locais e presets com maior prioridade
   podem prevalecer sobre a CEMG; diagnosticar a resolução, sem apagar arquivos.
7. Iniciar nova sessão do agente se necessário para recarregar skills/comandos.
8. Adaptar a constituição conscientemente usando o comando habitual; instalação
   não concede autorização para reescrever princípios já aprovados.
9. Fazer piloto com uma história: verificar artefatos, rodar testes reais,
   executar review, reproduzir roteiro e registrar decisão humana.

## Distribuição à equipe

Versionar este diretório num repositório da organização. Após aprovação e decisão
de licença, publicar ZIP imutável como release. Instalação por URL aceita
`specify preset add --from "URL_HTTPS_REAL_DO_ZIP"`; só fornecer URL existente.
Catálogo corporativo é uma etapa futura; nenhum foi criado nesta entrega.

## Atualização

`specify preset update cemg-speckit-preset --dev "CAMINHO_DA_NOVA_VERSAO"` substitui a
instalação por remoção e adição. Revisar fonte e preservar o estado antes de
atualizar: falha na adição pode deixar o preset removido. Atualizações precisam
de validação de compatibilidade e revisão dos comandos efetivamente registrados.

## Remoção

`specify preset remove cemg-speckit-preset` remove o preset e reconcilia as camadas de
comandos sobreviventes. Não apaga código, specs, tasks ou decisões humanas já
produzidos. Não usar apenas disable para restaurar comandos: comandos registrados
podem continuar presentes. Conferir list/resolve após remoção e recarregar agente.

## Manutenção

O preset usa comandos completos do upstream 1.1.3 para resolver explicitamente
regras conflitantes. A cada atualização da base, comparar o fluxo upstream,
preservar scripts/frontmatter/hooks e repetir instalação, resolução e remoção
nas integrações da equipe. Não editar caches globais dos agentes como distribuição.
