# Execução reproduzível com ou sem tela

## Regra de entrega

Antes de declarar um incremento funcional disponível ao DEV, a IA deve iniciar
o programa, serviço ou ambiente de execução aplicável, acionar o comportamento
entregue pelo meio real de uso e comparar o resultado observado ao esperado.
Isso pode ocorrer por automação, desde que exercite o meio real de entrada e
o fluxo previsto. Compilar, ler código, criar testes ou executar só unidades
isoladas não substitui a execução do comportamento entregue.

O DEV deve receber condições para reproduzir a execução e observar o resultado,
com ou sem interface gráfica. Pode usar debugger, desde que confira dados,
resposta e efeitos esperados. Atingir breakpoint, processo iniciar ou resposta
qualquer não comprova o requisito. Cada critério precisa de observação adequada.

## Meios de execução

| Entrega | Acionamento | O que observar |
|---|---|---|
| Interface gráfica | Iniciar aplicação e realizar ações reais | Resultado visual e efeitos previstos |
| API | Iniciar serviço e enviar requisição reproduzível | Status, corpo, persistência e erros previstos |
| Integração externa | Disparar operação em ambiente apropriado | Dados enviados, resposta e tratamento real |
| Mensageria | Publicar mensagem de teste no broker aplicável | Consumo, processamento, confirmação e efeitos |
| Job ou CLI | Executar comando com entrada conhecida | Saída, arquivos, registros e efeitos |
| Biblioteca | Executar harness ou exemplo que invoque a API pública | Retorno, erros e efeitos observáveis |

Adotar o nível de execução adequado ao produto. Não inventar tela para biblioteca
nem exigir produção para comprovar integração de teste. Simulação deve ser
identificada e seu limite declarado; não comprova acesso real à dependência simulada.

## Planejamento e tasks

Spec: identificar comportamento observável e critérios sem presumir aprovação.
Plan: definir inicialização, entrada, fixture, observação, asserções, depuração
opcional, limpeza e condições reais de acesso. Tasks: incluir execução real pela
IA e preparação do mesmo caminho para o DEV, por incremento e no fluxo integrado.
Se faltarem ferramenta ou acesso, não inventar execução: bloquear a comprovação
correspondente, buscar resolver e oferecer ao DEV o registro da impossibilidade.

PR puramente documental ou refatoração técnica sem novo comportamento pode usar
verificação adequada ao seu escopo; não pode declarar funcionalidade demonstrada
que ainda não existe. O PR que conclui a história deve permitir observar o fluxo
completo. Todos os incrementos executáveis devem ter caminho de reprodução próprio.

## Evidência e entrega ao DEV

Registrar versão, ambiente, inicialização, entrada exata, resultado esperado,
resultado real, efeitos e evidências. Fornecer endereço/comando/requisição/harness,
dados seguros, perfil, meios de observar, depuração opcional e limpeza. A IA
confere os passos que realmente puder executar. A diferença entre seu ambiente e
o do DEV deve ficar explícita; não prometer reprodutibilidade só por escrever roteiro.
O DEV reproduz, observa e decide o aceite normal da versão consolidada.

## Quando o teste for impossível

O DEV pode registrar explicitamente a impossibilidade, usando o template próprio.
O registro deve indicar cenário/critério, versão, ambiente, motivo, tentativas,
evidências disponíveis, o que ficou sem comprovação, risco e ação posterior.
Deve haver confirmação atribuível do DEV e uma decisão: AGUARDAR, REJEITAR ou
ACEITAR_COM_RESSALVAS. A IA pode preparar rascunho, não confirmar em nome do DEV.
Sem decisão humana o registro continua RASCUNHO.

Impossibilidade não equivale a teste aprovado nem a aceite automático. Se o DEV
aceitar com ressalvas, preservar NÃO EXECUTADO/IMPOSSIVEL e os checks normais
pendentes, relacionar a decisão ao registro de aceite e informar o escopo autorizado.
AGUARDAR mantém o trabalho dependente bloqueado; REJEITAR não aceita a entrega.
Uma falha funcional observada não pode ser reclassificada como impossibilidade
para contornar sua correção. Respeitar regras de segurança e constituição locais.

## Controle automatizado

O gate normal exige evidências da execução real de produto e da execução humana,
além dos testes. O stage dev-impossibility valida apenas o registro da decisão e
retorna DEV_IMPOSSIBILITY_RECORDED; nunca READY, aprovação de teste ou permissão
de merge. O resultado é verificação estrutural: não autentica a identidade do DEV.
Aceite com ressalvas continua exigindo o processo humano e os controles do provedor.
