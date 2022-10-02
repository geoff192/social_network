

def run():
    #Utilizando el API, obtener la lista completa de usuarios.
    users  = get_users()


    #Recorrer la lista de usuarios
    for
        user_id = 
        #Por cada usuario en la lista, obtener la lista de posts del usuario.
        user_posts = get_user_posts(user_id)
        
        #Recorrer la lista de posts
        for
            post_id = 
            #Por cada post, obtener la lista de comentarios del post.
            post_comments = get_post_comments(user_id, post_id)
            #Crear una propiedad nueva en el post actual llamada "comments" y asignarle el valor de post_comments

        #Crear una propiedad nueva en el usuario actual llamada "posts" y asignarle el valor de user_posts


    #Obtener el post con mas likes
    most_liked_post = get_most_liked_post(users)

    #Obtener el NOMBRE del usuario que tenga el post con mas likes  
    user_with_most_liked_post = get_user(most_liked_post.userId)
    #Imprimir el nombre del usuario que tenga el post con mas likes.
    #print("User with most liked post: " + user_with_most_liked_post.name)
    
    #Obtener el NUMERO DE LIKES del comentario con mas likes del POST CON MAS LIKES
    most_liked_comment = get_comment_with_most_likes()

    #Imprimir el numero de likes del comentario con mas likes de most_liked_post.
    #print("most_liked_post most liked comment amount: " + most_liked_comment.likes)

def get_user(user_id):
    #Utilizar la libreria 'requests' para hacer una llamada al API y obtener un usuario especifico.
    return

def get_users():
    #Utilizar la libreria 'requests' para hacer una llamada al API y obtener la lista de users
    return

def get_user_posts(user_id):
    #Utilizar la libreria 'requests' para hacer una llamada al API y obtener la lista de posts de un user
    return

def get_post_comments(user_id, post_id):
    #Utilizar la libreria 'requests' para hacer una llamada al API y obtener la lista de commentarios de un post
    return

def get_most_liked_post(users):
    
    #Declarar una variable llamada 'most_liked_post'
    most_liked_post = None
    #Recorrer la lista de usuarios
    
    for
        #Por cada usuario, recorrer la lista de posts
        user_posts =
        for 
            #Verificar si most_liked_post es igual a None y de ser asi, asignarle el valor del post actual.

            #Si most_liked_posts (else) no es None, compararar la cantidad de likes del post actual y el 'most_liked_post'


    #Retornar el most_liked_post 
    return


def get_comment_with_most_likes(post):
    #La logica de este metodo es muy similar a la de 'get_most_liked_post'
    return