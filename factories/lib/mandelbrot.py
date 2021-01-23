from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as pltcolors
import math
import random
import string

# * Animated Gif class to abstract details
class AnimatedGif:
    def __init__(self, size=(640, 480)):
        self.fig = plt.figure()
        self.fig.set_size_inches(size[0] / 100, size[1] / 100)

        # * Create random color for background
        r = lambda: random.randint(0,255)
        self.background_color = pltcolors.ListedColormap(np.random.rand(256,3))

        # * Create random color for foreground
        r = lambda: random.randint(0,255)
        self.foreground_color = pltcolors.ListedColormap(np.random.rand(256,3))

        # * Choose random bodoni letter
        self.bodoni_letter = random.choice(string.ascii_letters)

        self.fig.patch.set_facecolor('black')
        ax = self.fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
        ax.set_xticks([])
        ax.set_yticks([])
        self.images = []

    def add(self, image, stamp='Burro', is_background=False, label=''):
        cmap_color = self.foreground_color
        if is_background:
            cmap_color = self.background_color
        plt_im = plt.imshow(image, cmap=cmap_color, vmin=0, vmax=1, animated=True)
        text_color = [1 - i for i in pltcolors.ListedColormap(cmap_color.colors[::-1]).colors[len(cmap_color.colors) - 1]]
        opposite_color=pltcolors.to_hex(text_color)
        plt_txt = plt.text(10, 310, label, fontsize=8, fontname='Hiragino Maru Gothic Pro', color='white')

        # * Cool fonts: Zapfino, Apple Chancery, Trattatello
        stamp = plt.text(10, 20, stamp, fontname='Trattatello', fontsize=12, color='white')
        bodoni_stamp = plt.text(460, 20, self.bodoni_letter, fontname='Bodoni Ornaments', fontsize=12, color='white')

        # * Append everything
        self.images.append([plt_im, plt_txt, stamp, bodoni_stamp])

    def set_text(self, label):
        self.images.append([self.images[len(self.images)-1][0], plt.text(10, 310, label, fontsize=8, fontname='Hiragino Maru Gothic Pro', color='white'), self.images[len(self.images)-1][2], self.images[len(self.images)-1][3]])

    def save(self, filename):
        animation = anim.ArtistAnimation(self.fig, self.images)
        animation.save(filename, writer='imagemagick', fps=20)

def createMandelbrotGIF(file_name, collection_num):
    m = 480
    n = 320
    animated_gif = AnimatedGif(size=(m, n))

    # * Generate Stamp
    stamp = 'Burro ' + str(collection_num)

    # * Generate Initial Image
    x = np.linspace(-2, 1, num=m).reshape((1, m))
    y = np.linspace(-1, 1, num=n).reshape((n, 1))
    C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    Z = np.zeros((n, m), dtype=complex)
    M = np.full((n, m), True, dtype=bool)
    animated_gif.add(M, stamp, label='0', is_background=True)

    images = []
    for i in range(1, 100):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        if i <= 15 or not (i % 4):
            animated_gif.add(M, stamp, label=str(i))
        #     else:
        #     animated_gif.set_text(label=str(i))
    animated_gif.save(file_name)
    print("Successfully saved " + file_name)


# def createFractal(file_name):
#     dimensions = (800, 800)
#     scale = 1.0/(dimensions[0]/3)
#     center = (2.2, 1.5)       # Use this for Mandelbrot set
#     #center = (1.5, 1.5)       # Use this for Julia set
#     iterate_max = 100
#     colors_max = 50

#     img = Image.new("RGB", dimensions)
#     d = ImageDraw.Draw(img)

#     # Calculate a tolerable palette
#     palette = [0] * colors_max
#     for i in xrange(colors_max):
#         f = 1-abs((float(i)/colors_max-1)**15)
#         r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
#         palette[i] = (int(r*255), int(g*255), int(b*255))

#     # Calculate the mandelbrot sequence for the point c with start value z
#     def iterate_mandelbrot(c, z = 0):
#         for n in xrange(iterate_max + 1):
#             z = z*z +c
#             if abs(z) > 2:
#                 return n
#         return None

#     # Draw our image
#     for y in xrange(dimensions[1]):
#         for x in xrange(dimensions[0]):
#             c = complex(x * scale - center[0], y * scale - center[1])

#             n = iterate_mandelbrot(c)            # Use this for Mandelbrot set
#             #n = iterate_mandelbrot(complex(0.3, 0.6), c)  # Use this for Julia set

#             if n is None:
#                 v = 1
#             else:
#                 v = n/100.0

#             d.point((x, y), fill = palette[int(v * (colors_max-1))])

#     del d
#     img.save(file_name)