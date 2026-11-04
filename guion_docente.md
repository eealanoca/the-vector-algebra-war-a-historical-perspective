# Notas académicas y guion de desarrollo

**Ing. Elmer Efrain Alanoca Condori**  
Maestría en Ciencias de la Ingeniería Mecánica y Electromecánica  
Mecatrónica II

**The vector algebra war: a historical perspective**

## Organización

40 diapositivas principales y 22 apéndices técnicos. El cuerpo principal desarrolla el contenido y la lectura crítica del artículo. Las extensiones de cinemática de rotores, cambio de origen y sistemas generales de fuerzas se agrupan en los apéndices y se identifican como desarrollo propio.

## Convenciones

- Cl(3,0) euclídeo; I = e1 e2 e3 corresponde al j del artículo. J2 = e1 e2 identifica el bivector del plano de Cl2.
- Las rotaciones son activas; la velocidad angular de la extensión cinemática se expresa en el marco espacial.
- Los boosts usan rapidez adimensional y convención activa positiva.
- Maxwell se escribe en SI y en el vacío: se restituye 1/c en la derivada temporal y se conserva c en la proyección bivectorial.
- Dirac conserva la representación citada en la ecuación (21), con hbar = c = 1; ocho componentes reales no constituyen por sí solas una demostración de equivalencia.
- El momento mecánico r cruz f es el negativo de la coordenada axial f cruz r utilizada por el artículo.
- Coplanaridad, momento resultante y equilibrio se comprueban por separado.
- La fórmula de la inversa general solo se usa si su denominador central es no nulo.

## Desarrollo por diapositiva

### 1. Carátula

Identificar el título original y su traducción. La preparación corresponde a Ing. Elmer Efrain Alanoca Condori, para Mecatrónica II, dentro de la Maestría en Ciencias de la Ingeniería Mecánica y Electromecánica. Distinguir estos datos de la autoría del artículo de Chappell, Iqbal, Hartnett y Abbott. La portada utiliza la plantilla de título nativa de EastLansing.

### 2. Tesis y contribución del artículo

La contribución central es una síntesis histórica con una propuesta de lenguaje matemático. Las identidades y correspondencias algebraicas pueden verificarse directamente; la preferencia por un lenguaje universal es una posición metodológica de los autores. La presentación conservará esta distinción para evitar convertir una tesis interpretativa en un resultado experimental.

**Fuente y alcance:** [C16], resumen, secc. I y V, pp. 1 y 6--7.

### 3. Estructura del argumento

La progresión va de los criterios de comparación a la construcción matemática y termina en sus aplicaciones y límites. Los cálculos de componentes, ejemplos elementales y demostraciones complementarias están agrupados en apéndices. El cuerpo principal prioriza hipótesis, relaciones estructurales e interpretación.

**Fuente y alcance:** Organización analítica de [C16], secc. I--V.

### 4. Criterios para comparar sistemas vectoriales

Explicitar estos criterios permite comparar sin adoptar de entrada un ganador. Una notación más compacta no demuestra que un método sea numéricamente más rápido o pedagógicamente superior. El artículo argumenta sobre estructura y unificación, pero no presenta una comparación controlada de costos computacionales ni resultados de aprendizaje.

**Fuente y alcance:** Criterios elaborados a partir de [C16], secc. I, IV y V.

### 5. Genealogía de la controversia vectorial

El esquema sintetiza relaciones intelectuales; las flechas no constituyen una cadena cronológica exclusiva. Clifford precede al debate más intenso y su obra combina el producto métrico con el álgebra de extensión de Grassmann. Heaviside y Tait fueron actores decisivos en el desarrollo y difusión de las alternativas. Hestenes aparece posteriormente en la recuperación y ampliación del programa geométrico. Se omite una flecha Gibbs hacia Clifford para evitar una lectura cronológica anacrónica; la integración posterior de formalismos no implica esa influencia histórica.

**Fuente y alcance:** Adaptación selectiva de [C16], secc. II y fig. 1, pp. 1--3 y 6.

### 6. Hamilton y Gibbs: operaciones e interpretación

