from app.controller.post_controller import deleted_post,list_posts,created_post,get_one_post,get_one_post_update



def init_app(app):
    
    @app.get("/posts")
    def read_posts():
        return list_posts()


    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return get_one_post(id)    


    @app.post("/posts")
    def create_post():
        return created_post()


    @app.patch("/posts/<int:id>")
    def update_post(id):
        return get_one_post_update(id)    


    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return deleted_post(id)  
