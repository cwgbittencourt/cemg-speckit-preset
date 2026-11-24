# Política de PRs menores

## Unidades e responsabilidades

Task é unidade de execução; PR é unidade de revisão e integração; história é
unidade de aceite funcional. Um PR pode agrupar tasks e uma história pode exigir
vários PRs. Aprovação ou merge de PR não equivale a aceite funcional nem a deploy.

A IA implementa, executa verificações e faz uma passagem explícita de revisão.
O revisor humano aprova o PR no fluxo normal. O DEV valida o roteiro integrado
e decide o aceite da história. A mesma pessoa pode exercer funções diferentes,
mas a modalidade real de review deve ser declarada. Exceções à aprovação humana
exigem decisão humana explícita, com escopo e risco registrados; o agente não
pode concedê-las. O piloto deve manter aprovação humana por PR.

## Como dividir

Planejar no plan antes de gerar tasks. Cada PR deve ter objetivo coerente,
escopo delimitado, critérios cobertos, dependências e verificação própria.
Preferir incrementos por comportamento. Não separar mecanicamente por arquivo
ou camada quando isso impedir avaliar o incremento.

Código, testes e evidências viajam juntos. Preservar integridade, permissões e
contratos necessários desde o primeiro incremento que os utiliza. Separar
refatoração ampla, formatação ou arquivos gerados somente quando melhorar a
revisão sem quebrar a coerência da entrega.

A divisão dos PRs deve considerar escopo, complexidade e possibilidade de teste,
sem metas ou limites de quantidade de linhas ou duração da revisão. Para cada
incremento, avaliar se o objetivo é coerente, se os conceitos e impactos podem
ser compreendidos em conjunto e se o comportamento pode ser verificado sobre
a base declarada. Separar responsabilidades independentes quando isso facilitar
revisão e teste; manter juntas as mudanças necessárias para preservar invariantes
e comprovar o comportamento. Registrar a justificativa da divisão escolhida.

## PRs intermediários e dependentes

PR técnico intermediário pode não entregar valor utilizável, mas precisa de
testes próprios, compatibilidade e estado seguro. Código incompleto não deve
ficar exposto; se houver mecanismo de ativação, testar seu comportamento ligado
e desligado conforme o risco. O aceite da história permanece pendente.

Em PRs dependentes, registrar base, predecessor e ordem. Revisar o diff
incremental e manter rastreabilidade para o conjunto. Após mudança de base ou
correções, avaliar impacto, repetir checks afetados e renovar a revisão.
Não declarar como independente um PR que depende de outro ainda não integrado.

## Condições de integração normal por PR

- Objetivo e escopo revisados; incremento verificável sobre sua base declarada.
- Testes aplicáveis executados e aprovados na versão candidata, com evidências.
- Review da IA registrado com modalidade, base, versão e achados.
- Nenhum achado impeditivo aberto e aprovação humana registrada.
- Compatibilidade e segurança do estado intermediário verificadas.
- Dependências satisfeitas e checks exigidos pelo projeto aprovados.

Se alguma condição falhar, não declarar o PR pronto para integração normal.
Uma exceção humana deve manter os resultados reais e os riscos explícitos.

## Fechamento da história

O incremento que completa o fluxo inclui validação integrada da versão final,
regressão pertinente e roteiro consolidado para o DEV. Não criar PR adicional
apenas para cumprir contagem; o último PR funcional pode conter o fechamento.
O DEV valida o conjunto e registra aceite separado das aprovações dos PRs.
Mudanças relevantes posteriores exigem reavaliação das evidências e do aceite.

## Limites do pacote

Estas são regras de processo propostas para adoção manual. Sua aplicação técnica
depende de checks e configurações reais do projeto, não fornecidos neste pacote.

## Execução reproduzível por incremento

Cada incremento funcional deve demonstrar seu comportamento pelo meio real de
uso e permitir reprodução pelo DEV, inclusive por requisição, comando, mensagem
ou harness. Depuração é válida com resultado esperado e observação efetiva.
Para impossibilidade confirmada, seguir o registro e a decisão do DEV descritos
em EXECUCAO-REPRODUZIVEL.md, sem inferir aprovação de testes ou merge.