El signo no indica que el formalismo de Hamilton produzca energías físicas negativas: la energía se construye con la norma adecuada. Expresa que los generadores cuaterniónicos se identifican naturalmente con bivectores. La virtud de Gibbs fue operacional e histórica; la objeción de Clifford se refiere al alcance del sistema elemental, no a la validez de los resultados del análisis vectorial.

**Fuente y alcance:** [C16], secc. II, ecs. (2)--(4), p. 2.

### 7. Del debate vectorial a las teorías del siglo XX

El artículo presenta estos hitos para explicar por qué los lenguajes de la física continuaron diversificándose tras la adopción del sistema de Gibbs. La insuficiencia señalada corresponde al uso de cuaterniones reales sin ampliaciones para determinadas representaciones; no equivale a una imposibilidad absoluta de formular relatividad mediante construcciones cuaterniónicas ampliadas. La relación entre espinores, matrices y cuaterniones exige especificar el espacio y la acción utilizados. Las fechas son las que utiliza la discusión histórica del artículo.

**Fuente y alcance:** [C16], secc. II, pp. 2--3; hitos según el relato del manuscrito.

### 8. Direcciones y planos: la coincidencia dimensional en 3D

El conteo de generadores de SO(n) coincide con el de matrices antisimétricas y con los componentes bivectoriales. En tres dimensiones la dualidad depende de la métrica y de una orientación. Es una identificación útil, no una equivalencia de las leyes de transformación bajo todas las simetrías espaciales.

**Fuente y alcance:** [C16], secc. V, p. 6; formulación dimensional desarrollada.

### 9. Álgebra euclídea: hipótesis y relaciones generadoras

La signatura positiva forma parte de las hipótesis y evita confundir Cl(3,0) con el álgebra espacio-temporal Cl(1,3). El álgebra se genera imponiendo las relaciones cuadráticas y extendiendo por bilinealidad y asociatividad. El subespacio de grado uno no es cerrado para el producto geométrico; precisamente se amplía para conservar la información de grados cero y dos.

**Fuente y alcance:** [C16], secc. III, p. 3, construcción de la ec. (5).

### 10. Graduación: escalares, vectores, áreas y volúmenes

Un bivector representa un plano orientado con magnitud de área, no una flecha dentro del plano. Un trivector representa volumen orientado. Los dibujos son ayudas geométricas; un escalar no constituye por sí mismo la posición de un punto. Los ocho componentes son grados de libertad algebraicos sobre un espacio físico de tres dimensiones.

**Fuente y alcance:** [C16], sección III, pp. 3--4, ec. (10); esquema propio.

### 11. Multivectores y dualidad en $\Cl_3$

I es central en Cl(3,0) y permite una estructura compleja interna con coeficientes reales. No extrapolar su centralidad o el signo de su cuadrado a cualquier dimensión y signatura. Distinguir el bivector Iw de su vector axial dual w; esta distinción tendrá consecuencias en paridad y en la representación de los campos. La suma de espacios exteriores expresa una descomposición como espacio vectorial. El producto de Clifford respeta una graduación por paridad y mezcla grados enteros; no se está identificando la multiplicación de Clifford con la exterior.

**Fuente y alcance:** [C16], secc. III, ecs. (10)--(12), p. 3.

### 12. Proposición 1. Descomposición del producto geométrico

La identidad se obtiene polarizando el cuadrado métrico. Al expandir (a+b) al cuadrado y restar a al cuadrado y b al cuadrado se recupera la relación simétrica. El término alternante es el producto exterior. Así, Clifford integra la métrica euclídea y la estructura de Grassmann; no se limita a sumar dos reglas sin relación.

**Fuente y alcance:** [C16], ecs. (6)--(7) y (27), pp. 3 y 6; justificación explicitada.

### 13. Contenido geométrico: área y volumen orientados

El área está en el plano generado por los vectores. La normal del producto cruz es su representación dual en tres dimensiones. En el volumen, corregir la errata del texto donde se repite b en el triple producto: debe ser a punto b cruz c. No hace falta añadir una regla independiente de volumen: se usa el grado tres del producto.

**Fuente y alcance:** [C16], sección IV, pp. 5--6; dibujo y explicitación propios.

### 14. Criterios de ortogonalidad y dependencia lineal

