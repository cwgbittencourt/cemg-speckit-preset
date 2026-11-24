# Revisão dos controles de qualidade

Comparação com os comandos e templates centrais do Spec Kit 1.1.3.
Os exemplos são ilustrativos. As alterações estão no pacote para inspeção;
nenhuma configuração foi aplicada aos projetos existentes.

| Prioridade | Item | Original | Preset ajustado | Verificação ou atenção restante | Exemplo |
|---|---|---|---|---|---|
| Crítica | Spec e aceite | Cenários e teste independente; premissas e quota total de esclarecimentos. | Removidas quotas e suposições materiais; dúvidas impedem prontidão. | Confirmar que todas as decisões materiais foram respondidas. | Duplicidade por CPF ou e-mail precisa de decisão antes do plan. |
| Crítica | Passagem entre etapas | Pré-requisitos específicos, sem condição uniforme de passagem. | Condições de entrada/saída e reavaliação na etapa seguinte. | Registrar lacuna, impacto e trabalho dependente bloqueado. | Permissão de exclusão indefinida bloqueia planejamento desse fluxo. |
| Crítica | Análise de consistência | Recomenda corrigir problemas críticos antes de implementar. | Problemas impeditivos bloqueiam trabalho dependente; inspeção exigida antes de implementar. | Análise permanece somente leitura; remediação não é automática. | Requisito de auditoria sem task impede implementar o fluxo afetado. |
| Alta | Planejamento dos testes | Ferramentas e cenários; tarefas de teste condicionais. | Entrada, asserção, ambiente, acesso e limpeza precisam ser viáveis. | Infraestrutura faltante deve anteceder a task dependente. | Envio de e-mail exige meio real de observar entrega no ambiente de teste. |
| Alta | Tasks verificáveis | Agrupamento por história, arquivos e dependências. | Contrato concreto por task e agrupamento quando a verificação isolada é vazia. | Procedimento deve detectar descumprimento, além de existir. | CPF repetido deve ser rejeitado e não criar outro registro. |
| Alta | Evidências | Validação final sem modelo detalhado de registro. | Coletor de execução, hashes e vínculo à revisão; falhas preservadas. | Arquivo e saída zero não comprovam adequação semântica. | Escrever testes sem executar mantém NÃO EXECUTADO. |
| Alta | Code review | Sem relatório por PR estruturado nesses comandos centrais. | Escopo mínimo, achados impeditivos e confirmação da correção. | Declarar autorrevisão e exigir decisão humana de PR. | Exclusão sem autorização impede integração até correção. |
| Alta | Divisão de PRs | Sem matriz obrigatória por incremento nos templates centrais. | Divisão por escopo, complexidade e possibilidade de teste. | Preservar invariantes e segurança desde o primeiro incremento. | Cadastro API completo antes da interface, sem adiar duplicidade essencial. |
| Alta | Roteiro do DEV | Teste independente e quickstart, sem contrato completo de aceite. | Estados escrito, conferido, parcial e executado separados. | Aceite normal exige reprodução e decisão humana da versão final. | Sem endereço, perfil ou dados, roteiro não está pronto. |
| Alta | Exceções | Pode avançar com confirmação genérica em certos checklists. | Exceção precisa de condição, risco, escopo, autor, versão e ação posterior. | Verificador normal não aprova exceções como se tudo tivesse passado. | Continuar codificando não dispensa teste de e-mail nem aceita a história. |
| Alta | Hooks obrigatórios | Erro na configuração pode ser informado e o fluxo continuar. | Configuração ilegível ou hook exigido não verificado bloqueia conclusão. | Verificar também condicionais de qualidade sem avaliador. | YAML inválido não permite afirmar que análise obrigatória foi executada. |
| Alta | Constituição e instruções | Constituição tem autoridade; regras dispersas por comando. | Instruções permissivas identificadas foram conciliadas; conflitos exigem decisão. | Não reescrever silenciosamente princípios aprovados. | Não manter testes opcionais contra validação obrigatória. |

## Controles técnicos

| Controle | Original | Preset ajustado | Ativação necessária | Exemplo |
|---|---|---|---|---|
| Testes obrigatórios | Instruções do fluxo, sem impor CI do projeto. | Coletor real e exemplo de job que falha sem configuração. | Ativar CI e configurar os testes reais do projeto. | Teste falho precisa impedir merge. |
| Aprovação humana | Não imposta pelos templates centrais consultados. | Decisão atribuída exigida; guia de proteção de branch. | Configurar o provedor e restringir bypass; Markdown não autentica pessoa. | Review da IA não substitui aprovação humana. |
| Versão validada | Verificação no fluxo sem o registro detalhado proposto. | Verificador recusa revisão divergente e evidência alterada. | Caller deve fornecer SHA real; renovar após mudanças. | Evidência do commit A não libera commit B. |
| Configuração ativa | Resolução por camadas e comandos registrados. | Opção --project verifica as fontes dos principais templates/comandos. | Conferir arquivos efetivos e recarga do agente; CI deve habilitar a checagem. | Override antigo deve ser detectado antes de afirmar uso do padrão. |

## Execução reproduzível e impossibilidade

| Item | Original | Preset ajustado | Exemplo |
|---|---|---|---|
| Execução do produto | Prevê validação de cenários, sem o contrato detalhado de reprodução proposto aqui. | A IA inicia, aciona e compara o comportamento real ao esperado; o DEV recebe os mesmos passos, com ou sem tela. | Subir a API, enviar requisição, conferir resposta e persistência; o DEV pode repetir no debugger. |
| Registro de impossibilidade | Não estrutura esse registro específico nos templates centrais comparados. | O DEV confirma motivo, cenários, versão, tentativas e riscos e decide aguardar, rejeitar ou aceitar com ressalvas. | Serviço externo de teste indisponível; preservar NÃO EXECUTADO e registrar a decisão humana. |
| Constituição | Princípios do projeto orientam o processo. | Princípio explícito encadeia planejamento, execução da IA, roteiro, reprodução e decisão do DEV. | Uma história não recebe aceite normal só porque os testes unitários passaram. |
