Evaluación 3 - Programación Web

Este trabajo corresponde a la Evaluación 3 de la asignatura de Programación Web.

Se solicita desarrollar una aplicación con Python y Flask. La aplicación inicia en una página de escritorio que muestra dos opciones, una para cada ejercicio.

Al hacer clic en la primera opción, se despliega un formulario para ingresar tres notas y un valor para el porcentaje de asistencia. 
Tras enviar el formulario, se calcula el promedio y se informa el estado, que puede ser "aprobado" o "reprobado" según los criterios definidos.

Al hacer clic en la segunda opción, se muestra un formulario para ingresar tres nombres. 
Se calcula cuál de los tres nombres tiene mayor cantidad de caracteres. Adicionalmente, si hay más de un nombre con la misma cantidad máxima de caracteres, se muestran todos esos nombres y la cantidad de caracteres correspondiente.

La aplicación cumple con los requisitos indicados, presenta resultados claros y maneja correctamente los casos especiales en ambos ejercicios.


Estructura de carpetas  
=========================



<img width="516" height="319" alt="image" src="https://github.com/user-attachments/assets/134d8cb4-ed5c-48d9-8923-5b034dfff21d" />


-main.py: archivo principal con la lógica de la aplicación Flask.

-static/css/estilos.css: archivo de estilos globales CSS para toda la aplicación.

-templates/base.html: plantilla base que carga los estilos y estructura.

-templates/home.html: página inicial donde se muestran ambas opciones (Ejercicio 1 y 2).

templates/form_notas1.html: formulario para las notas y asistencia, y resultados correspondientes.

templates/form_nombres.html: formulario para los nombres y resultado de longitud.

====================================================================================================
Para ejecutar la pagina se debe :
1ero) clonar el repositorio
2) en el shell se debe importat flask con "pip install Flask", fijandose en la uvicacion del proyecto
3) ejecutar el codigo 
====================================================================================================

Una vez cargada la pagina web. 

La pagina Home se debe ver de la siguiente manera
<img width="1911" height="950" alt="image" src="https://github.com/user-attachments/assets/3cfbcef4-004d-408c-9837-93d3eeb8e937" />

Al elegir la primera opcion se debe ver de la siguiente manera
<img width="1884" height="966" alt="image" src="https://github.com/user-attachments/assets/13cd3abe-e822-4ee6-9b7f-e6d84d6618bc" />

Al alimentar los imputs y ejecutar la pagian se ve de la siguiente manera
<img width="1874" height="953" alt="image" src="https://github.com/user-attachments/assets/2c3fd62c-7bae-4a22-91ad-e0b9a75e37f2" />

Al elegir la segunda opcion se ve de la siguiente manera
<img width="1865" height="784" alt="image" src="https://github.com/user-attachments/assets/a5255654-4d3f-48e9-84da-78d6b3b85054" />

Al poblar los imputs y ejecutar la pagian se ve de la siguiente manera 
<img width="1860" height="969" alt="image" src="https://github.com/user-attachments/assets/bc0d6382-a118-4b16-b28a-c8a391105aa0" />









