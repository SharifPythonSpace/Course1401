
class ketab:

    def __init__(self, onvan, nevisande, tedade_safeh, nasher, vazeiyat = 'mojood'):
        self.onvan = onvan
        self.nevisande = nevisande
        self.tedad_safeh = tedade_safeh
        self.nasher = nasher
        self.vazeiyat = vazeiyat

    def amanat_gereftan(self):
        self.vazeiyat = 'namojood'
    
    def pasdadan(self):
        self.vazeiyat = 'mojood'
    
    def onvan_begoo(self):
        return self.onvan


class ketab_khoon:
    
    def __init__(self, meli, nam, name_khanevadegi):
        self.code_meli = meli
        self.nam= nam
        self.name_khanevadegi = name_khanevadegi
        self.ketabha = []
    def che_ketabi_amanat_gerefteh(self):
        return self.ketabha
    
    def amant_gerefan(self,name_ketab):
        self.ketabha.append(name_ketab)
    


cheshmhayash = ketab('cheshmhayash', 'bozorg alavi', 343, 'sales')
cheshmhayash.amanat_gereftan()
print(cheshmhayash.vazeiyat)

cheshmhayash1 = ketab('cheshmhayash1', 'bozorg alavi', 343, 'sales')

cheshmhayash.pasdadan()
print(cheshmhayash.vazeiyat)


mahya_ketabkhoon = ketab_khoon(1234, 'Mahya', 'lotfi')
mahya_ketabkhoon.amant_gerefan('cheshmayash')
mahya_ketabkhoon.amant_gerefan('olum')

print(mahya_ketabkhoon.che_ketabi_amanat_gerefteh())

print('hello')