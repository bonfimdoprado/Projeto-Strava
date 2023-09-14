### <h1 align="center"> Da Bike ao Código: Explorando Dados Esportivos do Strava </h1>


![Capa-Strava](https://github.com/bonfimdoprado/STRAVA/assets/119675645/80aed326-3649-4be8-8b40-8dfb72124462)


## Descrição do Projeto </h1>
Este projeto tem como objetivo fazer a extração dos meus dados esportivos, realizar a limpeza e preparação dos dados, explorar os dados por meio de análises exploratórias, fazer um predição dos dados e criar dashboards interativos.

## Informações do Projeto:

### 1 - Extração dos dados
Nesta primeira etapa foi criado três extratores utilizando o método  web scraping da biblioteca Selenium.
  1. O extrator de todas as minhas atividades gravadas no Strava foi o mais complexo do projeto, resultando na extração de um total de 1130 atividades. A complexidade aqui surgiu porque quando eu concluía a extração de dados de uma atividade e retornava à página anterior, o site automaticamente me redirecionava para a primeira página de atividades. Por esse motivo foi necessário desenvolver uma lógica que permitia ao extrator rastrear em que atividade ele havia parado e, consequentemente, determinar em qual página ele deveria continuar a extração. Em outras palavras, quando o processo estava prestes a atingir as últimas atividades, o extrator precisava 'clicar' repetidamente para avançar de página e garantir que estivesse extraindo os dados da página correta.
  2. O extrator dos KOM (King of Mountain), esse extrator buscava os dados dos segmentos que eu estava em 1º lugar no dia da extração dos dados.
  3. Por último, o extrator dos TOP 10, esse extrator buscava os dados dos segmentos que eu estava entre os 10 primeiros no dia da extração dos dados.



EM CONSTRUÇÃO....



