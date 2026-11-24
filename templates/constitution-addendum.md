# Adendo à constituição — qualidade por história

Cada história de usuário / caso de uso deve ser independentemente testável ao fim
de sua implementação única pela IA, possuindo critérios de aceite identificados,
validação executável, revisão do código, um plano de testes técnico para o DEV
(`validation/[USx]-dev.md`) e um plano de testes em linguagem de negócio para o
Usuário Final (`validation/[USx]-uat.md`).

- **Publicação em Homologação**: exige validação da IA, revisão concluída e
  verificação e aprovação explícita do **DEV** sobre o plano de testes do DEV.
- **Publicação em Produção**: exige obrigatoriamente execução e aprovação
  explícita por um **Usuário Final** sobre o plano de testes do Usuário Final na
  versão homologada, seguida da **assinatura final obrigatória do PO** do projeto.
- **Rastreabilidade de requisitos em `tasks.md`**: priorizar a leitura do
  `spec.md` e preservar exatamente os mesmos IDs e prefixos já definidos nele
  (ex.: `FR-xxx`/`NFR-xxx` ou `RF-xxx`/`RNF-xxx`), sem impor siglas às cegas.
  Toda tarefa de entrega que implemente comportamento ou critério de aceite deve
  citar os códigos correspondentes na própria linha do checkbox no formato
  `(ID-001, ID-002)` logo após os marcadores (ex.:
  `- [ ] T011 [US1] (RF-001, RF-002) ...`). Tarefas puramente de setup,
  infraestrutura ou configuração sem requisito direto podem omitir o código ou
  citar um requisito não funcional aplicável.

1. A IA deve executar as validações planejadas que suas ferramentas e acessos
   permitirem. Criar testes ou ler código não equivale a executá-los.
2. Toda execução deve identificar versão do código, ambiente, procedimento,
   resultado esperado, resultado observado e evidência verificável.
3. Não execuções, limitações e falhas devem ser explícitas. Não declarar como
   aprovado o que não foi executado. Bloqueios exigem causa e próximo passo.
4. Testes devem verificar comportamento e riscos relevantes. Reutilizar cobertura
   adequada. Não impor novos testes triviais para toda task documental ou técnica.
5. Mocks comprovam o comportamento sob simulação; não comprovam uma integração real.
6. A revisão deve comparar o diff com requisitos e analisar regressões. Registrar
   autoria e modalidade; autorrevisão não é revisão independente.
7. Alterações posteriores invalidam as evidências afetadas, que devem ser renovadas.
8. Sem validação e revisão concluídas, a história não está disponível para aceite
   normal. Exceções só podem ser decididas pelo DEV, com risco e escopo registrados.
9. Implementação concluída não significa história aceita. A IA não pode preencher
   uma decisão humana sem instrução humana explícita e atribuível.
10. Evidências não devem expor segredos nem dados pessoais desnecessários.

Templates instruem o processo. A imposição técnica depende de ferramentas e
políticas adicionais do repositório, que devem ser declaradas separadamente.

## Entrega em PRs revisáveis

Aplicar `.specify/presets/cemg-speckit-preset/policies/POLITICA-PRS.md`: planejar a divisão no plan, mapear tasks, validar e
revisar cada incremento. Exigir aprovação humana por PR no fluxo normal e
preservar o estado seguro dos incrementos intermediários. Registrar dependências,
bases e novas rodadas após alterações. Não conceder aceite de história por merge.

## Condições de passagem

Adotar policies/PASSAGENS.md do preset instalado: pré-condições reavaliadas,
perguntas sobre decisões materiais, bloqueios explícitos e exceções delimitadas.
Não conceder prontidão por limite de perguntas, aviso ou inferência de aceite.


## Princípio obrigatório de validação por história

Para cada história de usuário, o planejamento deve definir como a IA executará
o comportamento entregue, como seu resultado será observado e como o DEV
reproduzirá essa execução. Isso vale com ou sem interface gráfica.

1. Antes de declarar o incremento funcional disponível, a IA deve iniciar o
   programa/serviço ou harness apropriado, acionar o comportamento pelo meio real
   de uso e comparar dados, resposta e efeitos ao resultado esperado.
2. A IA deve entregar roteiro reproduzível com versão, ambiente, inicialização,
   acesso seguro, dados, entrada, passos, resultados esperados, observação e limpeza.
3. O DEV deve executar o programa ou fluxo pelo meio adequado, podendo depurar,
   conferir os resultados e registrar sua decisão de aceite na versão avaliada.
4. Teste unitário, compilação, arquivo de roteiro ou breakpoint isolado não
   substituem comprovação do comportamento. Automação que exercite o fluxo real
   e suas asserções é válida; declarar limites de mocks e simulações.
5. Se a IA não puder executar, preservar a comprovação pendente, explicar o motivo
   e preparar as condições para o DEV. Se o teste for impossível para o DEV, ele
   confirma o registro, identifica cenários, versão, tentativas, risco e evidências
   e decide AGUARDAR, REJEITAR ou ACEITAR_COM_RESSALVAS, com ação posterior.
6. A IA pode preparar o rascunho da impossibilidade, nunca confirmar ou aceitar
   pelo DEV. Registro de impossibilidade não equivale a teste aprovado, aceite
   automático nem autorização de integração. Preservar os resultados reais.

Aplicar o princípio a spec, plan, tasks, execução, review, PR e aceite. Manter
decisões humanas separadas dos resultados da IA. Sua adoção exige incorporação
explícita à constituição do projeto, sem sobrescrever silenciosamente princípios.
