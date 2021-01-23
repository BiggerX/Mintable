import inquirer
from factories import mandelbrot_factory, julia_factory, random_factory

if __name__ == "__main__":
    questions = [
        inquirer.List('mint',
                    message="What do you want to mint?",
                    choices=['Mandelbrot', 'Julia', 'Random'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers["mint"] == 'Mandelbrot':
        print('Generating Mandelbrot NFTs and uploading to Mintable.app')
        mandelbrot_factory.mandelbrot_mint()
    elif answers['mint'] == 'Julia':
        print('Generating Julia NFTs and uploading to Mintable.app')
        julia_factory.julia_mint()
    else:
        print('Generating Random Image NFTs and uploading to Mintable.app')
        random_factory.random_mint()
