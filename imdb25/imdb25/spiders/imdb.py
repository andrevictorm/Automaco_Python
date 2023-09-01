#CD para ir até o diretorio, MKDIR para criar a pasta

#para criar ambiente virtual na pasta do projeto>>> conda create -n [NOMEDOPROJETO] python=3.6

#Para ativar ambiente virtual, logo depois da instalação, use esse comando>>> conda activate [NOMEDOPROJETO]

#Na pasta que for criar o projeto, instale o scrapy >> pip install scrapy

#Começa com promt anaconda colocando no endereço desejado de criação >>> scrapy startproject [nomedoprojeto]

#Depois criar spider com nome do projeto e endereço que será extraido >>> scrapy genspider [nomedoprojeto] [site]

#depois utilizar o comando (scrapy shell) para realizar comandos para visualização 

#Utilize o comando a seguir para se conectar na pagina que deseja realizar a extração>>> fetch('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

#Depois que analisar o lugar exato que quer extrair a informação

# utilize o comando para visualização >>>> response.css('NOMEDOLUGAR').getall() / get

#no final, no prompt, para rodar, insira o codigo scrapy crawl (nomedoprojeto) -O
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filme in response.css('tr'):
            yield{
                'nome': filme.css('td.titleColumn>a::text').get(),
                'ano': filme.css('span.secondaryInfo::text').get(),
                'nota': filme.css('strong::text').get()
            }
        
        pass
