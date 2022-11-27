--------------------------------------------------------Jhony Alejandro Herrera Parrado-------------------------------------------------------------------------------
----------------------------------------------------INTRODUCION-------------------------------------------------------------------

Como consumidor promedio de vino en algunos momentos   es necesario  tener una ayuda a la hora de seleccionar vinos, es por esto que surge este algoritmo que ayuda a  tomar una decisión de acuerdo a las principales características de los vinos. Acá se podrá encontrar un algoritmo que ayudará a decidir el mejor vino  de acuerdo a los gustos del consumidor. Para esto se se utilizan los siguientes  métodos KNN y  DecisionTreeClassifier,  además  de esto se podrán observar las diferentes cualidades de estos por medios de gráficas.
![image](https://user-images.githubusercontent.com/110490202/204148567-94ed0e2f-f9ca-499a-9558-4777678be034.png)

---------------------------------------------------DESARROLLO-------------------------------------------------------------------

1.En primer lugar  debemos selecionar una base  de datos ,se elije esta base de datos ya que es la que mayores calificaciones presenta

![image](https://user-images.githubusercontent.com/110490202/204148854-2ec3ca8d-ffee-47bf-ba0b-c535ac26f8a2.png) 

2. se importan  la base de datosy las librerias  necesarias para  el desarrollo de este.
3. 
![image](https://user-images.githubusercontent.com/110490202/204149091-9568c9c4-0c37-455d-8b18-ec1fd9c02528.png)

3. Visualizamos los datos  para verificar que sean los datos requeridos. 

![image](https://user-images.githubusercontent.com/110490202/204149275-46209346-700c-4c74-b9d6-06788968d7e4.png)

4. se proced a hacer la eliminación y ajustes de valores NAN  en  cada   caracteristicas.
5. 
![image](https://user-images.githubusercontent.com/110490202/204149294-b3f5f327-d28f-4438-8a5a-7538428e3f50.png)

5. nuevamente  visualizamos los datos luego de  realizar los ajustes.
6. 
 ![image](https://user-images.githubusercontent.com/110490202/204149362-930c4e2a-9618-4d19-b5ad-d6e7a315a52e.png)
 
![image](https://user-images.githubusercontent.com/110490202/204149394-f5fc0619-a807-4efd-aeb7-e49edade74e2.png)

6. ahora se usan los datos de forma que 70 % de los datos para se usan entrenar, 20 % para probar y el 10 % para validar el método.
7.se genera un nuevo archivo lugo de realizar los ajustes de los  datos   en general y se le hace una  estandarizacion de los datos.
![image](https://user-images.githubusercontent.com/110490202/204149807-870d486b-c255-4974-a228-671957fc3727.png)
8.luego de esto  se hace PCA  la cual es  herramienta para reducir la dimensionalidad en los datos que puede ser utilizado para convertir un conjunto bastante grande de variables en un conjunto más pequeño que contenga la mayor cantidad de información contenida en el conjunto grande.

![image](https://user-images.githubusercontent.com/110490202/204150015-15c17120-67f6-4932-ab1b-9c03f1ff3a4c.png)
9. proceso de entrenamiento de metodo KNN 
![image](https://user-images.githubusercontent.com/110490202/204150222-3d9b0336-ea04-47c4-94ff-cd97d239a6cf.png)

10.se hace un reciclaje con los mejores parámetros y con el 90% de los datos que son  70 % de los datos para se usan entrenar, 20 % para probar

![image](https://user-images.githubusercontent.com/110490202/204150283-470f5e81-db9c-4c31-bc0b-8b9b0f640fd9.png)

11.se hace DecisionTreeClassifier

![image](https://user-images.githubusercontent.com/110490202/204150325-65764827-2918-472c-bae8-a80f99cb99bb.png)

---------------------------------------------------RESULTADOS-------------------------------------------------------------------
1. se puede observar cada caracteristica  y  la variacion de este.

![image](https://user-images.githubusercontent.com/110490202/204150992-e8f19256-d065-42fc-bfa6-fc55a30cffad.png)
![image](https://user-images.githubusercontent.com/110490202/204151133-02bb993a-5082-4a30-84bf-2ea82517ca4b.png)
![image](https://user-images.githubusercontent.com/110490202/204151149-fcf46b4a-e364-46a0-bf95-c6e294b36a05.png)
![image](https://user-images.githubusercontent.com/110490202/204151162-b4223b4b-9ba5-4ad0-8911-ccf9b06f4e97.png)
![image](https://user-images.githubusercontent.com/110490202/204151176-7af94aaa-f5f6-4352-93bb-905f0f3bbd40.png)
![image](https://user-images.githubusercontent.com/110490202/204151184-063ada14-5532-4fb8-b394-a2a235094353.png)
![image](https://user-images.githubusercontent.com/110490202/204151189-e9135ab9-2f87-4fc4-b7dd-7bc8909ef4bb.png)
![image](https://user-images.githubusercontent.com/110490202/204151204-3728d4c4-61ad-4a44-bdec-c840d03b151c.png)
![image](https://user-images.githubusercontent.com/110490202/204151231-4b498bce-0a1e-4cbc-b8e9-90f05eb83b1f.png)
![image](https://user-images.githubusercontent.com/110490202/204151251-71071032-34a6-46e6-888a-18afd5a4c605.png)

 2.La precisión de nuestro conjunto de datos de entrenamiento con ajuste en KNN : 67.29%  CON MCC =  0.2275418598167701
 
 ![image](https://user-images.githubusercontent.com/110490202/204151337-d0a06543-04c0-468d-8a83-67024c16829a.png)
 
 3.La precisión de nuestro conjunto de datos de entrenamiento con ajuste eN DecisionTreeClassifier  : 59.43%  MCC =  0.014188692204112178
 ![image](https://user-images.githubusercontent.com/110490202/204153764-aa7683a1-294f-4951-b8e2-8f5c0ed4baab.png)

---------------------------------------------------CONCLUSIONES------------------------------------------------------------------

podemos  observar que en ambos casos los valores   de entrenamientos y los valores finales  al realizar la validacion del 10%   presentan una variacion esto se puede inferir ya que muchos datos como  el PH  ,azúcar residual, # aacidez fija no presentan variaciones mayores al  0.1 sin embargo   se puede analizar que hay caracteristicas que son muy significativas  como lo son el acido citrico el cual varia hasta en 0.3 , el  % de sulfatos ,dióxido de azufre libre,dioxido sulfuroso  y el %cloruros por lo tanto estan son las principales caracteristicas  a la hora de analizar  y obtener las bases de datos, aun que la diferencia entre knn y  DecisionTreeClassifier  en el entrenamiento es alta  una vez se pone a prueba  con la validazacion podemos descartar el metodo de DecisionTreeClassifier ya que su La precisión es  mucho menor a  la de KNN.









