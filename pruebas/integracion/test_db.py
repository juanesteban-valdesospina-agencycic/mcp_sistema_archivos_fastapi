import pytest
from db import get_connection

def test_conexion_exitosa_a_base_de_datos():
    conn = None
    cursor = None
    try:
        conn, cursor = get_connection()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        assert resultado is not None
        assert list(resultado.values())[0] == 1
    finally:
        cursor.close()
        conn.close()
