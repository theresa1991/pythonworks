from blog.models import users,posts
session={}
def sign_in(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid please log in")
    return wrapper
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user
#print(authenticate(username="akhil",password="Password@123"))
#user is added in session if user has some value if authen true then user details is stored till
class LoginView:
    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
        print(session)

class PostListView:
    @sign_in
    def get(self,*args,**kwargs):#to accept as tuples dict etc all type accepted
        return posts
    @sign_in
    def post(self,*args,**kwargs):
        print(kwargs)
        post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        #print(post)
        posts.append(my_post)
        #print("successful")
        #print(posts[-1])
        print(my_post)
class MypostListView:
    @sign_in
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post
#all posts in a social media etc

class AddLike:
    @sign_in
    def post(selfself,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[ post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])
log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
aal_post=PostListView()
my_post={
    "postId":"9","title":"have a wonderful day","content":"mycontent","Liked by":[]
}
aal_post.post(data=my_post)
like=AddLike()
like.post(postid=1)
print(aal_post.get())
myposts=MypostListView()
print(myposts.get())
