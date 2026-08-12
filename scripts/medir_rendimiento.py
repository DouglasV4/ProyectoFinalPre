import json
import time
import urllib.request
import urllib.error


URL = "http://127.0.0.1:8000/ask"

PAYLOAD = {
    "pregunta": "¿Qué vehículos están disponibles?"
}

NUM_SOLICITUDES = 20


def calcular_percentil(datos, percentil):
    datos = sorted(datos)

    posicion = (len(datos) - 1) * (percentil / 100)

    inferior = int(posicion)
    superior = min(inferior + 1, len(datos) - 1)

    peso = posicion - inferior

    return (
        datos[inferior]
        + (datos[superior] - datos[inferior]) * peso
    )


def realizar_solicitud():
    datos = json.dumps(PAYLOAD).encode("utf-8")

    request = urllib.request.Request(
        URL,
        data=datos,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    inicio = time.perf_counter()

    try:
        with urllib.request.urlopen(request, timeout=10) as response:

            response.read()

            fin = time.perf_counter()

            duracion_ms = (fin - inicio) * 1000

            return {
                "status": response.status,
                "duration_ms": duracion_ms,
                "error": None
            }

    except urllib.error.HTTPError as error:

        fin = time.perf_counter()

        duracion_ms = (fin - inicio) * 1000

        return {
            "status": error.code,
            "duration_ms": duracion_ms,
            "error": f"HTTP {error.code}"
        }

    except Exception as error:

        fin = time.perf_counter()

        duracion_ms = (fin - inicio) * 1000

        return {
            "status": None,
            "duration_ms": duracion_ms,
            "error": type(error).__name__
        }


def main():

    resultados = []

    print("=" * 60)
    print("MEDICIÓN DE RENDIMIENTO - RENTCAR AI")
    print("=" * 60)

    print(f"Endpoint: {URL}")
    print(f"Solicitudes: {NUM_SOLICITUDES}")
    print()

    for numero in range(1, NUM_SOLICITUDES + 1):

        resultado = realizar_solicitud()

        resultados.append(resultado)

        print(
            f"Solicitud {numero:02d} | "
            f"status={resultado['status']} | "
            f"duracion={resultado['duration_ms']:.2f} ms"
        )

    tiempos = [
        resultado["duration_ms"]
        for resultado in resultados
    ]

    exitosas = [
        resultado
        for resultado in resultados
        if resultado["status"] == 200
    ]

    errores = [
        resultado
        for resultado in resultados
        if resultado["status"] != 200
    ]

    p50 = calcular_percentil(tiempos, 50)
    p95 = calcular_percentil(tiempos, 95)
    maximo = max(tiempos)

    tasa_error = (
        len(errores) / len(resultados)
    ) * 100

    resumen = {
        "endpoint": URL,
        "solicitudes": len(resultados),
        "exitosas": len(exitosas),
        "errores": len(errores),
        "p50_ms": round(p50, 2),
        "p95_ms": round(p95, 2),
        "max_ms": round(maximo, 2),
        "tasa_error_porcentaje": round(tasa_error, 2)
    }

    print()
    print("=" * 60)
    print("RESULTADOS")
    print("=" * 60)

    print(f"Solicitudes: {resumen['solicitudes']}")
    print(f"Exitosas: {resumen['exitosas']}")
    print(f"Errores: {resumen['errores']}")
    print(f"p50: {resumen['p50_ms']} ms")
    print(f"p95: {resumen['p95_ms']} ms")
    print(f"Máximo: {resumen['max_ms']} ms")
    print(f"Tasa de error: {resumen['tasa_error_porcentaje']} %")

    with open(
        "scripts/resultados_rendimiento.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            {
                "resultados": resultados,
                "resumen": resumen
            },
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print()
    print("Resultados guardados en:")
    print("scripts/resultados_rendimiento.json")


if __name__ == "__main__":
    main()