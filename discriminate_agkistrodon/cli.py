# -*- coding: utf-8 -*-

import click
import logging
import discriminate_agkistrodon
from keras.utils import plot_model


@click.command()
def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.info("Initializing")


@click.command()
def draw_capetian_modifier():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.info("Initializing")
    model = discriminate_agkistrodon.capetian_modifier()
    plot_model(model, to_file='model.png')


if __name__ == "__main__":
    main()
