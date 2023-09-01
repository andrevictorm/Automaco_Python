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


class TabjogoSpider(scrapy.Spider):
    name = 'tabjogo'
    start_urls = ['http://example.com/']

    def parse(self, response):
        for jogo in response.css('td.collection_rank').get():
            yield{
            'rank':jogo.css('td.collection_rank>a::attr(name)').get(),
            'nome':jogo.css('a.primary::text').get(),
            'ano':jogo.css('span.smallerfont.dull::text').get(),
            'geek_voto':jogo.css('#row_ .collection_bggrating:nth-child(4)::text').get().split(),
            'medvoto':jogo.css('#row_ .collection_bggrating:nth-child(5)::text').get().split()[0],
            'n_voto':jogo.css('#row_ .collection_bggrating~ .collection_bggrating+ .collection_bggrating::text').get().split()[0]
            }

