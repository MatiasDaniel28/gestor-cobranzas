

import json


def guardar_consultas(consultas, ruta="consultas.json"):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                consultas,
                archivo,
                default=str,
                ensure_ascii=False,
                indent=4,
            )

    except OSError:
        print("No se pudieron guardar las consultas.")
        return False

    return True