# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Jackokie Zhao
# Data:     2017年07月19日
# =========================================================================

"""Multi-threaded word2vec mini-batched skip-gram model.
Trains the model described in:
(Mikolov, et. al.) Efficient Estimation of Word Representations in Vector Space
ICLR 2013.
http://arxiv.org/abs/1301.3781
This model does traditional minibatching.
The key ops used are:
* placeholder for feeding in tensors for each example.
* embedding_lookup for fetching rows from the embedding matrix.
* sigmoid_cross_entropy_with_logits to calculate the loss.
* GradientDescentOptimizer for optimizing the loss.
* skipgram custom op that does input processing.
"""

import argparse
import sys
import os
import time

import numpy as np
import tensorflow as tf

FLAGS = None


class Word2Vec(object):
    """ Word2Vec model (Skipgram)."""

    def __init__(self, options, session):
        self._options = options
        self._session = session
        self._word2

def build_graph(self):
    """ Build the graph for the full model."""
    (words, counts, words_per_epoch, se;f/)


def main(_):
    if tf.gfile.Exists(FLAGS.log_dir):
        tf.gfile.DeleteRecursively(FLAGS.log_dir)
    tf.gfile.MakeDirs(FLAGS.log_dir)
    if not FLAGS.train_data or not FLAGS.eval_data or not FLAGS.save_path:
        print('--train_data --eval_data and --save_path must be specified.')
        sys.exit(1)

    with tf.Graph().as_default(), tf.SEssion() as session:
        with tf.device('/cpu:0'):
            model =  word2vec(opts, session)
            model.read_analogies() # Read analogies questions.

        for _ in range(FLAGS.epoch):
            model.train()   # Process one epoch.
            model.eval()    # Eval analogies.
        # Perform a final save.
        model.saver.save(session,
                        os.path.join(FLAGS.save_path, 'model.chpt'),
                        global_step=model.global_step
        )



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--learning_rate',
        type=float,
        default=0.01,
        help='Initialize learning rate.'
    )

    parser.add_argument(
        '--log_dir',
        type=str,
        default='./log_dir',
        help='Directory to put the log data.'
    )

    parser.add_argument(
        '--save_path',
        type=str,
        default=None,
        help='Directory to write the model and training summaries.'
    )

    parser.add_argument(
        '--train_data',
        type=str,
        default=None,
        help='Training the text file. E.g. download and unzip form. \
                http://mattmahoney.net/dc/text8.zip.'
    )

    parser.add_argument(
        '--eval_data',
        type=str,
        default=None,
        help="File consisting of analogies of four tokens.\
                embedding 2 - embedding 1 + embedding 3 should be close \
                to embedding 4."
    )

    parser.add_argument(
        '--embedding_size',
        type=int,
        default=200,
        help='The embedding dimension siez.'
    )

    parser.add_argument(
        '--epoch',
        type=int,
        default=200,
        help='Number of epochs to train. Each epoch processes the training data\
                once completely.'
    )

    parser.add_argument(
        '--batch_size',
        type=int,
        default=16,
        help='Number of training examples processed per step.\
                (Size of minibach).'
    )

    parser.add_argument(
        '--no_neg_sample',
        type=int,
        default=100,
        help='Negtive samples per training example.'
    )

    parser.add_argument(
        '--current_step',
        type=int,
        default=0,
        help='The number of current training steps.'
    )

    parser.add_argument(
        '--window_size',
        type=int,
        default=5,
        help='The number of words to predict to the left and right\
                of the target word.'
    )

    parser.add_argument(
        '--min_count',
        type=int,
        default=5,
        help='The minimum number of word occurrences for it to be included\
                in the vocabulary.'
    )

    parser.add_argument(
        '--sub_sample',
        type=float,
        default=1e-3,
        help='Subsample threthold for word occurrence. Words that appear \
                with higher frequency will be randomly down-sampled. \
                Set to 0 to disable.'
    )

    parser.add_argument(
        '--static_interval',
        type=int,
        default=5,
        help='Print statistics every n seconds.'
    )

    parser.add_argument(
        '--summary_interval',
        type=int,
        default=5,
        help='Save training summary to file every n seconds.'
    )

    parser.add_argument(
        '--checkpoint_interval',
        type=int,
        default=600,
        help='Checkpoint the model (i.e. save the parameters) every n seconds.'
    )

    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
