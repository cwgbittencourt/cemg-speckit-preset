# Exemplo de divisão da US1 em PRs

Exemplo ilustrativo. Nenhum PR foi criado e nenhum teste foi executado.
Para este exemplo, a história inclui API e interface; complementa US1-cadastro.md.

| PR | Objetivo | Dependência | Verificação | Estado da história |
|---|---|---|---|---|
| PR-A | Cadastro pela API com rejeições e integridade | Banco de teste preparado | HTTP com banco real; nome ausente e e-mail duplicado | Pendente |
| PR-B | Formulário conectado à API e erros apresentados | PR-A | Interação da interface e integração pertinente | Pendente |
| PR-C opcional | Correções finais, evidências consolidadas e roteiro | PR-B | Fluxo completo sobre versão final e regressão | Disponível ao DEV se comprovada |

PR-C só existe se houver trabalho material. Se PR-B incluir fechamento, dispensar
PR-C. Cada PR carrega testes e review próprios; não deixar comprovação para PR-C.
Não dividir duplicidade para depois quando ela for uma invariante do cadastro.

Exemplo de tasks para PR-A: preparar testes; implementar API e rejeições;
executar integração; revisar diff; corrigir/revalidar; preparar descrição.
Mapear IDs reais ao gerar tasks. Aprovação humana continua pendente.

Situação atual do exemplo: testes NÃO EXECUTADOS, review PENDENTE, aprovação
de todos os PRs PENDENTE e aceite funcional PENDENTE. Uma execução com mock de
persistência não aprovaria a integração real descrita acima.
