import uuid
from datetime import datetime
from users import User
class Comment():
    comments = []

    def auth_user(self,logged_in):
        for item in User.users:
            if logged_in == item["logged_in"]:
                return item
        return False

    def create_a_comment(self,logged_in,author,message,is_reply=False):
        this_user = self.auth_user(logged_in)
        if this_user:
            payload = {
                "commentID":str(uuid.uuid4().int),
                "Author": author,
                "Timestamp": str(datetime.utcnow()),
                "Message": message,
                "is_reply": is_reply if is_reply else "False"
            }
            Comment.comments.append(payload)
            the_status = "Reply on comment"+str(is_reply)+" created!!" if is_reply\
                    else "Comment Created!!"
            answer={
                "Status": the_status,
                "Details": payload
            }
            return answer
        else:
            return "You are not a user in this System."


    def fetch_all_comments(self,logged_in):
        this_user = self.auth_user(logged_in)
        if this_user:
            if this_user["role"] == "Admin":
                return Comment.comments
        return "You are not authorized to view all comments"
    
    def fetch_a_comments(self,logged_in,comment_id):
        this_user = self.auth_user(logged_in)
        my_comment = False
        if this_user:
            for thing in Comment.comments:
                if thing["commentID"] == str(comment_id):
                    my_comment = thing
                    break
            if this_user['role'] == "Admin" or \
            this_user['userID'] == my_comment['Author']:
                return my_comment
        return "You are not authorized to view all comments"

    def edit_a_comments(self,logged_in,comment_id, edit_comment):
        this_user = self.auth_user(logged_in)
        if this_user:
            count = 0
            while (count<len(Comment.comments)):
                if Comment.comments[count]["commentID"] == str(comment_id):
                    if this_user['role'] == "Admin" or \
                        this_user['role'] == "Moderator" or \
                        this_user['userID'] == Comment.comments[count]['Author']:
                        Comment.comments[count]["Message"] = str(edit_comment)
                        return Comment.comments[count]["Message"]
                count = count + 1
        return "You are not authorized to delete this comments"

    def delete_a_comment(self,logged_in,comment_id):
        this_user = self.auth_user(logged_in)
        if this_user:
            if this_user["role"] == "Admin":
                for item in Comment.comments:
                    if item["commentID"] == str(comment_id):
                        Comment.comments.remove(item)
                        return {"Status":"Comment ID "+str(comment_id)+" is deleted!"}
        return "You are not authorized to delete this comments"

    

