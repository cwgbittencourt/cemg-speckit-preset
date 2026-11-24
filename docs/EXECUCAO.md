# Execução reproduzível e registro de impossibilidade

## Caminho normal

1. No plan, definir como iniciar o produto e acionar o comportamento pelo meio
   real de uso. Para API, usar requisição; para mensagem, publicar uma entrada;
   para biblioteca, usar exemplo ou harness executável. Prever dados e limpeza.
2. Nas tasks, incluir a execução pela IA e o roteiro de reprodução pelo DEV.
3. A IA inicia e aciona o produto, verifica dados/resposta/efeitos contra critérios
   e preserva evidências. Teste automatizado de fluxo é válido se realmente
   exercitar a entrada e verificar os resultados previstos.
4. Preencher product-execution-template.json com executor AI, state OBSERVED,
   meio, versão, inicialização, entrada, esperado, observado, efeitos, cenários
   e artifacts com path relativo à feature e sha256. Acrescentar ao registro do
   gate uma evidence com kind product-execution e hash desse JSON.
5. O DEV recebe roteiro completo e reproduz o mesmo comportamento, inclusive
   por debugger quando útil. Preencher outro registro com executor DEV a partir
   da execução real e decisão humana atribuível. Não preencher pelo DEV sem fonte.
6. O gate de PR exige demonstração pela IA; o gate de aceite exige também
   demonstração pelo DEV e decisão de aceite. Ambos mantêm as exigências de testes,
   review, versão e aprovações da política anterior.

Meios aceitos no JSON: UI, API, INTEGRATION, MESSAGE, JOB, CLI, LIBRARY.
O estado OBSERVED só pode ser usado após verificar resultado e efeitos esperados;
não significa apenas ter observado que o programa falhou. Uma falha deve ficar
registrada como tal e não pode liberar o caminho normal. Hashes comprovam vínculo
dos arquivos, não a veracidade ou suficiência semântica do que foi declarado.

## Sem tela

Uma requisição reproduzível precisa de método, endpoint, headers não sensíveis,
corpo ou entrada e resposta esperada. Mensagens precisam de destino, formato,
correlação e efeito previsto. Jobs precisam de comando, dados, saída e modo de
observar os efeitos. Bibliotecas precisam de exemplo que use o contrato público.
Depuração deve indicar valores e efeitos a conferir; breakpoint isolado não basta.

## Quando o DEV não consegue executar

Preparar dev-impossibility-template.md e/ou a versão JSON para o mesmo conjunto
de cenários. A IA registra o que sabe e deixa o estado DRAFT. O DEV confirma a
impossibilidade e decide. No JSON, usar:

- state CONFIRMED_BY_DEV apenas após confirmação humana atribuível.
- decision WAIT para AGUARDAR, REJECT para REJEITAR ou ACCEPT_WITH_RESERVATIONS
  para ACEITAR_COM_RESSALVAS.
- human_confirmation com actor, timestamp e source; source aponta a evidência
  local da confirmação real incluída em evidence com path e sha256.
- reason, attempts, unverified, risk, scope, next_action e next_owner preenchidos.

```powershell
python .specify/presets/cemg-speckit-preset/tools/check_gate.py --feature specs/001-exemplo --record verification/dev-impossibility.json --stage dev-impossibility --revision HASH_REAL
```

Um registro estruturalmente válido retorna DEV_IMPOSSIBILITY_RECORDED, inclusive
se a decisão for aguardar ou rejeitar. Esse resultado não é READY, teste aprovado,
aceite normal ou permissão de integração. Relacionar a decisão ao registro de
aceite; se houver ressalvas, preservar os cenários não executados e os riscos.
Não usar esse estágio como substituto do check obrigatório de prontidão no CI.

## Contrato dos registros de prontidão

O preset `1.0.0` exige checks estruturados e evidências verificáveis por hash.
Os modelos iniciais ficam pendentes de propósito e só atingem `READY` quando
todos os critérios aplicáveis ao estágio foram comprovados na revisão candidata.
Não preencher execução retroativa que não ocorreu. O pacote não inicia aplicações
nem altera projetos existentes ao ser apenas inspecionado.
