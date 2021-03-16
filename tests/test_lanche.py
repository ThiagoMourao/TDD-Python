import unittest
from lanche import lanche

class TestLanche(unittest.TestCase):
    def test_lanche_deve_levantar_assertionError_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            lanche(0)

    def test_lanche_deve_retornar_Lanche_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Lanche completo!'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(lanche(entrada),saida)

    def test_lanche_deve_retornar_Fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome!'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(lanche(entrada),saida)
        

if __name__ =='__main__':
    unittest.main(verbosity=2)