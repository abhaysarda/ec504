# ec504
# Adv. Data Structures and Algorithms Project on LSH and KD-trees

This project involves developing and testing LSH and KD-tree implementations.

The problem that we are seeking to apply this to is applying the same to weather data to predict power outages. The corresponding data files and final implementation are in the Final Implementation folder.



# Running the code yourself

The final project is inside the Final Implementation folder. There are three parts to the project: Data Analysis, Locality Sensitive Hashing and KD-trees

# Data Analysis
The Data Analysis folder takes in 8 years of data from Michigan and analyzes it. We remove multicollinear variables and use the SelectKBest features library to extract the most correlated features. The final data is outputted as a csv file for the other programs to use.

# Locality Sensitive Hashing
The two different LSH implementations can be run from the jupyter notebooks. One uses the Cosine similarity, while the other is a custom one, that we designed from scratch. It actually beats actual kNN, which means we could have optimized the kNN more.

# KD-trees
The two different KD-tree implementations are in two separate folder. One is using the SciPy KD-tree modules, which acts as a benchmark for the other one. The other one is a custom one written for the project.

As long as you have anaconda installed, the notebooks should run perfectly! Simply run the jupyter notebooks!

# Accuracy
kNN: 92.18%
LSH: 95.6%
KD-trees: 89%
