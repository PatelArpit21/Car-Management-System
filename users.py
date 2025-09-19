import database as db
def signup(username,password): ## updating the username and password in the users database
    val=(username,password)
    db.insert_data(("insert into users(username,password) values('%s','%s')"%val)) # id, username , password

def checkuser(username):  # CHECK USER LIST FOR NEW USERNAME
    x=db.fetch_data("select * from users where username='%s'"%username)
    if x==[]:
        return True;
    else:
        return False;

def get_id(username):  # fetching the 'id' from users table 
    x=db.fetch_data("select id from users where username='%s'"%username)
    return (x[0][0])

def check_password(username,password):  # CHECK USER LIST FOR NEW USERNAME IF IT ALREADY EXSISTS
    x=db.fetch_data("select password from users where username='%s'"%username)
    if x:
        if x[0][0]==password:
            return True;
        else:
            return False;
    else:
        return False;

def check_owner(username):
    x=db.fetch_data("select * from users where username='%s'"%username)
    if x[0][0]==1:
        return True;
    else:
        return False;

# def