Incluir los casos degenerados evita afirmar que existe un plano único cuando los vectores son colineales o nulos. Para vectores no nulos, la ausencia de parte bivectorial indica paralelismo. Para tres vectores, el volumen cero caracteriza dependencia lineal, y por tanto coplanaridad en el sentido de estar contenidos en un plano por el origen.

**Fuente y alcance:** [C16], sección IV, p. 6, discusión de la ec. (27).

### 15. Proposición 2. Invertibilidad y divisores de cero

La inversa de cualquier vector euclídeo no nulo existe por positividad de su cuadrado. Para un multivector general, la conjugación produce un denominador central que puede anularse. D distinto de cero es condición necesaria y suficiente: si M fuera invertible y D fuera cero, su conjugado sería cero, lo que obliga a M a ser cero. La estructura matricial mostrada más adelante hace visible la misma condición como no singularidad.

**Fuente y alcance:** [C16], ecs. (8) y (12), p. 3; condición de existencia explicitada.

### 16. Subálgebras pares y recuperación de los formalismos

Los complejos y cuaterniones se recuperan como estructuras algebraicas, no solo por tener igual cantidad de componentes. El producto de dos elementos pares es par. La identificación cuaterniónica exige escoger una convención de signos que respete ij igual a k. La comparación evita denominar subálgebra al conjunto de vectores cartesianos.

**Fuente y alcance:** [C16], secc. III, pp. 3--4 y tabla I, p. 6.

### 17. El plano de Clifford y la representación compleja

Esta diapositiva explicita la parte del artículo dedicada al plano. Se usa J2 para el bivector bidimensional y se reserva I para el trivector tridimensional. En Cl2 el bivector J2 anticonmuta con los vectores del plano, a diferencia del seudoescalar central de Cl3. De esa anticonmutación surge el cambio de signo entre las fórmulas unilateral vectorial y compleja. La ecuación v=e1 z establece la correspondencia; no se afirma que vector y operador sean el mismo tipo geométrico.

**Fuente y alcance:** [C16], ecs. (13)--(14), pp. 3--4, y conexión con ec. (1).

### 18. Representación matricial: el álgebra de Pauli

Las matrices de Pauli verifican las mismas relaciones de producto que los generadores euclídeos. Esta representación permite comprobar el isomorfismo del álgebra real de ocho dimensiones con las matrices complejas dos por dos. La matriz no es el espinor: en la formulación de Pauli, el espinor es un objeto complejo de dos componentes sobre el que actúan matrices. Que el álgebra par sea isomorfa a los cuaterniones no elimina la necesidad de declarar las leyes de transformación de un estado físico.

**Fuente y alcance:** [C16], inicio de la sección III, p. 3; matrices explicitadas para la presentación.

### 19. Rotores y grupo Spin(3)

En Cl3 los rotores son los elementos pares unitarios y se identifican con los cuaterniones unitarios. R y menos R tienen la misma acción por conjugación. El semíangulo refleja la doble cubierta, no una corrección arbitraria. Con la base de Pauli, los generadores bivectoriales corresponden a matrices antihermíticas sin traza y los rotores a SU(2).

**Fuente y alcance:** [C16], ecs. (3) y (9), pp. 2--3; estructura de grupo explicitada.

### 20. Acción adjunta, isometría y composición

La norma se conserva por la asociatividad y porque el cuadrado vectorial es escalar. La conservación del producto interno se obtiene por polarización de la norma. Para componer, aplicar primero R1 y luego R2 e invertir el orden de los factores en el reverso. Rodrigues se obtiene descomponiendo el vector en componentes paralela y perpendicular al eje; la derivación está en el apéndice.

**Fuente y alcance:** Desarrollo de [C16], ec. (9), p. 3.

### 21. Paridad e involuciones: operaciones diferentes

La reversión, la involución de grado y la conjugación no son intercambiables. La extensión de menos identidad sobre el espacio vectorial a todo el álgebra coincide con la involución de grado. Al expresar un bivector como Iw, la representación axial depende de la orientación escogida. En electrodinámica esto permite distinguir E de la parte magnética IcB sin confiar solo en una letra vectorial.

**Fuente y alcance:** [C16], ecs. (12), (21) y discusión polar--axial, pp. 3 y 5.

### 22. Derivación geométrica y unificación del cálculo

