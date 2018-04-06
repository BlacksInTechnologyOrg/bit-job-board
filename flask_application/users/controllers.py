import datetime
import json

from flask import Blueprint, request, redirect, render_template
from flask_application.s3upload import uploadprofilepic
from flask_security import login_required, current_user
from flask_application.controllers import TemplateView
from flask_application.users.models import User, Contract
from flask_application.users.forms import ProfilePicForm
from flask_application.awskey import cdn,bucket
users = Blueprint('users', __name__)


class ProfileView(TemplateView):
    blueprint = users
    route = '/profile'
    route_name = 'profile'
    template_name = 'profiles/profile.html'
    decorators = [login_required]
    methods = ['GET','POST']

    def dispatch_request(self, *args, **kwargs):
        form = ProfilePicForm()
        jobs = Contract.objects

        if request.method == 'POST':
            profilepicture = form.profilepic.data
            uploadprofilepic(profilepicture, current_user.username)
            return redirect("/profile")

        contractlistjson = jobs(author=current_user.id).to_json()
        contractlist = json.loads(contractlistjson)

        print(contractlist)
        profilepic = cdn + current_user.username + "/images/profiledata/" + current_user.username + "_profilepic.jpg"
        return render_template(self.template_name, form=form, profilepicture=profilepic, contractlist=contractlist)
