import getopt
import sys

from models.rankgan.Rankgan import Rankgan
from utils.text_process import add_spaces


def set_gan():
    gans = dict()
    gans['rankgan'] = Rankgan
    Gan = gans['rankgan']
    gan = Gan()
    gan.vocab_size = 20
    gan.generate_num = 100
    gan_func = gan.train_real
    gan.pre_epoch_num = 5
    gan.adversarial_epoch_num = 10

    input_file = 'data/amp.txt' ############ path for input file ########################


    token_file = 'data/token.txt'
    add_spaces(input_file, token_file)
    gan_func(token_file)
    return gan



if __name__ == '__main__':
    gan = None
    set_gan()
