import re

class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self._validaURL()
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self.url = url.strip()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def _validaURL(self):
        if not self._url:
            raise ValueError("A URL está vazia!")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self._url)
        if not match:
            raise ValueError("A URL não é válida!")
        
    def get_url_base(self):
        indice_interrogacao = self._url.find('?')
        return self._url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self._url.find('?')
        return self._url[indice_interrogacao+1:]
    
    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self._url)

    def __str__(self):
        return self._url + "\n" +"Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, outro_url):
        return self._url == outro_url.url