En la regla temporal se conserva el orden de los factores aunque el producto no conmute. Para nabla al cuadrado, los términos cruzados se cancelan por anticonmutación y por igualdad de derivadas mixtas bajo la regularidad supuesta. El artículo remite al cálculo geométrico para la unificación de teoremas integrales; esa afirmación no sustituye la formulación de sus hipótesis y condiciones de frontera.

**Fuente y alcance:** [C16], ecs. (22)--(24), p. 5; cuadrado del operador desarrollado.

### 23. Paravectores y forma cuadrática de Minkowski

La identidad de Minkowski no requiere cambiar el cuadrado positivo de los generadores espaciales: el signo temporal-espacial surge al multiplicar por la conjugación. El álgebra de espacio físico y el álgebra espacio-temporal pueden relacionarse, pero no se deben identificar como si tuvieran la misma dimensión real o los mismos generadores.

**Fuente y alcance:** [C16], ecs. (15)--(16), p. 4; factores dimensionales explicitados.

### 24. Boosts de Lorentz y parametrización por rapidez

La cantidad del exponente es una rapidez adimensional por una dirección unitaria, no una velocidad con unidades. El cuadrado positivo del vector genera cosenos hiperbólicos y senos hiperbólicos, mientras el cuadrado negativo del bivector generaba funciones trigonométricas. La acción tiene el mismo L en ambos lados, a diferencia de la rotación con rotor y rotor inverso. El signo depende de si se adopta una transformación activa o un cambio pasivo de marco.

**Fuente y alcance:** [C16], sección III.A, p. 4, ec. (17); expansión y convención explicitadas.

### 25. Exponenciales: estructura circular e hiperbólica

La comparación es estructural y no permite usar la misma regla de acción para todos los elementos. Para los boosts de paravectores de la convención elegida aparece L a ambos lados; para rotaciones se usa el rotor y su inverso. La exponencial existe por su serie en el álgebra finito-dimensional. Raíces y logaritmos requieren estudiar dominio y ramas, como indica el artículo al remitir a funciones multivectoriales.

**Fuente y alcance:** [C16], ecs. (9), (17) y secc. IV, pp. 3--4 y 6.

### 26. Electrodinámica en el vacío: formulación de referencia

Se elige el vacío para fijar de manera coherente epsilon cero y mu cero. La forma general en medios requiere relaciones constitutivas adicionales. El conteo de ocho componentes es un conteo de las ecuaciones, no de grados de libertad dinámicos independientes. Las cuatro leyes siguen existiendo al reescribirlas como una igualdad multivectorial.

**Fuente y alcance:** [C16], sección III.A, p. 4, ec. (18).

### 27. Maxwell: una ecuación multigraduada en unidades SI

Esta forma SI se verifica expandiendo el producto. El PDF mezcla la expresión temporal con constantes c sin especificar completamente la normalización; restaurar uno sobre c evita incompatibilidad dimensional. La igualdad multivectorial no reduce el contenido físico de Maxwell: organiza las mismas ecuaciones. Se usa el vacío y ausencia de monopolos magnéticos; los medios materiales requieren relaciones constitutivas adicionales.

**Fuente y alcance:** [C16], ecs. (18)--(19), p. 4; normalización SI explicitada.

### 28. Equivalencia de Maxwell mediante proyecciones de grado

La parte bivectorial de DF es I multiplicado por la suma de la derivada temporal de B y c por el rotacional de E. La fila conserva ese factor c y, al dividir por c, recupera la ley de Faraday habitual. La parte vectorial procede de la derivada de E sobre c y de I c por I rotacional de B, que produce menos c rotacional de B. El apéndice expande todos los grados.

**Fuente y alcance:** Desarrollo de las ecs. (18)--(19) del [C16] con la convención SI adoptada.

### 29. Ecuación de Dirac: representación y contenido real

Este bloque ilustra el alcance del lenguaje, sin suponer conocimientos avanzados de teoría cuántica. La ecuación usual i gamma derivada psi igual a m psi se escribe de forma equivalente multiplicando por uno sobre i. La coincidencia de dimensión es necesaria para una correspondencia lineal, pero no demuestra que las acciones de los operadores ni las transformaciones físicas sean equivalentes.

