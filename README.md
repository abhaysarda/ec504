# ec504
Adv. Data Structures and Algorithms Project on LSH and KD-trees

### Using the LSH_minhash_Jaccard_Shuffle.py to find percentage similarity between two documents:

Variables a,b,c are used to store the contents of the documents. The contents can be changed/updated. Run 

``python3 LSH_minhash_Jaccard_Shruthi.py`` 

The output will be a percentage measure of the similarity between each pair of documents.

For the sample sentences:

a = "Who was the first king of Poland"
b = "Who was the first ruler of Poland"
c = "Who was the last pharaoh of Egypt",

the output would look as follows-

>0.7450980392156863 0.29411764705882354 0.3333333333333333

This indicates the higher measure of similarity between sentences a and b as compared to (a,c) and (b,c).

### Using the cosineDist.py to find percentage similarity between two documents:

The code has been designed such that it outputs the percentage similarity in terms of the cosine measure and hash value comparison. If the "Hash" section of the output is 1, it would mean that the hash values are identical and the two points would fall inside the same bucket. However, this would vary from the "Angle" sections since "Angle" quantifies the exact similarity between the two points and hence cannot be used for approximate nearest neighbour search. The "Error" section calculates the error betweeen the "Angle" measure of similarity and "Hash" measure of similarity. In other words, it quantifies the "nearness" of 2 neighbours. 

Sample output:

> Angle:  0.5765716493563977 Hash:  1.0 Error:  -0.7343898214840381 %

Here, even though the points were far off (see Error value), they were put in the same bucket with regards to the hash value. 

