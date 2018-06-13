# PROCON
Kaggle - Dataset: Consumer Business Complaints in Brazil 

Consumer Business Complaints in Brazil Consumer complaints about issues with business in Brazil Postado por: Luiz Gerosa. Líder técnico da Picpay.

O dataset xxxx possui 1.206.072 registros, distribuidos entre os anos de 2012 a 2016.

2012: possui 211.076 registros, sendo x linhas e y colunas xxxx. 2013: 268.096 registros, sendo x linhas e y colunas. 2014: 267.764 registros, sendo x linhas e y colunas. 2015: 255.650 registros , sendo x linhas e y colunas. 2016: 203.486 registros, sendo x linhas e y colunas.

A sua estrutura contém nas colunas os campos:

AnoCalendario: DataArquivamento: data de arquivamento das reclamações. DataAbertura: data de abertura das reclamações. CodigoRegiao: índices atribuídos às regiões correspondentes aos agrupamentos das unidades da federação constantes no mapa político do Brasil.
Região: regiões correspondentes aos agrupamentos das unidades da federação. constantes no mapa político do Brasil. UF: estados brasileiros. strRazaoSocial: razão social das empresas. strNomeFantasia: nome comercial/de fachada das empresas. Tipo: NumeroCNPJ RadicalCNPJ RazaoSocialRFB NomeFantasiaRFB CNAEPrincipal DescCNAEPrincipal Atendida CodigoAssunto DescriçãoAssunto CodigoProblema SexoConsumidor FaixaEtariaConsumidor CEPConsumidor

Pergunta de pesquisa

A partir de uma breve pesquisa na internet sobre a atuação do PROCON, chegamos à seguinte pergunta de pesquisa:

O PROCON é eficaz na proteção dos direitos dos consumidores? De que forma PROCON, consumidores e empresas se relacionam diante do arbítrio de conflitos de interesses entre as partes?

A partir desta pergunta, foram feitas as seguintes sub-perguntas:

qual é o gênero dos reclamantes?
homens e mulheres tem diferentes taxas de reclamação?
quem ganha mais processos, homens ou mulheres?
quais são as faixas etárias mais afetadas?
quais são as faixas etárias que ganham mais processos?
quais são as faixas etárias e sexo que ganham mais processos?
quais são os tipos de problemas mais comuns? -como clusterizar os tipos de problemas? Podemos?
quais são as regiões mais afetadas por problemas?
quais são as regiões das pessoas que efetivamente ganham mais processos? (edited)
quais são as regiões das pessoas que efetivamente perdem mais processos? (edited)
dá pra saber de quais bairros pertencem as pessoas que ganham e perdem mais processos? Dá pra clusterizar?
dá pra saber a curva de crescimento das reclamações? -dá pra saber a curva de crescimento dos processos resolvidos com ganho de causa para o consumidor? -dá pra saber a curva de crescimento dos processos resolvidos com ganho de causa para as empresas?
dá pra saber a curva dos processos que foram para litígio na justiça? -dá pra saber a curva dos processos que foram para litígio na justiça e que tiveram ganho de causa para o consumidor? -dá pra saber a curva dos processos que foram para litígio na justiça e que tiveram ganho de causa para as empresas? -dá para saber as regiões onde os processos que foram para litígio na justiça tiveram ganho de causa para as empresas? Dá para investigar o por quê? Dá para saber se essa justiça é desonesta por algum fato jornalístico ou algo do tipo?
Transformação do Dataset:

Entre eles, #637.319 mulheres, #559.967 homens, #7.815 classificados como “N” e 971 não informados (Null). Os classificados como “N” ainda vamos averiguar se representam dados de pessoas que deliberadamente não quiseram informar o sexo.

Estados que fazem mais reclamações:

Os estados que apresentam mais reclamações são:

SP: 206059 PE: 113057 BA: 88537 MG: 83333 MS: 73054 ES: 73050 SC: 63001 RJ: 61869 GO: 52478 Al: 48943 CE: 46083 MT: 44256 PR: 39519 TO: 36211 RN: 34830 PB: 34664 MA: 22473 PA: 22388 DF: 18823 PI: 12029 AM: 9455 RO: 7607 AC: 6862 SE: 3570 AP: 2287 RS: 1634

Destas reclamações, 750.698 foram atendidas contra 455.374 não atendidas.
