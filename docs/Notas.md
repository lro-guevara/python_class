# Notas de markdown (#)

## Subtitulo

### Subtitulo 3

#### Subtitulo 4

##### Subtitulo 5

Este documento esta en **markdown** (**), nos permite usar *recursos graficos.* (*)

~~Scratch this~~ depende del uso de dos ""~".

1. Item numerado 1
2. Item numerado 2
3. Item numerado 3
   * Item 1 (* o -)
   * Item 2

Se permite el uso de links:

[Typora markdown](https://typora.io/)

URLs dentro de "<>" se convertiran automaticamente en links:

<https://typora.io/>

Insertar imagenes mediante: "![Alt logo][http://ejemplo.png] // [logo]: URL"

![alt text][logo]

[logo]:https://www.creadores.unam.mx/wp-content/uploads/2019/02/centro-de-ciencias-geno%CC%81micas.png	"Ciencias Genomicas"

Para conocer el contenido de mi actual directorio de trabajo uso `ls` y saber mi directorio de trabajo uso `pwd`. Esto es posible con "``"

Se pueden generar scripts colocando los comandos entre `````

```
ls
pwd
cd data
mkdir scripts
```

Además se puede especificar el lenguaje de trabajo despues de las ````

````javascript
var s = "JavaScript syntax highlighting";
alert (s);
````

Ademas es posible generar tablas separando las columnas con |

| Tabla | X    | Y    |
| ----- | ---- | ---- |
| 3z    | 3zx  | 3zy  |



Sesion 1. Programacion en Python. 25.02.2021 



# Sesión 2 Comandos en git

* git init*      Inicializar repositorio
  * *git add **archivo***      Genera cambios en archivo de area de preparación	
  * *git commit -m "Mensaje"*      Agregar un mensaje que exprese que se formalizaron los cambios del repositorio
    * *git commit --amend -m "Nuevo mensaje"*     Cambiar mensaje de Commit
  * *git log*     Conocer ultimo mensaje del commit
    * *git log -N*     N indica el número de commits que quiero obtener
    * *git log --oneline*     Versión reducida de los commits 
  * *git diff **archivo***     Comparar las versiones del archivo
    * *git diff HEAD~1*     Últimos cambios en versiones anteriores
    * *git diff --staged **archivo***    Compara archivo de área de preparación y repositorio
  * *git show HEAD~1*     Cambios que se realizaron a más detalle, incluyendo Autor y commit que se configuró
  * *git status*     Cambios que se han hecho
    * *git status -u*     Archivos sin seguimiento
  * *git checkout*     Recuperar versiones anteriores indicando el commit al que queremos volver

+ *nano **archivo***     Modificar archivo