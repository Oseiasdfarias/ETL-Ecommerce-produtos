
<p align="center">
  <img height="90px" src="https://logodownload.org/wp-content/uploads/2016/08/mercado-livre-logo-0-1.png">
</p>

<p align="center" style="font-size:1.5vw">
  • <a href="#techs">Tecnologias</a>
  • <a href="#id1"> Solução </a>
  • <a href="#id9"> Rede Social </a>
</p>

<h3  id="techs">Tecnologias</h3>

<p align=center> <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white""> <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"> <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white"> <img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  </ul>
  <br>
</p>



<h1>ETL E-commerce Mercado Livre</h1>



Proposta do Projeto

Imagine que uma marca de tênis deseja avaliar sua relevância no ecossistema do Mercado Livre. Para isso, é necessário obter KPIs relacionadas ao segmento de tênis na plataforma. O objetivo é coletar informações detalhadas e implementar um dashboard que facilite a visualização e análise desses dados.

Sua equipe de Dados ficou responsável por realizar esse projeto.


---

<h2 id="id1">Solução do problema de negócio</h2>

<h3>Etapas</h3>

+ Etapa 1: Extração dos dados usanda Web Scraping
+ Etapa 2: Transformação dos dados usando Pandas
+ Etapa 3: Carregamento dos dados em uma banco de dados SQLite3
+ Etapa 4: Consumindo os dados usando uma Dashboard com Streamlit


<h2 id="id1">Como executar o Projeto</h2>

Primeiramente, acesse a pasta do projeto e instale as dependências usando o pip ou o Poetry. Para isso, execute um dos comandos abaixo:

`
poetry install
`
ou 
`pip install -r requirements.txt`


Agora em seguida, para executar cada etapa, siga as instruções abaixo:


<h3>Extração dos dados usanda Web Scraping</h3>


`
    scrapy crawl mercadolivre -o ../data/data.json
`


<h3>Transformar e carregar</h3>

`
     python src/transformacao/main.py
`



<h3>Visualizar Dashbard</h3>

`
     streamlit run src/dashboard/app.py
`


<h3  id="id9">🎥 Rede Social</h3>

<p align=center> <a href="https://oseiasfarias.info"><img src="https://img.shields.io/badge/Portfólio-%230077B5.svg?style=for-the-badge&logoColor=white"></a> <a href="https://www.linkedin.com/in/oseiasfarias/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://oseiasfarias.medium.com"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"></a>
<a href="https://www.kaggle.com/osiasdfarias"><img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"></a>
</p>