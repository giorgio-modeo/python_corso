from nonAlimenti import NonAlimento 
from alimento import Alimento
class GestioneProdotto():
    def __init__(self):
        self._elenco = []

    def aggiungiProdotto(self, prodotto):
        self._elenco.append(prodotto)

    def stampaProdotti(self):
        for prodotto in self._elenco:
            print("\n",prodotto)
            
    def costoTotale(self):
        totale = 0
        for prodotto in self._elenco:
            totale += prodotto.getPrezzo()
        return f"\ntotale: {totale}"
    
    def confronto_per_categoria(self):
        elenco_categoria = []
        for prodotto in self._elenco:
            if isinstance(prodotto, NonAlimento):
                elenco_categoria.append(prodotto)
                elenco_categoria.sort(key=lambda x: x.getCategoria())
                print(elenco_categoria)
            else:
                return ""
            


    def __eq__(self, other):
        return self._elenco[0] == other._elenco[1]

lista = ["abbigliamento","elettronica","altro","libri","non lo so"]
elenco = GestioneProdotto()
for i in range(5):
    a = NonAlimento( f"test{i}", f"test{i}", i*10, 1, lista[i], i/1.2)
    a.setCode(a.getCode()+i)
    elenco.aggiungiProdotto(a)



print(elenco._elenco[1] == elenco._elenco[1])
