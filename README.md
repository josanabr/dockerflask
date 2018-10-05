# Tutorial paso a paso de Flask

En este repositorio se encuentran disponibles

* `Dockerfile`
* `requirements.txt`

Usted ahora podrá crear su contenedor donde correrá la aplicación `app.py`.
Para crear el contenedor ejecutar `docker build -t <miusuario>/myflaskapp:1.0.0`.

Para ejecutar el contenedor debe ejecutar `docker run --rm -p 5000:5000 <miusuario>/myflaskapp:1.0.0`.
Una vez ejecutada esta línea usted podrá acceder a [http://localhost:5000](http://localhost:5000).

Asegúrese de cambiar `<miusuario>` por su usuario en la plataforma [Docker Hub](http://hub.docker.com).
