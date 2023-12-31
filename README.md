### <h1 align="center"> Da Bike ao Código: Explorando Dados Esportivos do Strava </h1>


![Capa-Strava](https://github.com/bonfimdoprado/STRAVA/assets/119675645/80aed326-3649-4be8-8b40-8dfb72124462)


## Descrição do Projeto </h1>
Este projeto tem como foco a extração, limpeza e preparação dos dados esportivos do Strava, seguido por análises exploratórias e a criação de dashboards interativos. Além de explorar os dados, o projeto visa melhorar a experiência do usuário ao oferecer um sistema de recomendações personalizadas de rotas para pedaladas em Guaxupé/MG, facilitadas por um executável (.exe) que simplifica o processo de busca. Em resumo, o projeto não apenas analisa dados esportivos, mas também enriquece a experiência do usuário com informações úteis e recomendações práticas.

## Informações do Projeto:

### 1 - Extração dos dados
Nesta primeira etapa foi criado três extratores utilizando o método  web scraping da biblioteca Selenium.
  1. O extrator de todas as minhas atividades gravadas no Strava foi o mais complexo do projeto, resultando na extração de um total de 1130 atividades. A complexidade aqui surgiu porque quando eu concluía a extração de dados de uma atividade e retornava à página anterior, o site automaticamente me redirecionava para a primeira página de atividades. Por esse motivo foi necessário desenvolver uma lógica que permitia ao extrator rastrear em que atividade ele havia parado e, consequentemente, determinar em qual página ele deveria continuar a extração. Em outras palavras, quando o processo estava prestes a atingir as últimas atividades, o extrator precisava 'clicar' repetidamente para avançar de página e garantir que estivesse extraindo os dados da página correta.
  2. O extrator dos KOM (King of Mountain), esse extrator buscava os dados dos segmentos que eu estava em 1º lugar no dia da extração dos dados.
  3. Por último, o extrator dos TOP 10, esse extrator buscava os dados dos segmentos que eu estava entre os 10 primeiros no dia da extração dos dados.

### 2 - Limpeza e Tratamento dos dados
Nesta etapa, realizei o tratamento dos dados, formatei as datas e adicionei novas colunas para análises posteriores.

### 3 - Dashboard Interativo em Power BI
Criei este primeiro dashboard, que ainda é provisório. Neste dashboard tem análises gerais dos meus dados esportivos. Este dashboard é interativo, onde pode filtrar os dados no menu lateral esquerdo.
![powerbi](https://github.com/bonfimdoprado/Projeto-Strava/assets/119675645/08ae8bbf-f632-40f4-a2c3-aa797b0ccc8d)


### 4 - Recomendação de Rotas
Este script em Python foi desenvolvido como parte de um sistema de recomendação de rotas para pedalada em Guaxupé/MG, usando dados do Strava. O código estabelece margens para encontrar atividades semelhantes dentro do banco de dados existente.,  solicita entrada do usuário para novos dados e encontra atividades semelhantes no banco de dados. As recomendações são filtradas por distância, elevação e tempo de movimentação. O resulta são 5 atividades recomendadas pelo sistemta.
![codigo recomendacao](https://github.com/bonfimdoprado/Projeto-Strava/assets/119675645/27bdec7b-863e-45f6-8942-9e2ba0e7bf86)

Simplificando a busca por rotas de pedal, desenvolvi um executável (.exe) para evitar a necessidade de executar o código manualmente. Ao clicar no ícone, um prompt de comando será aberto, permitindo a inserção fácil dos dados para obter recomendações. Este executável oferece uma experiência mais amigável para os usuários que desejam encontrar rotas de forma rápida e intuitiva.
![exec recomendacao](https://github.com/bonfimdoprado/Projeto-Strava/assets/119675645/2824a75a-0229-4bd8-a9c2-9d8ccceee246)









