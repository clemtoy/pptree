# -*- coding: utf-8 -*-
"""
Ettore Forigo (c) 2020
"""

from itertools import chain, zip_longest, repeat

JOINER_WIDTH = 3
DEFAULT_JOINER = ' ' * JOINER_WIDTH
CONNECTION_JOINER = '─' * JOINER_WIDTH
L_BRANCH_JOINER = '─┘ '
LR_BRANCH_JOINER = '─┴─'
R_BRANCH_JOINER = ' └─'


def multijoin(blocks, joiners=()):
    f"""
    Take one block (list of strings) or more and join them line by line with the specified joiners

    :param blocks: [['a', ...], ['b', ...], ...]
    :param joiners: ['─', ...]
    :return: ['a─b', ...]
    """

    # find maximum content width for each block
    block_content_width = tuple(max(map(len, block), default=0) for block in blocks)

    return tuple(

        joiner.join(

            (string or '')                 # string if present (see fillvalue below)
            .center(block_content_length)  # normalize content width across block

            for string, block_content_length in zip(block, block_content_width)

        )

        for block, joiner in zip(zip_longest(*blocks, fillvalue=None),
                                 chain(joiners, repeat(DEFAULT_JOINER))) # joiners or default

    )


def wire(block, connector):
    left_c = ' ' if connector == '┌' else '─'
    right_c = ' ' if connector == '┐' else '─'

    length = len(block[0])

    length -= 1  # connector
    left = length // 2
    right = length - left

    return multijoin([[
        f'{left_c * left}{connector}{right_c * right}',
        *block
    ]])


def branch(blocks):
    wired_blocks = tuple(map(lambda blk: wire(blk, '┬'), blocks))

    return multijoin(wired_blocks, (CONNECTION_JOINER,))


def branch_left(blocks):
    last, *rest = blocks

    last = wire(last, '┌')
    rest = branch(rest)

    return multijoin([last, rest], (CONNECTION_JOINER,))


def branch_right(blocks):
    *rest, last = blocks

    rest = branch(rest)
    last = wire(last, '┐')

    return multijoin([rest, last], (CONNECTION_JOINER,))


def connect_branches(left, right):
    joiner = (LR_BRANCH_JOINER if right else L_BRANCH_JOINER) if left else R_BRANCH_JOINER

    return multijoin([left, right], (joiner,))


def blocklen(block):
    if block:
        return len(block[0])

    else:
        return 0