**Fuente y alcance:** [C16], sección III.A, p. 5, ec. (20).

### 30. Dirac en $\Cl_3$: alcance de la correspondencia

Exponer la ecuación como la representación citada por los autores. Una demostración completa exige construir la aplicación desde el espinor de Dirac, verificar la correspondencia de las matrices gamma y recuperar los observables y las leyes de transformación. No se obtiene una nueva física por sustituir la unidad imaginaria por I; se reorganiza la representación matemática.

**Fuente y alcance:** [C16], ec. (21), p. 5, con remisión a su referencia [23].

### 31. Rectas orientadas y coordenadas de Plücker

La pareja dirección y momento codifica una línea, no un punto de aplicación único. Cambiar r por r más lambda v no cambia el bivector. Las seis coordenadas de Plücker cumplen una restricción; al identificar pares que difieren por escala común, una recta tiene cuatro grados de libertad. Para una fuerza la magnitud importa y no se elimina esa escala. Las distintas componentes físicas pueden tener unidades distintas.

**Fuente y alcance:** [C16], sección III.B, p. 5, ec. (25); esquema propio.

### 32. Fuerza aplicada y orientación del momento

La expresión del artículo usa el orden f exterior r, que se opone al momento r cruz f empleado habitualmente en mecánica. Declarar el signo es indispensable antes de utilizar la representación en equilibrio o dinámica. La invariancia sobre la línea de acción no equivale a insensibilidad general al punto de aplicación en un cuerpo deformable.

**Fuente y alcance:** [C16], secc. III.B, ec. (25), p. 5; convención mecánica explicitada.

### 33. Producto recíproco y coplanaridad de líneas

El artículo asocia la parte trivectorial a la torsión de dos fuerzas. Para evitar una interpretación mecánica excesiva, presentarla como producto recíproco de líneas: mide un triple producto y detecta coplanaridad. Dos fuerzas coplanares pueden ejercer un momento no nulo. El signo cambia al invertir orientaciones o convenciones, por lo que no debe describirse como un torque universal independiente de esas elecciones.

**Fuente y alcance:** [C16], sección III.B, p. 5, ec. (26); interpretación geométrica precisada.

### 34. Extensión dimensional y costo de representación

El producto cruz usual entre dos vectores no ofrece una representación canónica de todos los planos en dimensión cuatro. El exterior sí generaliza de manera uniforme. El crecimiento exponencial de la dimensión es una advertencia de costo algebraico, no una medida directa del costo de un algoritmo que puede explotar estructuras dispersas o subálgebras.

**Fuente y alcance:** [C16], sección IV y conclusión, pp. 5--7.

### 35. Correspondencias y límites de cada formalismo

La tabla aplica los criterios definidos al comienzo. En el sistema de Gibbs las rotaciones se representan mediante matrices u otros operadores, lo que es una ampliación rutinaria y eficaz. Los cuaterniones son un álgebra de división, mientras Cl3 contiene divisores de cero. Clifford conserva el contenido de los productos conocidos y distingue grados, pero requiere elegir representaciones y métodos de cálculo apropiados.

**Fuente y alcance:** Síntesis de [C16], secc. II--V; alcance de invertibilidad precisado.

### 36. Implicaciones para Mecatrónica II

Las conexiones se formulan como problemas, objetos y límites. El artículo cita aplicaciones en robótica, visión, óptica y procesamiento de señales, pero no reproduce un estudio de implementación para cada una. En particular, las traslaciones y las poses completas no se atribuyen a los rotores de Cl3: se mencionan modelos ampliados cuando son necesarios.

**Fuente y alcance:** [C16], secc. III.B y secc. V, pp. 5--7; vínculos mecánicos explicitados.

### 37. Evaluación crítica: tres niveles de afirmación

El artículo usa un lenguaje fuerte al describir limitaciones y defectos de sistemas previos. Una evaluación rigurosa distingue el alcance de las identidades de las inferencias sobre conveniencia o naturalidad. La isotropía del plano complejo se preserva bajo rotaciones apropiadas; distinguir un eje real y uno imaginario no demuestra una ruptura física de simetría. Tampoco hay en el artículo un experimento que mida reducción de esfuerzo de aprendizaje.

**Fuente y alcance:** Lectura crítica de [C16], secc. II, IV y V, pp. 1--2 y 5--7.

