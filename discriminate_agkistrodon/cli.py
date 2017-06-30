# -*- coding: utf-8 -*-

import click
import logging
import sys
import discriminate_agkistrodon


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.info("Initializing")

    model = discriminate_agkistrodon.capetian_modifier()

if __name__ == "__main__":
    main()