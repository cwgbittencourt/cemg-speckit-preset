# Condições de passagem entre etapas

## Regra geral

Antes de executar trabalho dependente, ler a etapa anterior e verificar suas
condições. Revalidar as condições na entrada de cada comando; não confiar apenas
em status antigo. Falha implica BLOQUEADO, identificação da lacuna, impacto,
ação necessária e pergunta objetiva quando depender de decisão humana.
Trabalho independente pode continuar, com escopo explícito. Rascunho pode ser
salvo; não declarar pronto, aprovado ou aceito enquanto houver pendência impeditiva.

## Esclarecimentos e premissas

Consultar contexto e evidências antes de perguntar. Decisões que alterem escopo,
comportamento, permissões, integridade, resultado esperado ou critérios de aceite
não podem ser presumidas. Propor opções com implicações e aguardar decisão.
Limitar perguntas por rodada apenas para facilitar a conversa; não limitar o
total de pendências nem converter dúvidas restantes em suposições. Premissas
reversíveis de baixo impacto podem ser documentadas com motivo e efeito.
Pedido para parar perguntas não resolve as pendências: manter o bloqueio dependente.

## Condições por passagem

| Destino | Condição de entrada e conclusão |
|---|---|
| Plan | Spec com critérios observáveis, cenários, escopo, dependências e nenhuma decisão relevante pendente |
| Tasks | Spec pronta e plan com matriz de cobertura, procedimentos, resultados esperados, ambiente e solução planejada para acessos/dados; divisão de PRs verificável |
| Implementação | Spec e plan consistentes; todas as tasks com origem, dependências e verificação; análise sem achados impeditivos abertos |
| Integração de PR | Incremento testado na versão candidata, review concluído, impeditivos resolvidos, estado seguro e aprovação humana explícita |
| Publicação em Homologação (Aceite DEV) | Fluxo integrado validado pela IA, revisão atualizada, plano de testes do DEV conferido e executado pelo DEV com aprovação explícita (ou exceção humana explícita), e plano de testes do Usuário Final disponibilizado |
| Publicação em Produção (Aceite Usuário Final + Assinatura PO) | Versão aprovada em homologação pelo DEV, plano de testes do Usuário Final executado e aprovado explicitamente por um Usuário Final na versão candidata, e assinatura final obrigatória do PO |

Na saída de spec/plan/tasks, registrar READY somente após verificar seus próprios
critérios. Pré-condições são reavaliadas também no destino. Análise de consistência
deve ocorrer antes da implementação; pode ser executada internamente como inspeção
somente leitura, sem exigir que o usuário lembre de chamar analyze separadamente.
Quando analyze for chamado, respeitar sua proibição de editar artefatos: apresentar
achados e estado calculado, sem escrever um registro nem aplicar remediação.

## Testes e cobertura

Para cada critério, identificar cenário, entrada, estado inicial, asserção,
procedimento, ambiente, dados, limpeza e evidência. Uma associação por palavras
não comprova cobertura; avaliar se a asserção realmente detectaria violação.
Infraestrutura ausente deve ter trabalho anterior planejado. Não iniciar a task
dependente até essa infraestrutura estar disponível e verificada. Testes existentes
adequados podem ser reutilizados. Testes escritos e compilação não substituem
execução funcional; mocks não comprovam integração real.

## Tasks e PRs

Task exige procedimento e resultado concreto, além de origem e dependências.
Expressões isoladas como verificar funcionamento são insuficientes. Agrupar tarefas
sem verificação própria significativa. Dividir PRs por escopo, complexidade e
possibilidade de teste; não estabelecer metas de linhas ou duração. Manter juntas
as mudanças necessárias para integridade, autorização e contratos desde o início.
Não adiar validações essenciais para PR futuro. Declarar predecessor e base reais.

## Evidências e versão

Registrar execução real, comando, diretório, ferramenta, versão/base, ambiente,
saída, resultado observado e referência verificável. Preservar falhas e rodadas.
Se não executado, manter estado real e tarefa pendente. Após correção, rebase ou
integração, avaliar impacto e renovar as verificações afetadas antes de prontidão.
Status preenchido e presença de arquivo não comprovam comportamento nem autenticidade.

