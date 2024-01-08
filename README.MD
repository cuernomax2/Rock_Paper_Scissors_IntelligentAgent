# Agente Inteligente para RPS

Mateo Manuel González Ulla - IES de Teis - 01/2024

### El problema

Estudio de la solución del juego **piedra, papel, tijeras** a través de un agente inteligente programado en Python

### Contorno de tareas

| Contorno de tareas |  Observable  | Agentes | Determinista | Episódico | Estático | Discreto | Conocido |
| :-----------------: | :----------: | :-----: | :----------: | :--------: | :-------: | :------: | :-------: |
|         RPS         | Parcialmente observable |  Multiagente  | Estocástico | Si | Si | Si | Si |

* **Parcialmente Observable:** No se puede saber qué piensa el agente rival.
* **Multiaxente:** Existen dos jugadores (agentes) que se enfrentan.
* **Estocástico:** Las acciones del agente varían el resultado en cada partida.
* **Episódico:** Cada partida es "independiente" de la anterior.
* **Estático:** El medio no cambia mientras el usuario piensa su acción.
* **Discreto:** Las variables a tener en cuenta son limitadas y discretas.
* **Coñecido:** Sabemos las reglas del juego en todo momento y no cambian.

### Estructura del Agente

Una vez se conoce en profundidad el entorno de trabajo del agente, es posible definir con mayor precisión la estructura que este tomará. En este caso se ha optado por utilizar un programa de agente inteligente basado en modelos. 

![img](media/rps_model.png)

El agente utiliza una estadística para las tres primeras rondas  sobre los movimientos más utilizados por los americanos (véanse las imágenes adjuntas). De este modo se intenta predecir cuál será el primer movimiento del rival y jugar en base a ese resultado, intentando siempre ganar.

![img](media/percentage-of-americans-who-chose-rock-paper-or-scissors-v0-0mfued6gvrxa1.webp)
![img](media/0ka5828l0er91.webp)

