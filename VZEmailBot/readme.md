To get this script running, you will need to do the following:

ssh-add - so that the shell scripts that are running in conjunction with the python script will still run without being prompted for a password

Run script as such: /path/to/pythonscript.py &  <--- this is so the script will run in background and you can keep doing stuff on the terminal

As a note, you should also specify the path for the shell scripts so that they will also run correctly.

Join the slack channel (Shouldn't be an issue since I will invite the team)

You will need to edit the paths in the python script so that the shell scripts are calling from the correct path. Otherwise the shell scripts will not work.

This will essentially make it so NOC does not have to post the summary e-mail tasks on a daily basis at 4 PM as well as the weekly which occurs on Monday.

It will also be a way to ensure we are monitoring failures on the weekly tasks as the bot will be posting to the slack channel.

If you need help setting this up, please do not hesitate to ask me directly

---Chris A 
