import unittest
from CorporateData import CorporateData
from CorporateLog import CorporateLog
from InterfazParaAWS import InterfazParaAWS

class TestSingletonPattern(unittest.TestCase):
    def test_singleton_corporate_data(self):
        instance1 = CorporateData.getInstance()
        instance2 = CorporateData.getInstance()
        self.assertIs(instance1, instance2, "La clase CorporateData no mantiene una única instancia, no es un Singleton")

    def test_singleton_corporate_log(self):
        instance1 = CorporateLog.getInstance()
        instance2 = CorporateLog.getInstance()
        self.assertIs(instance1, instance2, "La clase CorporateLog no mantiene una única instancia, no es un Singleton")

class TestInterfazAWS(unittest.TestCase):
    def setUp(self):
        self.session_id = "test_session"
        self.cpu_id = "test_cpu"
        self.sede_id = "UADER-FCyT-IS2"
        self.interfaz = InterfazParaAWS(self.session_id, self.cpu_id)

    def test_valid_access(self):
        response = self.interfaz.consultar_datos_sede(self.session_id, self.cpu_id, self.sede_id)
        self.assertIn("datos_sede", response, "El acceso a los datos de la sede no fue exitoso, la clave 'datos_sede' no se encontró en la respuesta")

    def test_invalid_key_access(self):
        invalid_sede_id = "clave_incorrecta"
        response = self.interfaz.consultar_datos_sede(self.session_id, self.cpu_id, invalid_sede_id)
        self.assertIn("error", response, "El manejo de la clave incorrecta no fue adecuado, no se encontró el campo 'error' en la respuesta")

    def test_missing_arguments(self):
        # En este caso, se pasa un ID de sede vacío para probar el manejo de argumentos faltantes
        response = self.interfaz.consultar_datos_sede(self.session_id, self.cpu_id, "")
        self.assertIn("error", response, "No se gestionaron correctamente los argumentos faltantes, no se encontró el campo 'error' en la respuesta")

if __name__ == "__main__":
    unittest.main()