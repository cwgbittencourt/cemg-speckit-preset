# Exemplo ilustrativo — cadastro de cliente

ESTE EXEMPLO NÃO FOI EXECUTADO. Não corresponde a um projeto implementado.
Endpoint, comandos e dados são hipóteses didáticas, não evidências reais.

## Spec resumida

US1: Como operador, quero cadastrar clientes para identificá-los nas consultas.

- US1-AC01: Nome e e-mail válidos criam exatamente um cliente consultável.
- US1-AC02: E-mail já cadastrado é rejeitado sem duplicação.
- US1-AC03: Nome ausente é rejeitado sem persistência.

| Cenário | Dado | Quando | Então |
|---|---|---|---|
| US1-S01 | base isolada vazia | cadastro válido | cliente identificável na consulta |
| US1-S02 | cliente existente | mesmo e-mail | rejeição e manutenção de um registro |
| US1-S03 | base isolada vazia | nome ausente | erro e nenhum registro |

## Decisões ilustrativas do plan

API hipotética: POST /clientes; sucesso 201, duplicidade 409, validação 422.
Testes de integração HTTP com banco de teste real e limpeza por caso. Um mock
do repository não seria suficiente para comprovar a ausência de duplicação.
O teste unitário de validação pode complementar, sem substituir a integração.

## Tasks ilustrativas

- [ ] T001 Preparar banco isolado e verificar migrations/limpeza em tests/conftest.py.
- [ ] T002 [US1] Escrever cenários em tests/integration/test_clientes.py.
- [ ] T003 [US1] Implementar cadastro e rejeições em src/clientes.py e verificar os três cenários.
- [ ] T004 [US1] Executar testes e registrar evidence/US1-validation.md.
- [ ] T005 [US1] Revisar diff e registrar evidence/US1-review.md.
- [ ] T006 [US1] Resolver impedimentos e renovar evidências afetadas.
- [ ] T007 [US1] Entregar validation/US1-dev.md e atualizar acceptance/US1.md.

Hipótese de execução futura: `python -m pytest tests/integration/test_clientes.py`.
Resultado atual: NÃO EXECUTADO — projeto ilustrativo inexistente.
Validação: PENDENTE. Revisão: PENDENTE. Aceite humano: PENDENTE.

## Roteiro funcional esperado

O roteiro real precisaria fornecer inicialização, endereço, autenticação,
requisições completas, dados de teste e limpeza. Depois, o DEV cadastraria
nome/e-mail válidos, consultaria o cliente, repetiria o e-mail e tentaria nome
ausente, observando tanto respostas como o estado persistido. Sem essas
instruções concretas, o roteiro ainda não estaria pronto para entrega.

## Exemplo de bloqueio, não de aprovação

Se o banco de teste estiver indisponível, a IA registra NÃO EXECUTADO nos
cenários afetados, aponta a causa e mantém validação BLOQUEADA. Testes unitários
aprovados não mudam a situação da integração. O DEV recebe a pendência, não uma
declaração de que a história foi comprovada.
