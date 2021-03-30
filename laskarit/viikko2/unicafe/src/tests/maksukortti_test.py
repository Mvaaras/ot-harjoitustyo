import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_maksukortin_summa_on_aluksi_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 12.0")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 8.0")
    
    def test_rahan_ottaminen_ei_vie_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_ottaminen_onnistuneesti_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
    
    def test_rahan_ottamisen_epaonnistuminen_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)