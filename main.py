import inquirer
import os
import importlib
import sys
sys.path.insert(0, './factories')

if __name__ == "__main__":
    directory = os.fsencode('./factories')
    actions = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".py"):
            file_path = './factories/' + filename
            actions.append(filename.replace('.py', ''))

    questions = [
        inquirer.List('mint',
                      message="What do you want to mint?",
                      choices=actions,
                      ),
    ]
    answers = inquirer.prompt(questions)

    module = importlib.import_module(
        'factories.' + answers['mint'], package=sys.path)
    mint = getattr(module, 'mint')
    mint()