### 38. Conclusiones

Cerrar con la respuesta a los criterios iniciales: qué se conserva, qué se integra y qué sigue requiriendo hipótesis. La propuesta de los autores gana fuerza al reconocerse como una estructura que contiene y relaciona formalismos existentes, no como una descalificación de sus aplicaciones válidas. La práctica profesional exige además evaluar costo, estabilidad numérica y adecuación de la implementación.

**Fuente y alcance:** Síntesis de [C16], secc. V, pp. 6--7.

### 39. Referencias

La fuente de contenido es el manuscrito local, identificado como arXiv versión dos. No usar la paginación editorial para las remisiones internas al PDF de ocho páginas. Las obras complementarias se reconocen como bibliografía que cita el artículo, no como fuentes íntegramente revisadas para esta preparación.

**Fuente y alcance:** Las remisiones de [C16] corresponden al manuscrito local WARaLG.pdf.

### 40. Bibliografía especializada y trazabilidad

Los apéndices permiten auditar signos, unidades e hipótesis sin fragmentar el argumento principal. La bibliografía de ampliación se ofrece para profundización y mantiene la numeración del artículo original. El guion conserva el razonamiento por diapositiva y las correcciones conceptuales adoptadas.

**Fuente y alcance:** Referencias [19], [23] y [25] de [C16], p. 7.

### 41. A1. Representación compleja del plano

Un mismo tipo de número puede representar una posición plana o una transformación por multiplicación. Al sumar se recupera la regla del paralelogramo. La crítica del artículo al uso de ejes real e imaginario debe entenderse como una motivación para distinguir objetos y operadores; representar el plano mediante complejos no rompe por sí mismo su isotropía física. El diagrama utiliza una rotación antihoraria.

**Fuente y alcance:** [C16], sección II, pp. 1--2, ec. (1).

### 42. A2. Norma e inversa cuaterniónica

Distinguir la dimensión de la representación de la dimensión del espacio físico. La cuarta componente no obliga a interpretar el escalar como tiempo. La daga se usa aquí exclusivamente para la conjugación cuaterniónica; después la reversión de Clifford tendrá una tilde. La positividad de q por su conjugado permite dividir por todo cuaternión no nulo.

**Fuente y alcance:** [C16], sección II, p. 2, ec. (2); inversa desarrollada para la presentación.

### 43. A3. Rotación cuaterniónica y acción bilateral

El manuscrito escribe q prima igual a exponencial de a sobre dos por q por exponencial de menos a sobre dos. Aquí se reserva q para el operador unitario y se escribe v con sombrero para el cuaternión puro transformado. El cambio es de notación, no de acción. El módulo del generador a incorpora el ángulo; la dirección unitaria por sí sola no determina la amplitud del giro.

**Fuente y alcance:** [C16], secc. II, ec. (3), p. 2; parametrización angular explicitada.

### 44. A4. Cuadrado vectorial y cancelación de términos cruzados

Mostrar cómo se cancelan los términos cruzados sin declarar que toda multiplicación conmute. La norma se obtiene como escalar. La diferencia de signos no convierte a un formalismo en falso: indica que los generadores cuaterniónicos serán identificados con bivectores, que tienen otro significado geométrico.

**Fuente y alcance:** [C16], sección III, p. 3, ec. (5) y texto posterior.

### 45. A5. Comprobación por componentes del producto geométrico

Hacer la multiplicación sin saltarse el cambio e2e1 igual a menos e1e2. El ángulo no orientado entre ambos vectores es 45 grados; el giro de a hacia b en el plano e12 es horario. El resultado ba es 5 más 5e12, de modo que intercambiar el orden conserva la proyección e invierte la orientación del área.

**Fuente y alcance:** Desarrollo algebraico a partir de las ecs. (6)--(7) del [C16].

### 46. A6. Recuperación de un factor mediante inversa derecha

La inversa existe para todo vector no nulo en esta signatura positiva. Para resolver ab igual a C se multiplica por b inverso a la derecha. No se puede cambiar el orden por comodidad. En álgebras con signatura indefinida puede haber vectores no nulos con cuadrado cero, para los que esta fórmula no da una inversa.