## Revisão e impeditivos

Revisar diff e contexto, critérios de aceite, testes, integração, permissões,
integridade e regressões pertinentes. Registrar arquivo/linha, efeito e evidência
de cada achado, modalidade real e limites. Autorrevisão não é independente.
São impeditivos: violação de critério obrigatório ou princípio da constituição;
falha de teste exigido; perda/corrupção de dados; acesso indevido; integração
necessária não comprovada; PR intermediário inseguro; evidência obrigatória
ausente ou desatualizada. Outros riscos devem ser classificados com justificativa.
Não encerrar review normal com impeditivo aberto. Confirmar correção e revalidação.

## Roteiro e decisão do DEV

Estados distintos: ESCRITO, CONFERIDO_PELA_IA, EXECUTADO_PELO_DEV.
Se a IA não puder conferir algum passo, registrar CONFERENCIA_PARCIAL e o motivo.
Endereço, acesso seguro, dados, ações, resultados, observação e limpeza devem
permitir reprodução. A execução do DEV é decisão humana atribuída e não inferida.
Para aceite normal, exigir execução humana e decisão referente à versão validada.
Não confundir publicação, integração, aprovação de PR e aceite da história.

## Plano de testes do Usuário Final e publicação em Produção

Além do plano técnico do DEV (`validation/[USx]-dev.md`), cada história deve
entregar um plano de testes em linguagem de negócio para o Usuário Final
(`validation/[USx]-uat.md`).
- **Homologação**: só pode ser publicada após verificação e aprovação explícita
  do **DEV** na versão candidata.
- **Produção**: só pode ser publicada após execução e aprovação explícita de um
  **Usuário Final** sobre o plano de testes em homologação, seguida da
  **assinatura final obrigatória do PO** do projeto em `acceptance/[USx].md`.
A aprovação do DEV para homologação não substitui o teste do Usuário Final nem a
assinatura do PO, e a IA não pode preencher ou aprovar decisões humanas.

## Exceções humanas

Um pode continuar genérico não dispensa controles. Solicitar confirmação do escopo
exato quando ambíguo. Registrar condição não atendida, justificativa, risco, trabalho
permitido, responsável, data, versão, referência à decisão e ação posterior.
Uma exceção não aprova teste não executado nem substitui autorização de publicação.
Exceções em regras de segurança ou da constituição seguem o processo próprio do
projeto. Enquanto não houver decisão inequívoca, manter bloqueado o dependente.
O verificador automatizado deste pacote valida apenas o caminho normal; exceções
exigem revisão humana e procedimento separado, sem marcar checks falsamente verdes.

## Hooks e conflitos

Se houver extensions.yml ilegível, interromper a etapa dependente até identificar
os hooks e sua obrigatoriedade; não continuar silenciosamente. Falha ou ausência
de ferramenta para hook obrigatório impede a conclusão correspondente. Ausência
de configuração só é aceitável se nenhuma obrigação local exigir aquele hook.
Hook condicional de qualidade sem avaliador também é pendência, não aprovação.
Conflito entre constituição, comandos e política deve ser apresentado para decisão
humana. Não diluir a constituição nem reescrevê-la silenciosamente.

## Registro e controles externos

Usar templates/stage-status-template.json e registrar evidências em verification/.
Executar tools/check_gate.py antes de declarar prontidão quando houver Python.
Sem ferramenta, registrar a limitação e não declarar que o controle foi executado.
O verificador apenas verifica estrutura, estados, hashes e vínculo à revisão;
não interpreta a suficiência dos testes nem autentica declarações humanas.
Usar CI e proteção de branch para impor integração; exemplos e instruções em docs/.

## Complemento obrigatório de execução

Aplicar policies/EXECUCAO-REPRODUZIVEL.md: execução real pela IA e reprodução
pelo DEV, com ou sem tela. Se impossível, admitir registro confirmado pelo DEV
com decisão explícita, preservando o que não foi comprovado e o bloqueio normal.
O registro da impossibilidade não concede aceite por si só.
