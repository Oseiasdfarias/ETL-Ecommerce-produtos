import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import sqlite3
import plotly.express as px



class Dashboard:
    """
    Classe que implementa a aminação do Aeropêndulo.

    Atributo:
        estrutura_db: Cria a estrutura do Dashboard.
    """
    def __init__(self, df) -> None:
        """
        Iniciador da classe.

        Args:
            df: DataFrame pandas com os dados para serem mostrados no Dashboard.
        Returns:
            Renorna um None.
        """
        self.df = df
        self.pg_title = "Pesquisa de Mercado - Tênis Esportivos no Mercado Livre"
        st.set_page_config(page_title=self.pg_title,
                           layout="wide",
                           initial_sidebar_state="collapsed")
        self.pages = ["Docs", "Portfólio", "LinkedIn", "GitHub"]
        self.styles = {
            "nav": {
                "background-color": "#44475a",
            },
            "div": {
                "max-width": "32rem",
            },
            "span": {
                "border-radius": "0.5rem",
                "color": "#EFEFEF",
                "margin": "0 0.125rem",
                "padding": "0.4375rem 0.625rem",
            },
            "active": {
                "background-color": "rgba(255, 255, 255, 0.25)",
            },
            "hover": {
                "background-color": "rgba(255, 255, 255, 0.35)",
            }
        }
        self.options = {
            "show_menu": False,
            "show_sidebar": False,
        }

        self.urls = {
            "Docs": "#",
            "GitHub": "https://github.com/Oseiasdfarias/ETL-Ecommerce-produtos",
            "LinkedIn": "https://www.linkedin.com/in/oseiasfarias/",
            "Portfólio": "https://oseiasfarias.info"}
        self.page = st_navbar(self.pages, styles=self.styles,
                        urls=self.urls, options=self.options)

        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')
        self.estrutura_db()


    def estrutura_db(self):
        """Método responável por implementar a estrutura do Dashboard."""
        # Melhorar o layout com colunas para KPIs
        st.subheader("KPIs Principais")
        col1, col2, col3 = st.columns(3)

        # KPI 1: Número total de itens
        total_items = self.df.shape[0]
        col1.metric(label="Número Total de Itens", value=total_items)

        # KPI 2: Número de marcas únicas
        unique_brands = self.df['brand'].nunique()
        col2.metric(label="Número de Marcas Únicas", value=unique_brands)

        # KPI 3: Preço médio novo (em reais)
        average_new_price = self.df['new_price'].mean()
        col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

        # Quais marcas são mais encontradas até a 10ª página
        st.subheader('Marcas mais encontradas até a 10ª página')
        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = (self.df['brand']
                            .value_counts()
                            .sort_values(ascending=False)
                            .to_frame()
                            .reset_index())
        fig = px.bar(top_10_pages_brands, x='brand', y='count', text_auto='.2s')
        col1.plotly_chart(fig)
        col2.write(top_10_pages_brands)


        # Qual o preço médio por marca
        st.subheader('Preço médio por marca')
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = (self.df.groupby('brand')
                                ['new_price']
                                .mean()
                                .sort_values(ascending=False)
                                .to_frame()
                                .reset_index())
        fig1 = px.bar(average_price_by_brand, x='brand',
                    y='new_price', text_auto='.2s')
        col1.plotly_chart(fig1)
        col2.write(average_price_by_brand)

        # Qual a satisfação por marca
        st.subheader('Satisfação por marca')
        col1, col2 = st.columns([4, 2])
        df_non_zero_reviews = self.df[self.df['reviews_rating_number'] > 0]
        satisfaction_by_brand = (df_non_zero_reviews
                                .groupby('brand')
                                ['reviews_rating_number']
                                .mean()
                                .sort_values(ascending=False)
                                .to_frame()
                                .reset_index())
        fig2 = px.bar(satisfaction_by_brand, x='brand',
                    y='reviews_rating_number', text_auto='.2s')
        col1.plotly_chart(fig2)
        col2.write(satisfaction_by_brand)


if __name__ == "__main__":
    # Conectando ao banco de dados SQLite3
    # Usando gerenciador de contexto para a conexão com o banco de dados
    with sqlite3.connect("./data/quotes.db") as conn:
        # Carregando a base de dados da tabela "mercadolivre_items" em um DataFrame Pandas
        df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

    dash = Dashboard(df)
