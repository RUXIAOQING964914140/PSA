# PSA
# INSTALLATION

# Requirements:

Python 3.9x (may work with earlier versions, not tested)

Blast 2.16.0

clustalo 1.2.4 

mafft 7.525 

muscle 5.3 

foldseek

Java environment

Methods:Protein Similarity Alignment Methods.docx

# Usage

#### Neighborhood：

Identify the highly similar neighbors of the target protein:KIBA_sim_Top5_ner.ipynb

##### Feature:

Type1 「Features include: mean, standard deviation, median, count of non-missing affinity values, mode, top 5 maximum values, and top 5 minimum values per row (calculated after removing NaNs), totaling 15 dimensions.」
Specificity-Based Statistical Features : KIBA_Protein_Drug_singlefea.ipynb.

Type2 「The features of highly similar neighbors are incorporated as supplementary features for the target entity.」
Neighbor-Based Statistical Features: Protein_nerFea.ipynb
Affinity-Based Neighborhood Features:affinity_fea.ipynb

#### L2R format:

Format the data according to the requirements of the L2R algorithm：drug_protein_all_feature.ipynb

#### Train and Test

 Obtain the index value of each sample:5_fold.ipynb
 Split the dataset into training and test sets based on index values (5-fold cross-validation):sample_split.ipynb
 Training:mafft_train.py
 Testing:mafft_test.py

# Evaluation criteria:

MSE

CI

Rm2




##### Note:

Some data processing is done with linux commands,the code is simple, therefore the specific code is not listed.

We have provided the code used in this work, omitting repeatedly used sections. The listed code is sufficient to reproduce the experimental procedures.
