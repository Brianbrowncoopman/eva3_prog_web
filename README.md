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


