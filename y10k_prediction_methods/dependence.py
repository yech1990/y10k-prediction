#!/usr/bin/env python
# encoding: utf-8

## import modules

import os

import scipy as sp
import pylab as pl
import scipy.stats as st
import numpy as np
import pandas as pd

import limix.io.data as data
import limix.io.genotype_reader as gr
import limix.io.phenotype_reader as phr

import limix.modules.varianceDecomposition as var
import limix.modules.qtl as qtl
import limix.io.data as data
import limix.io.genotype_reader as gr
import limix.io.phenotype_reader as phr
import limix.io.data_util as data_util
import limix.utils.preprocess as preprocess
from limix.utils.plot import *
from limix.stats.geno_summary import *
from sklearn import linear_model
import scipy.linalg as LA
import limix.modules.lmm_fast as lmm_fast

## Prepare Working Directory

os.chdir("/home/example")
print "The working directory has been changed to \"{}\"".format(os.getcwd())

#if not os.os.path.isfile("./input_data/y10k_hybrids_Yield.hdf5"):
    #import urllib
    #urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
