#ACTA DE REUNION

##Objetivos

1.	Redacción del acta en la Wiki del grupo
2.	Ajustes de ASRs y tareas en la herramienta de planeación

##Entregables

•	Actualización de los modelos de arquitectura
•	Actualización de los ASRs en la herramienta de planeación
•	Experimento (esto es la implementación de una parte de los modelos de arquitectura que permita evidenciar el nivel de cumplimiento de los ASRs seleccionados)
•	Documentación de los escenarios de prueba
•	Implementación de pruebas
•	Reporte y análisis de los resultados de las pruebas
•	Reflexión sobre cómo la introducción de tácticas y patrones en este Sprint impactaron positiva o negativamente los atributos de calidad del Sprint anterior
•	Los puntos 4, 6 y 7 deben deben quedar consignados en la Wiki del repositorio.

##Especificación del ASR de integridad

“Como arquitecto de software, debo garantizar que, cuando un usuario ingrese a la aplicación y el sistema esté operando con normalidad, los usuarios no autorizados no puedan modificar datos de usuarios. Este requisito debe cumplirse el 99.99% de las veces."

##Especificación del ASR de confidencialidad

"Como arquitecto de software, debo garantizar que, cuando un usuario ingrese a la aplicación y el sistema esté operando con normalidad, los usuarios no autorizados no puedan acceder a la información sensible de otros usuarios. Este requisito debe cumplirse el 99.99% de las veces."

•	Diseño de arquitectura (plasmado al menos en una vista funcional y de despliegue) para direccionar los ASRs de confidencialidad e integridad

•	Diseño e implementación del experimento del ASR de integridad

•	Diseño e implementación del experimento del ASR de confidencialidad


•	Actualizar la Wiki para reflejar el diseño e implementación del experimento del ASR de integridad.


•	Actualizar la Wiki para reflejar el diseño e implementación del experimento del ASR de confidencialidad.


#Actas de reunión de equipo (seguimiento y retrospectiva)

##Seguimiento

Los miembros del equipo han completado todas las actividades asignadas durante el Sprint. Aquí están los detalles:


| Nombre              | Número de actividades asignadas | Número de actividades completadas | Comentarios y compromisos |
|---------------------|---------------------------------|-----------------------------------|---------------------------|
| Alejandro Pulido    | 1                               | 1                                 | Continuar con la eficiencia e implementación de los sprints |
| Johan Bautista      | 1                               | 1                                 | Mantener la comunicación constante y la implementación de pruebas |
| Nicolas Casas       | 1                               | 1                                 | Revisar diariamente el progreso del sprint y colaborar en lo que estemos atrasados |
| Marco Ramírez       | 1                               | 1                                 | Colaboración en problemas técnicos |
| Esteban Castelblanco| 1                               | 1                                 | Asegurarse de actualizar la documentación |


###Seguimiento grupal

1.	¿Cuál es el porcentaje de tareas completadas y SIN completar?

Se observa que el 100% de las tareas han sido completadas. Sin embargo, para continuar mejorando, cada miembro del equipo ha definido al menos una acción de mejora:





Con base en la tabla y la respuesta a la pregunta, el grupo identifica las dificultades que tiene y en la columna de “Comentarios y compromisos” cada uno define al menos una acción de mejora (concreta) para la próxima semana.

| Nombre              | Acciones de mejora sugeridas |
|---------------------|------------------------------|
| Alejandro Pulido    | Implementar herramientas de gestión de tareas para optimizar y monitorear la eficiencia de los sprints. |
| Johan Bautista      | Desarrollar talleres de capacitación en pruebas de software para mejorar la implementación de pruebas eficaces. |
| Nicolas Casas       | Establecer reuniones diarias breves para revisar el avance de los sprints y asignar recursos a tareas atrasadas. |
| Marco Ramírez       | Facilitar talleres de resolución de problemas para mejorar la colaboración en problemas técnicos. |
| Esteban Castelblanco| Implementar un sistema de gestión de conocimiento para mejorar y centralizar la actualización de la documentación. |

###Planeación de lo que falta del Sprint

Asegurar que cada ASR asignado tiene tareas claras, responsables definidos y una fecha de terminación adecuada es crucial. Utilizando azure para visualizar y gestionar estas tareas de manera eficiente.


## Retrospectiva de Sprint – Método de la Estrella de Mar

