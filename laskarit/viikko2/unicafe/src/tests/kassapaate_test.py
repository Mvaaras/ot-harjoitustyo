import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.paate.kassassa_rahaa,100000)
    
    def test_luodun_kassapaatteen_myytyjen_edullisten_annosten_maara_on_oikea(self):
        self.assertEqual(self.paate.edulliset,0)
    
    def test_luodun_kassapaatteen_myytyjen_maukkauden_annosten_maara_on_oikea(self):
        self.assertEqual(self.paate.maukkaat,0)

    def test_onnistunut_edullinen_kateisosto_lisaa_rahaa_kassaan(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa,100240)
    
    def test_onnistunut_maukas_kateisosto_lisaa_rahaa_kassaan(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa,100400)
    
    def test_onnistunut_edullinen_kateisosto_palauttaa_oikean_vaihtorahan(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(500),260)
    
    def test_onnistunut_maukas_kateisosto_lisaa_rahaa_kassaan(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(500),100)
    
    def test_onnistunut_edullinen_kateisosto_lisaa_myytyjen_edullisten_maaraa(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.edulliset,1)
    
    def test_onnistunut_maukas_kateisosto_lisaa_myytyjen_maukkaiden_maaraa(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.maukkaat,1)

    def test_epaonnistunut_edullinen_kateismaksu_ei_lisaa_rahaa_kassaan(self):
        self.paate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.paate.kassassa_rahaa,100000)
    
    def test_epaonnistunut_maukas_kateismaksu_ei_lisaa_rahaa_kassaan(self):
        self.paate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.paate.kassassa_rahaa,100000)
    
    def test_epaonnistunut_edullinen_kateismaksu_ei_lisaa_myytyjen_maaraa(self):
        self.paate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.paate.edulliset,0)
    
    def test_epaonnistunut_maukas_kateismaksu_ei_lisaa_myytyjen_maaraa(self):
        self.paate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.paate.maukkaat,0)
    
    def test_epaonnistunut_edullinen_kateismaksu_palauttaa_kaiken_vaihtorahana(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(100),100)
    
    def test_epaonnistunut_maukas_kateismaksu_palauttaa_kaiken_vaihtorahana(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(100),100)
    
    #Tuon edellisen jälkeen päätin tehdä ensin edulliset, sitten maukkaat. Tulee vähemmän sotku.

    #Kortin oletetaan toimivan oikein koska sitä on jo testattu onnistuneesti

    def test_onnistunut_edullinen_korttimaksu_veloittaa_summan_kortilta(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)
    
    def test_onnistunut_edullinen_korttimaksu_nostaa_myytyjen_maaraa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 1)
    
    def test_onnistunut_edullinen_korttimaksu_palauttaa_true(self):
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti), True)
    
    def test_epaonnistunut_edullinen_korttimaksu_ei_velota_kortilta(self):
        self.kortti.ota_rahaa(800)
        self.paate.syo_edullisesti_kortilla(self.kortti) #200
        self.assertEqual(self.kortti.saldo, 200)
    
    def test_epaonnistunut_edullinen_korttimaksu_ei_lisaa_myytyja(self):
        self.kortti.ota_rahaa(800)
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset,0)

    def test_epaonnistunut_edullinen_korttimaksu_palauttaa_false(self):
        self.kortti.ota_rahaa(800)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti),False)
    
    def test_edullinen_korttimaksu_ei_muuta_kassan_rahamaaraa(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa,100000)



    def test_onnistunut_maukas_korttimaksu_veloittaa_summan_kortilta(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)
    
    def test_onnistunut_maukas_korttimaksu_nostaa_myytyjen_maaraa(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 1)
    
    def test_onnistunut_maukas_korttimaksu_palauttaa_true(self):
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_epaonnistunut_maukas_korttimaksu_ei_velota_kortilta(self):
        self.kortti.ota_rahaa(800)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 200)
    
    def test_epaonnistunut_maukas_korttimaksu_ei_lisaa_myytyja(self):
        self.kortti.ota_rahaa(800)
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat,0)

    def test_epaonnistunut_maukas_korttimaksu_palauttaa_false(self):
        self.kortti.ota_rahaa(800)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti),False)
    
    def test_maukas_korttimaksu_ei_muuta_kassan_rahamaaraa(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa,100000)
    
    #kortin lataus

    def test_kortin_lataaminen_lisaa_rahaa_kortille(self):
        self.paate.lataa_rahaa_kortille(self.kortti,500)
        self.assertEqual(self.kortti.saldo,1500)
    
    def test_kortin_lataaminen_lisaa_rahaa_kassaan(self):
        self.paate.lataa_rahaa_kortille(self.kortti,500)
        self.assertEqual(self.paate.kassassa_rahaa,100500)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,-500)
        self.assertEqual(self.kortti.saldo,1000)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa_kassapaate(self):
        self.paate.lataa_rahaa_kortille(self.kortti,-500)
        self.assertEqual(self.paate.kassassa_rahaa,100000)

        