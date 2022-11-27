
---------------------------------------------------------Jhony Alejandro Herrera Parrado---------------------------------------------------------------------------------
----------------------------------------------------INTRODUCION-------------------------------------------------------------------
Como consumidor promedio de vino en algunos momentos   es necesario  tener una ayuda a la hora de seleccionar vinos, es por esto que surge este algoritmo que ayuda a  tomar una decisión de acuerdo a las principales características de los vinos. Acá se podrá encontrar un algoritmo que ayudará a decidir el mejor vino  de acuerdo a los gustos del consumidor. Para esto se se utilizan los siguientes  métodos KNN y  DecisionTreeClassifier,  además  de esto se podrán observar las diferentes cualidades de estos por medios de gráficas.
![image](https://user-images.githubusercontent.com/110490202/204148567-94ed0e2f-f9ca-499a-9558-4777678be034.png)

---------------------------------------------------DESARROLLO-------------------------------------------------------------------
1.En primer lugar  debemos selecionar una base  de datos ,se elije esta base de datos ya que es la que mayores calificaciones presenta
![image](https://user-images.githubusercontent.com/110490202/204148854-2ec3ca8d-ffee-47bf-ba0b-c535ac26f8a2.png) 
2. se importan  la base de datosy las librerias  necesarias para  el desarrollo de este.
![image](https://user-images.githubusercontent.com/110490202/204149091-9568c9c4-0c37-455d-8b18-ec1fd9c02528.png)
3. Visualizamos los datos  para verificar que sean los datos requeridos.
![image](https://user-images.githubusercontent.com/110490202/204149275-46209346-700c-4c74-b9d6-06788968d7e4.png)
4. se proced a hacer la eliminación y ajustes de valores NAN  en  cada   caracteristicas.
![image](https://user-images.githubusercontent.com/110490202/204149294-b3f5f327-d28f-4438-8a5a-7538428e3f50.png)
5. nuevamente  visualizamos los datos luego de  realizar los ajustes.
 ![image](https://user-images.githubusercontent.com/110490202/204149362-930c4e2a-9618-4d19-b5ad-d6e7a315a52e.png)
![image](https://user-images.githubusercontent.com/110490202/204149394-f5fc0619-a807-4efd-aeb7-e49edade74e2.png)
6. ahora se usan los datos de forma que 70 % de los datos para se usan entrenar, 20 % para probar y el 10 % para validar el método.
7.se genera un nuevo archivo lugo de realizar los ajustes de los  datos   en general y se le hace una  estandarizacion de los datos.
![image](https://user-images.githubusercontent.com/110490202/204149807-870d486b-c255-4974-a228-671957fc3727.png)
8.luego de esto  se hace PCA  la cual es  herramienta para reducir la dimensionalidad en los datos que puede ser utilizado para convertir un conjunto bastante grande de variables en un conjunto más pequeño que contenga la mayor cantidad de información contenida en el conjunto grande
![image](https://user-images.githubusercontent.com/110490202/204150015-15c17120-67f6-4932-ab1b-9c03f1ff3a4c.png)
