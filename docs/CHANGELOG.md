# Changelog

## [1.0.0] — 2026-11-23

Release inicial do preset **`cemg-speckit-preset`** para Spec Kit (`>=1.1.3`), compatível e validado com **Codex**, **GitHub Copilot**, **Antigravity**, **Claude Code** e **Kiro CLI**.

### Principais entregas
- **Execução reproduzível obrigatória com ou sem tela**: exige iniciar, acionar, observar e comparar resultados reais em UI, API, integração, mensageria, job, CLI ou biblioteca (depuração é aceita quando demonstra resultados; breakpoint ou teste unitário isolado não basta).
- **Rastreabilidade ponta a ponta**: vínculo estrito entre requisitos (`RF`/`RNF` ou `FR`/`NFR`), critérios de aceite (`USn-ACnn`), cenários (`USn-Snn`), tarefas em `tasks.md`, PRs e evidências.
- **Planos de validação separados para Homologação e Produção**:
  - Roteiro técnico do DEV (`validation/[USx]-dev.md`) para publicação em Homologação.
  - Plano de testes do Usuário Final / UAT (`validation/[USx]-uat.md`) em linguagem de negócio, aliado à assinatura final obrigatória do PO em `acceptance/[USx].md` para publicação em Produção.
- **Tratamento estruturado de impossibilidade técnica**: modelos Markdown e JSON (`dev-impossibility-template`) para registro confirmado pelo DEV com decisão explícita (`AGUARDAR`, `REJEITAR` ou `ACEITAR_COM_RESSALVAS`), sem mascarar testes não executados como aprovados.
- **Ferramentas de verificação e integridade**:
  - `tools/check_gate.py`: validador determinístico de prontidão por estágio (`spec`, `plan`, `tasks`, `pr`, `acceptance`, `production` e `dev-impossibility`) com checagem de hashes SHA-256.
  - `tools/record_test.py`: coletor de execução de testes com preservação de `stdout`/`stderr` e vínculo à revisão do código.
  - `tools/verify_package.py`: verificador de integridade do pacote contra `preset.yml` e `checksums.json`.
