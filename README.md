# Predicting quantitative traits from genome and phenome with near perfect accuracy

![Figure 2a](figure2a.png)

Python code and IPython notebooks accompanying [our paper](http://biorxiv.org/content/early/2015/10/26/029868). 

Specifically, 

## How to use

.
├── figures
│   └── figure2a.png
├── input_data
│   └── y10k_hybrids_Yield.hdf5
├── notebooks
│   ├── results1.ipynb
│   ├── results2ab.ipynb
│   ├── results2c.ipynb
│   ├── results2d.ipynb
│   ├── results2e.ipynb
│   └── results2f.ipynb
├── output
│   └── README.md
├── README.md
├── REQUIREMENT.txt
└── y10k_prediction_methods
    ├── BLUP.py
    ├── data_import.py
    ├── dependence.py
    ├── helper_functions.py
    ├── __init__.py
    ├── LMM.py
    ├── midparent.py
    ├── MRF.py
    ├── MTLMM.py
    ├── QTL_fitting.py
    └── train_and_test_sets.py

### wrapped script for different prediction methods
- `train_and_test_sets.py` - code for partitioning individuals into four sets, as shown in Figure 3a
- `BLUP.py` - fitting the BLUP model
- `QTL_fitting.py` - constructing and fitting the QTL model
- `LMM.py` - constructing and fitting the LMM and LMM+P models
- `MTLMM.py` - fitting the multi-trait LMM
- `MRF.py` - fitting the mixed random forest

### jupyter notebooks
- 
-
-
- 

[This notebook](results2ab.ipynb) was used to produce the results for Figure 2. 
All models were fitted using [Limix](https://github.com/PMBio/limix). 
