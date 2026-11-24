# Checklist de inspeção do pacote

Esta lista avalia a proposta; não é evidência de um software implementado.

- [ ] A unidade de aceite por história atende ao meu fluxo de trabalho.
- [ ] Os templates preservam as informações técnicas de que meus projetos precisam.
- [ ] Todos os critérios devem ser rastreáveis até cenário, teste e evidência.
- [ ] Validação executada está separada de testes apenas escritos.
- [ ] Há tratamento explícito de falhas, bloqueios e não execuções.
- [ ] Mocks não são apresentados como prova de integração real.
- [ ] Revisão identifica diff, versão, modalidade, achados e resolução.
- [ ] O roteiro inclui preparação, dados, ações, resultados e limpeza.
- [ ] Aceite humano não pode ser concedido autonomamente pelo agente.
- [ ] Exceções preservam resultados reais e identificam decisão humana.
- [ ] Alterações posteriores exigem renovação das evidências afetadas.
- [ ] Entendo que este pacote não inclui enforcement de CI nem aplicação automática.
- [ ] Antes de aplicar, vou confirmar caminhos, versão e comando efetivamente usado.

Decisão sobre adoção: [pendente]
Observações: [preencher após inspeção]

## Inspeção de divisão em PRs e governança

- [ ] Cada PR tem objetivo, dependências e verificação própria.
- [ ] Código, testes e review acompanham o incremento.
- [ ] A divisão não adia integridade, compatibilidade ou permissões essenciais.
- [ ] PR intermediário pode ser integrado sem conceder aceite funcional.
- [ ] Aprovação humana de PR, aceite do DEV (Homologação) e aceite do Usuário Final + PO (Produção) estão separados.
- [ ] Bases, versões e revalidações são rastreáveis.
- [ ] A divisão usa escopo, complexidade e possibilidade de teste, sem metas de linhas ou duração de revisão.
- [ ] O último incremento entrega validação integrada e roteiros consolidados (DEV e UAT).
