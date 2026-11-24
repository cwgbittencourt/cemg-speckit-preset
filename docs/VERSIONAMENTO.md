# Versionamento e convivência

## Identidade estável

Manter o ID `cemg-speckit-preset` e registrar a versão em `preset.yml` usando SemVer (`X.Y.Z`).
A versão `1.0.0` é a release inicial estável deste preset, consolidando condições
obrigatórias de passagem, execução reproduzível do produto, rastreabilidade de
requisitos e governança de aceite para Homologação (DEV) e Produção (Usuário Final + PO).

- **PATCH**: correções de instruções ou documentação sem mudar o contrato esperado.
- **MINOR**: acréscimos compatíveis ao contrato existente.
- **MAJOR**: mudanças incompatíveis em política, artefatos ou fluxo que exijam migração.

Não alterar o conteúdo de uma release já distribuída; sempre publicar uma nova versão.
Qualquer atualização deve explicar os efeitos nos projetos e a compatibilidade.

## Convivência recomendada

Projetos diferentes podem usar versões diferentes do mesmo ID. No mesmo projeto,
manter uma única versão ativa. A instalação é indexada pelo ID do preset; não
tratar versões como camadas simultâneas. O Spec Kit oficial continua sendo a base.

Evitar `cemg-speckit-preset-v1` e `cemg-speckit-preset-v2` como IDs apenas para distinguir releases:
seriam presets distintos fornecendo os mesmos nomes de templates e comandos,
com precedência que pode gerar mistura de políticas. Comparar versões em cópias
de teste ou branches/worktrees separados, com instalação e verificação em cada um.

O nome do arquivo ZIP e da pasta pode incluir a versão (por exemplo,
`cemg-speckit-preset-1.0.0.zip`). Isso não muda o ID estável do manifesto.

## Atualização controlada

Não é necessário desinstalar manualmente antes de atualizar. O comando `update`
faz remoção e adição internamente. Revisar a nova fonte e preservar o estado
antes de executar; se a adição falhar, o preset anterior pode já ter sido removido.
Depois, conferir `list`/`info`/`resolve`, comandos registrados e executar piloto.

Para voltar a uma release anterior, usar uma cópia preservada dessa release e
o fluxo `update --dev`, sujeito à compatibilidade do CLI. A volta do preset não
desfaz artefatos, código ou decisões já produzidos. Mudanças no projeto precisam
de avaliação e reversão próprias. Consulte `docs/ADOCAO.md` para os comandos.
