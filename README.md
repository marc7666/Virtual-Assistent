# Basic ChatBot

## bot.py

chatterbot library => Is a Python library that makes it easy to generate automated responses to a user’s input. ChatterBot uses a selection of machine learning algorithms to produce different types of responses.

The first step it's to create an object of the ChatBot class and giving to him a name. Then, the possible initial data of the dialog is eliminated. Third the file that contends the inputs (introduced by the user) and the responses of the bot is opened in reading mode. Next, the object that will train the bot is created. In the next step, the program trains the bot using the knowledge.bc file. Finally, with a loop the communication flow is done. Inside the loop, the first step is to request something to the user, second the program searches the most adequate response in the file, third the response is printed and finally, in every loop, the program checks if the answer of the bot is a determined one to kill the program.

knowledge.bc file => This file contents the dialog. The structure of this file is:
-> User input
-> Bot response

If the user introduces a input that is not in the knowledge.bc file, the bot will answr with the most adequate response (using his own criteria)