**Fuente y alcance:** [C16], sección III, p. 3, ec. (8); comprobación propia.

### 47. A7. Denominador central de la inversa multivectorial

El elemento z es central, por lo que los términos cruzados zU y Uz se cancelan. U al cuadrado es norma de v al cuadrado menos norma de w al cuadrado más 2I por v punto w. Para coeficientes reales, alpha al cuadrado más beta al cuadrado solo se anula cuando ambos son cero. El caso M igual a 1 más e1 da precisamente cero.

**Fuente y alcance:** Desarrollo algebraico de la fórmula posterior a la ec. (12) del [C16].

### 48. A8. Convención cuaterniónica de los bivectores

El artículo utiliza otra base equivalente para la correspondencia. Aquí se escogen tres bivectores negativos cíclicos para cumplir i por j igual a k con una regla uniforme. Subrayar que la subálgebra par sí es cerrada bajo el producto y es isomorfa a los cuaterniones; el subespacio vectorial de grado uno no es una subálgebra, porque su producto tiene grados cero y dos.

**Fuente y alcance:** [C16], sección III, p. 4; tabla I, p. 6. Convención de signos equivalente.

### 49. A9. Comprobación de un giro de $90^\circ$

Calcular e12 por e1 igual a menos e2, e1 por e12 igual a e2 y e2 por e12 igual a menos e1. Comprobar el signo del giro con la regla de la mano derecha. Este ejemplo fija la convención para que las fórmulas con signos opuestos de otros libros no generen confusión. El anexo deriva la fórmula de Rodrigues a partir del mismo rotor.

**Fuente y alcance:** Ejemplo propio basado en la ec. (9) del [C16].

### 50. A10. No conmutatividad: dos giros sobre ejes fijos

Aclarar que los ejes son fijos en el mismo marco y se usan giros activos. El orden se lee de derecha a izquierda en el producto de rotores. Las matrices de rotación tampoco conmutan en general; la propiedad no es una desventaja exclusiva de los cuaterniones.

**Fuente y alcance:** [C16], secciones II--III, pp. 2--4; ejemplo didáctico propio.

### 51. A11. Derivación de la fórmula de Rodrigues

La componente paralela conmuta con el bivector I n y la perpendicular anticonmuta con él. Al expandir los factores se obtiene el giro plano de la componente perpendicular. La fórmula familiar de Rodrigues confirma que el rotor produce la rotación euclídea habitual; no introduce una nueva ley física.

**Fuente y alcance:** Derivación complementaria de la rotación de la ec. (9) del [C16].

### 52. A12. Invariancia del intervalo y boost numérico

El intervalo es escalar y por eso puede conmutar con L. La conjugación invierte el orden, aunque como los factores extremos son iguales el aspecto del resultado puede disimular esa propiedad. El ejemplo usa unidades de longitud comunes para ct y x y el signo activo escogido antes.

**Fuente y alcance:** Desarrollo de las ecs. (16)--(17) del [C16]; comprobación propia.

### 53. A13. Expansión homogénea de la ecuación de Maxwell

El signo menos de la parte vectorial se debe a I por I igual a menos uno. Esta expansión es la comprobación central de equivalencia del bloque electromagnético. El teorema no requiere tratar al vector axial B como si fuera un vector polar: su representación física en F es el bivector I c B.

**Fuente y alcance:** Desarrollo de las ecs. (18)--(19), con factores SI explicitados.

### 54. A14. Reconstrucción de la línea de acción

Aplicar la identidad del producto triple: (v cruz r) cruz v es norma de v al cuadrado por r menos v por r punto v. Se obtiene la componente de r perpendicular a v, que es el punto de la línea más cercano al origen. La invariancia bajo traslación sobre la propia recta muestra por qué no se recupera un punto único de aplicación.

**Fuente y alcance:** Desarrollo de la ec. (25) del [C16], respetando su orden de producto.

### 55. A15. Fuerza excéntrica: signo y unidades

Multiplicar primero las magnitudes y después verificar la orientación: e1 cruz e2 es e3, mientras e2 exterior e1 es menos e12. La invariancia al deslizar la fuerza sobre su propia recta expresa el principio de transmisibilidad para la estática de un sólido rígido. No significa que cualquier punto de aplicación sea equivalente en un cuerpo deformable.

