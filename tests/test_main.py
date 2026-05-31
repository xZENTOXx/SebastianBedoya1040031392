import pytest

from main import calcular_estadisticas


class TestCalcularEstadisticas:

    def test_media_correcta(self):
        resultado = calcular_estadisticas([1, 2, 3, 4, 5])
        assert resultado["media"] == 3.0

    def test_mediana_correcta_lista_impar(self):
        resultado = calcular_estadisticas([1, 2, 3, 4, 5])
        assert resultado["mediana"] == 3.0

    def test_mediana_correcta_lista_par(self):
        resultado = calcular_estadisticas([1, 2, 3, 4])
        assert resultado["mediana"] == 2.5

    def test_minimo_y_maximo(self):
        resultado = calcular_estadisticas([10, 25, 3, 47])
        assert resultado["minimo"] == 3.0
        assert resultado["maximo"] == 47.0

    def test_desviacion_estandar(self):
        resultado = calcular_estadisticas([2, 4, 4, 4, 5, 5, 7, 9])
        assert round(resultado["desviacion_estandar"], 4) == 2.0

    def test_un_solo_elemento(self):
        resultado = calcular_estadisticas([42])
        assert resultado["minimo"] == 42.0
        assert resultado["maximo"] == 42.0
        assert resultado["media"] == 42.0
        assert resultado["mediana"] == 42.0
        assert resultado["desviacion_estandar"] == 0.0

    def test_numeros_negativos(self):
        resultado = calcular_estadisticas([-10, -5, 0, 5, 10])
        assert resultado["media"] == 0.0
        assert resultado["minimo"] == -10.0
        assert resultado["maximo"] == 10.0

    def test_lista_vacia_lanza_excepcion(self):
        with pytest.raises(ValueError, match="no puede estar vacía"):
            calcular_estadisticas([])

    def test_retorna_todas_las_claves(self):
        resultado = calcular_estadisticas([1, 2, 3])
        claves_esperadas = {"minimo", "maximo", "media", "mediana", "desviacion_estandar"}
        assert set(resultado.keys()) == claves_esperadas

    def test_valores_son_float(self):
        resultado = calcular_estadisticas([1, 2, 3])
        for valor in resultado.values():
            assert isinstance(valor, float)
