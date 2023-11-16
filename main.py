import getopt
import sys
import argparse

from models.rankgan.Rankgan import Rankgan
from utils.text_process import add_spaces


def set_gan(input_file):
    gans = dict()
    gans['rankgan'] = Rankgan
    Gan = gans['rankgan']
    gan = Gan()
    gan.vocab_size = 20
    gan.generate_num = 100
    gan_func = gan.train_real
    gan.pre_epoch_num = 5
    gan.adversarial_epoch_num = 10

    token_file = 'data/token.txt'
    add_spaces(input_file, token_file)
    gan_func(token_file)
    return gan



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GAN Training Script')
    parser.add_argument('-d', '--data-file', type=str, default='data/amp.txt', help='Path to the input data file')
    args = parser.parse_args()

    input_file = args.data_file

    gan = None
    set_gan(input_file)
