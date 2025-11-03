import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_ei_voi_lisata_negatiivista(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), self.varasto.tilavuus)

    def test_varastoon_voi_lisata_tasan_tilavuuden_verran(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_varastoon_ei_voi_lisata_enemman_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_voi_ottaa_enemman_kuin_siella_on(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(1), 0)

    def test_varastosta_ei_voi_ottaa_negatiivista(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
    
    def test_varasto_printtaa_oikean_saldon_ja_tilan(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
    def test_varaston_luominen_negatiivisella_tilavuudella_nollaa_tilavuuden(self):
        self.virhe_varasto = Varasto(-1)
        self.assertAlmostEqual(self.virhe_varasto.tilavuus, 0)

    def test_varaston_luominen_negatiivisella_saldolla_nollaa_saldon(self):
        self.virhe_varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.virhe_varasto.saldo, 0)
    
    def test_varastoa_luodessa_saldo_ei_ole_isompi_kuin_tilavuus(self):
        self.virhe_varasto = Varasto(10, 11)
        self.assertAlmostEqual(self.virhe_varasto.saldo, 10)
    
    def test_varastoa_luodessa_saldo_joka_on_pienempi_kuin_tilavuus_lisataan_oikein(self):
        self.virhe_varasto = Varasto(10, 5)
        self.assertAlmostEqual(self.virhe_varasto.saldo, 5)
