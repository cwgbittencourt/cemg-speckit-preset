# Ativação dos controles por projeto

Nada neste guia foi aplicado a repositórios existentes. Instalar o preset copia
os arquivos e registra comandos; não ativa CI nem proteção de branch.

## Verificador local

Copiar o modelo stage-status-template.json para FEATURE_DIR/verification/spec.json
e preencher com resultados reais. Manter um registro por estágio/PR/história.
Consultar policies/gate-requirements.json para as chaves exigidas em cada estágio.

Cada evidência tem path relativo ao FEATURE_DIR, sha256 do arquivo e kind
(document, test-run ou product-execution). Na integração e aceite, incluir execução de teste e fonte
da decisão humana como evidências com hash. O campo human_decisions contém kind
(pr-approval ou story-acceptance), decision APPROVED, actor, timestamp, revision
e source (path relativo da fonte incluída nas evidências). Referências a decisões
reais podem ser exportadas para arquivo; não inventar aprovações nem identidades.

```powershell
python .specify/presets/cemg-speckit-preset/tools/check_gate.py --feature specs/001-exemplo --record verification/spec.json --stage spec --revision HASH_REAL --project .
```

O verificador retorna 1 em pendência, versão divergente, evidência alterada ou
fonte inesperada dos principais templates/comandos. Sem --project, não verifica
a resolução ativa. Não interpreta a suficiência dos testes, não autentica o autor
de decisões e não comprova a semântica de um documento. Checks true exigem análise
real do agente/revisor, não são preenchimento automático para liberar o fluxo.
Os nomes de checks do exemplo JSON são apenas do estágio spec; usar o arquivo
de requisitos para montar os outros registros. Exceções não passam pelo caminho
normal do verificador; exigem procedimento humano separado e preservação de falhas.

## Coleta da execução de testes

```powershell
python .specify/presets/cemg-speckit-preset/tools/record_test.py --feature specs/001-exemplo --cwd . --revision HASH_REAL -- python -m pytest tests/integration
```

O comando após -- é ilustrativo e só se aplica a um projeto que use pytest nesse
caminho. Substituir pelo teste real autorizado. O coletor executa com shell=False,
preserva stdout/stderr e resultado em pasta única e devolve a referência da
evidência. Exit code zero sozinho não demonstra asserções adequadas nem execução
de todos os cenários; revisar a saída e a cobertura. Saídas podem conter segredos:
usar ambiente/dados de teste, revisar acesso e não publicar logs sensíveis.
O valor revision deve ser obtido do código efetivamente testado. Em CI, usar o
SHA real do checkout; em árvore local alterada, registrar também diff e arquivos
novos com hashes nos relatórios e não apresentar o HEAD limpo como código testado.

## CI

examples/quality-gates.yml é uma referência desativada, não um workflow instalado.
Ela mantém o comando de teste vazio de propósito: ao habilitar sem configurar,
falha em vez de aprovar. Escolher a feature real, estágio, registro e testes do
projeto. Para múltiplas histórias, criar matriz ou descoberta explícita; não
validar só uma história e declarar cobertura de todas.

Os registros de planejamento precisam estar revisados e versionados. Evidências
de execução podem ser produzidas no job e o registro montado depois por rotina
específica do projeto; essa rotina deve verificar asserções/cobertura e nunca
converter automaticamente todas as condições em true. Mudanças relevantes exigem
nova revisão. Uma fonte de decisão humana local não substitui aprovação no GitHub.

## Proteção de branch e decisões humanas

No provedor Git, configurar manualmente ruleset/proteção da branch de destino:
exigir PR, aprovação humana conforme política, bloquear aprovação pelo autor,
invalidar aprovação após novas mudanças quando disponível, exigir checks de testes
e de qualidade e restringir bypass conforme responsáveis definidos. Confirmar
que os nomes dos checks correspondem aos jobs realmente executados.

Testar uma reprovação: um PR com teste falho ou aprovação ausente deve ficar
impedido de merge. A configuração deve ser revisada por administrador autorizado;
nenhuma API de repositório foi chamada para instalar essas regras nesta entrega.

## Atualidade dos comandos

Além de check_gate --project, conferir skills/arquivos registrados: o resolvedor
declarar a origem correta não prova que um agente com cache antigo recarregou
suas instruções. Conferir versão 1.0.0 e condições de passagem no comando efetivo,
reiniciar a sessão se necessário e realizar piloto com bloqueios reais.

## Novos registros de execução

Os gates de PR e aceite também exigem product-execution com resultado observado
no meio real de uso; consulte EXECUCAO.md e os novos modelos JSON. Impossibilidade
confirmada pelo DEV é um estágio separado, que não retorna READY nem libera o
caminho normal. Nunca tratar o retorno desse estágio como check de aceite normal.
