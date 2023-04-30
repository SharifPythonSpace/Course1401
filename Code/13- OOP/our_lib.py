
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

class shakhs():
   
    def __init__(self,name,family):
        self.name= name
        self.family= family
class ketab_khoon(shakhs):
    
    def __init__(self, meli, nam, name_khanevadegi):
        self.code_meli = meli
        super().__init__(name_khanevadegi,nam)
        self.ketabha = []
    def che_ketabi_amanat_gerefteh(self):
        return self.ketabha
    
    def amant_gerefan(self,name_ketab):
        self.ketabha.append(name_ketab)
    
class ketabkhooneh(object):
    def __init__(self):
        self.tedad_saloon_motaleh =0
        self.moozoate_ketab=[]
        self.tedade_aza=0
        self.addres_ketabkhooneh=''
        self.tedade_ghafaseh=0
        self.saate_bazoo_baste_shodan=()
        self.list_aza=0
        self.hazine_sabte_nam=0
        self.zarfiat=0
    def sakhte_salon(self,tedad,zarfiat):
        self.tedad_saloon_motaleh+=tedad
        self.zarfiat=zarfiat
        print("saloon ha sakhte shood")
    def sabt_e_ketabkhooneh(self,address):
        self.addres_ketabkhooneh=address
    def takhassos_e_ketabkhoone(self,mozooat):
        self.moozoate_ketab=mozooat

ketabkhoone_zahra=ketabkhooneh()
ketabkhoone_zahra.sabt_e_ketabkhooneh('sharif university')
ketabkhoone_zahra.takhassos_e_ketabkhoone(['math','pyisics','ce'])
ketabkhoone_zahra.sakhte_salon(4,100)
print(ketabkhoone_zahra.zarfiat)

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