**Fuente y alcance:** Ejemplo propio basado en la sección III.B del [C16].

### 56. A16. Coplanaridad y par puro: un contraejemplo

Este ejemplo evita interpretar literalmente la expresión del artículo sobre ausencia de torsión cuando el trivector se anula. Un par de fuerzas tiene fuerza resultante cero y momento no nulo, aun cuando sus líneas sean coplanares. El producto recíproco y el momento resultante responden preguntas distintas.

**Fuente y alcance:** Contraejemplo didáctico para delimitar la interpretación de la ec. (26).

### 57. A17. Comprobaciones estructurales

La norma del producto de dos vectores permite reconstruir el producto de las magnitudes de sus factores: tres al cuadrado más cuatro al cuadrado es veinticinco. El conmutador fija los signos de la ecuación cinemática del rotor. Las condiciones de equilibrio de fuerza y momento son independientes de la coplanaridad de líneas. Estos resultados pueden contrastarse con el script de verificación algebraica incluido.

**Fuente y alcance:** Comprobaciones desarrolladas a partir de las identidades de [C16].

### 58. A18. Generadores bivectoriales y álgebra de Lie

Esta extensión hace explícita la relación del artículo con cinemática de cuerpos rígidos. G_i igual a menos I e_i sobre dos satisface el álgebra de so(3), comprobable con productos de base. Derivar v=Rv0R reverso usando la ecuación de R y su reverso da un conmutador, que es la velocidad angular cruz v. Se especifica el marco porque la ecuación del rotor es distinta si omega se expresa en coordenadas corporales.

**Fuente y alcance:** Extensión analítica del esquema de rotación de [C16], ec. (9).

### 59. A19. Cambio de origen y rotación de una fuerza-momento

La matriz de cambio de origen resulta directamente de sustituir r prima por r menos d en el producto cruz. Los bloques no son una suma de cantidades de la misma unidad: el bloque d cruz convierte fuerza en momento. Se distingue este cambio pasivo de origen de una rotación activa del sistema físico. Para transformaciones rígidas completas puede formularse la acción sobre fuerzas y momentos con estructuras adicionales; no se presenta aquí como una acción de rotores euclídeos sobre traslaciones.

**Fuente y alcance:** Extensión mecánica de la representación de líneas de [C16], secc. III.B.

### 60. A20. Restricción de Plücker y sistemas de fuerzas

La restricción de Plücker caracteriza una línea y no una fuerza-momento arbitraria. Sumar dos representaciones de fuerzas produce una pareja de fuerza y momento, pero no garantiza que pueda reducirse a una fuerza aplicada sobre una única recta. Si la fuerza resultante no es cero, el momento paralelo a ella no se elimina cambiando el origen. Esta distinción es central para no confundir líneas de acción con tornillos o sistemas generales de fuerzas.

**Fuente y alcance:** Consecuencia mecánica de [C16], ecs. (25)--(26); desarrollo analítico propio.

### 61. A21. Funciones de vectores y multivectores

El artículo menciona explícitamente seno, logaritmo, raíces y potencias como dos elevado a un vector. Para un vector euclídeo las potencias pares son escalares y las impares son proporcionales al vector, de donde surgen las fórmulas. La expresión con n se entiende para r positivo; en el vector cero los valores se obtienen directamente de las series. No se extrapola la existencia global de logaritmos o raíces a elementos singulares.

**Fuente y alcance:** [C16], secc. IV, p. 6, referencia [26]; fórmulas desarrolladas por series.

### 62. A22. Ámbitos de aplicación citados por el artículo

Esta tabla recoge los dominios enumerados en la conclusión. Diferenciar una aplicación citada de un resultado desarrollado y demostrado en este manuscrito. Algunos ejemplos utilizan álgebras de mayor dimensión, signaturas o modelos distintos de Cl3; el artículo los presenta como parte de un marco más amplio y no como realizaciones idénticas del álgebra euclídea básica.

**Fuente y alcance:** [C16], secc. V y referencias, p. 7.

## Cotejo documental

El informe `revision_contenido_paper.md` registra la cobertura de las ecuaciones (1)–(27), las secciones del manuscrito, las convenciones y las precisiones respecto del texto original.
