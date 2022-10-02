# Social Network

El siguiente proyecto consiste en realizar una serie de llamadas a un API para despues obtener diferentes metricas.


## API

El siguiente es el endpoint del API

```
https://63390646937ea77bfdc5d20a.mockapi.io
```

## API PATHS

### Users

Retorna una lista de todos los usuarios de la red social.

```
/users
```

### Posts

Retorna todos los posts de un usuario especifico.

```
/users/:id/posts
```

### Comments

Retorna todos los commentarios de un post especifico.

```
/users/:id/posts/:id/comments
```