| Categoría             | Acciones                                        |
|-----------------------|-------------------------------------------------|
| **Comenzar a hacer**  | Mejorar la comunicación para la asignación de tareas. <br> Utilizar más Azure para revisar la gestión de tareas de cada integrante. <br> Sesiones de revisión rápida al final de cada semana. |
| **Más de**            | Uso de herramientas que logran los objetivos esperados. <br> Feedback continuo. <br> Responsabilidad y compromiso en las entregas. |
| **Dejar de hacer**    | Postergar las actualizaciones del documento. <br> Ignorar las necesidades de capacitación entre integrantes. <br> Retrasar decisiones críticas. |
| **Seguir haciendo**   | Revisiones de código. <br> Utilizar metodologías ágiles. <br> Retrospectivas efectivas. |
| **Menos de**          | No solicitar ayuda entre compañeros del grupo. <br> Sobrecarga para algunos integrantes. <br> Gestionar mejor el tiempo que hay para hacer las entregas. |



###Comparen las retrospectivas de Sprint 2 y Sprint 3 y respondan las siguientes preguntas:

· ¿Cuáles son las similitudes y diferencias entre las dos retrospectivas?

Ambos sprints enfatizaron la importancia de las revisiones de código y el uso de herramientas colaborativas.

· ¿Reflejan las diferencias alguna mejora en la dinámica de trabajo en equipo?

El Sprint 3 introdujo reuniones diarias de sincronización y propuso reducir las reuniones largas, reflejando una mejora en la eficiencia y comunicación del equipo.


· Si no hay mejoras, ¿cuáles son las barreras que impiden el mejoramiento continuo?

Las diferencias reflejan mejoras en la dinámica del equipo, mostrando un enfoque más estructurado y comunicativo. Sin embargo, la tendencia a postergar actualizaciones sigue siendo una barrera que necesita atención.

A partir de lo que colocaron en los ejes de la estrella de Sprint 3 (excepto el eje “Seguir haciendo”), cada integrante debe derivar acciones concretas para este Sprint y colocarlas en la siguiente tabla

#FALTA TABLA 

##Diseño y planeación Sprint 4

###ASR de Escalabilidad: 

"Como arquitecto de software, debo garantizar que el sistema pueda escalar de forma efectiva y eficiente para manejar un aumento en la demanda de usuarios durante los períodos pico, manteniendo un tiempo de respuesta consistente sin degradar la calidad del servicio."

###ASR de Disponibilidad: 

"Como arquitecto de software, debo asegurar que el sistema esté disponible y operativo el 99.99% del tiempo, minimizando el tiempo de inactividad y asegurando un acceso constante para los usuarios a los servicios críticos."

###Selección de bases de datos y tecnologías para microservicios

Bases de datos:

Para la escalabilidad - Base de datos NoSQL: podría ser útil por su capacidad para escalar horizontalmente y manejar grandes volúmenes de datos y tráfico intenso, lo cual es ideal para manejar la escalabilidad de servicios específicos que requieren alta disponibilidad y rendimiento.

Para la disponibilidad - Base de datos SQL: Ya que nos ofreceria consistencia y alta disponibilidad, lo que es crucial para mantener los servicios operativos durante fallos de red o hardware.
Tecnologías para implementar microservicios:

Contenedores Docker: 

Facilitan el despliegue rápido y consistente de microservicios, asegurando que el entorno de ejecución sea uniforme y aislado.

Kubernetes: 

Sistema de orquestación de contenedores que permite la gestión automatizada, escalabilidad y descubrimiento de servicios, fundamental para mantener la operatividad y eficiencia en la gestión de múltiples microservicios.

###Planificación de tareas para los ASRs

Tareas para ASR de Escalabilidad:

1.	Diseñar e implementar la arquitectura de microservicios utilizando Docker y Kubernetes para asegurar un despliegue eficiente y escalable.
2.	Configurar y optimizar una base de datos NoSQL para el servicio específico que maneje la mayor carga durante los picos de demanda.
3.	Realizar pruebas de carga para evaluar la capacidad de escalado del sistema y ajustar configuraciones.

Tareas para ASR de Disponibilidad:

1.	Implementar y configurar una base de datos SQL que garantice la disponibilidad de datos incluso en caso de fallo de una zona de disponibilidad.
2.	Establecer políticas de respaldo y recuperación ante desastres para garantizar la continuidad del negocio.
3.	Implementar monitorización y alertas para detectar y responder rápidamente a los fallos que puedan afectar la disponibilidad del sistema.

![image](https://github.com/LosFullStackOverflow/ASR3/assets/111070716/55d0aafe-faee-4ac3-821f-1ecdf1e68485)
