import unittest
from InterfazParaAWS import InterfazParaAWS

class TestInterfazParaAWS(unittest.TestCase):

    def setUp(self):
        # Inicialización de la interfaz de AWS
        self.aws_interface = InterfazParaAWS()
        
        # Establecer datos de prueba usando métodos setter si están disponibles
        self.aws_interface.setCorporateData({"id": 1, "name": "Empresa XYZ", "balance": 1000.75})
        self.aws_interface.setCUIT("20-12345678-9")
        self.aws_interface.setSeqID("SEQ123456")

    def test_getCUIT_correct_value(self):
        # Verificar que el CUIT se obtiene correctamente
        self.assertEqual(self.aws_interface.getCUIT(), "20-12345678-9")

    def test_getCUIT_no_value(self):
        # Verificar que devuelve None si el CUIT no se ha establecido
        self.aws_interface.setCUIT(None)
        self.assertIsNone(self.aws_interface.getCUIT())

    def test_getSeqID_correct_value(self):
        # Verificar que el SeqID se obtiene correctamente
        self.assertEqual(self.aws_interface.getSeqID(), "SEQ123456")

    def test_getSeqID_empty_value(self):
        # Verificar que se maneja un SeqID vacío correctamente
        self.aws_interface.setSeqID("")
        self.assertEqual(self.aws_interface.getSeqID(), "")

    def test_getCorporateData_correct_value(self):
        # Verificar que los datos corporativos se obtienen correctamente
        self.assertEqual(self.aws_interface.getCorporateData(), {"id": 1, "name": "Empresa XYZ", "balance": 1000.75})

    def test_getCorporateData_no_data(self):
        # Verificar que se devuelve None si los datos corporativos no se han establecido
        self.aws_interface.setCorporateData(None)
        self.assertIsNone(self.aws_interface.getCorporateData())

if __name__ == "__main__":
    unittest.main()
