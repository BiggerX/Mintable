import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as pltcolors
import random
import string

def julia_quadratic(zx, zy, cx, cy, threshold):
    """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y
    belongs to the Julia set. In order to belong, the sequence 
    z[i + 1] = z[i]**2 + c, must not diverge after 'threshold' number of steps.
    The sequence diverges if the absolute value of z[i+1] is greater than 4.
    :param float zx: the x component of z[0]
    :param float zy: the y component of z[0]
    :param float cx: the x component of the constant c
    :param float cy: the y component of the constant c
    :param int threshold: the number of iterations to considered it converged
    """
    # * initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
    return threshold - 1  # it didn't diverge

def animate(i):
    ax.clear()  # clear axes object
    ax.set_xticks([])  # clear x-axis ticks
    ax.set_yticks([])  # clear y-axis ticks

    X = np.empty((len(re), len(im)))  # the initial array-like image
    cx, cy = r * np.cos(a[i]), r * np.sin(a[i])  # the initial c number

    # iterations for the given threshold
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = julia_quadratic(re[i], im[j], cx, cy, threshold)

    ax.text(10, 20, 'Julia ' + str(count), fontname='Trattatello', fontsize=18, color='white')
    ax.text(780, 20, bolodoni_letter, fontname='Bodoni Ornaments', fontsize=18, color='white')
    # ax.text(10, 710, i, fontsize=12, fontname='Hiragino Maru Gothic Pro', color='white')

    # * 'magma' is a really cool color otherwise: pltcolors.ListedColormap(np.random.rand(256,3))
    img = ax.imshow(X.T, interpolation="bicubic", cmap=color)

    return [img]

def createJuliaGIF(file_name, collection_num):
    x_start, y_start = -2, -2 # an interesting region starts here
    width, height = 4, 4  # for 4 units up and right
    density_per_unit = 200  # how many pixles per unit

    global bolodoni_letter
    bolodoni_letter = random.choice(string.ascii_letters)

    color_options = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

    global color
    color = color_options[np.random.randint(len(color_options), size=1)[0]]

    global count
    count = collection_num

    # real and imaginary axis
    global re, im
    re = np.linspace(x_start, x_start + width, width * density_per_unit )
    im = np.linspace(y_start, y_start + height, height * density_per_unit)

    global threshold
    threshold = 20  # max allowed iterations
    frames = 100  # number of frames in the animation

    # we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
    global r, a
    r = 0.7885
    a = np.linspace(0, 2*np.pi, frames)


    fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
    global ax
    ax = plt.axes()  # create an axes object
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=80, blit=True)
    anim.save(file_name, writer='imagemagick')

    print("Successfully saved " + file_name)
