import inquirer
from factories import mandelbrot_factory, julia_factory, random_factory, mandelbrot_dive_factory, invader_factory, rainbow_factory, taste_factory

if __name__ == "__main__":
    questions = [
        inquirer.List('mint',
                      message="What do you want to mint?",
                      choices=['Taste', 'Random Rainbow', 'Invader', 'Julia', 'Mandelbrot',
                               'Mandelbrot Dive', 'Random Gif', 'Random Image'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    if answers["mint"] == 'Mandelbrot':
        print('Generating Mandelbrot NFTs and uploading to Mintable.app')
        mandelbrot_factory.mandelbrot_mint()
    elif answers['mint'] == 'Julia':
        print('Generating Julia NFTs and uploading to Mintable.app')
        julia_factory.julia_mint()
    elif answers['mint'] == 'Invader':
        print('Generating Invader NFTs and uploading to Mintable.app')
    elif answers['mint'] == 'Taste':
        print('Generating Taste NFTs and uploading to Mintable.app')
        taste_factory.taste_mint()
    elif answers['mint'] == 'Random Rainbow':
        print('Generating Random Rainbow NFTs and uploading to Mintable.app')
        rainbow_factory.random_rainbow_mint()
    elif answers['mint'] == 'Mandelbrot Dive':
        print('Generating Mandelbrot Dive NFTs and uploading to Mintable.app')
        mandelbrot_dive_factory.mandelbrot_mint()
    elif answers['mint'] == 'Random Gif':
        print('Generating Random Gif NFTs and uploading to Mintable.app')
        # random_gif_factory.mint_gif()
    else:
        print('Generating Random Image NFTs and uploading to Mintable.app')
        random_factory.random_mint()
