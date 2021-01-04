# Captain America v.s. Iron Man - Can Bayes tell one from the other?

> The aim of this repo is to demonstrate how to build a simple Machine Learning Model (Naive Bayes Classifier) for performing the task of author identification in a complete end-to-end manner. 

This repo goes along with a set of Medium posts [the first](https://medium.com/swlh/author-identification-using-naive-bayes-algorithm-1-abeeb88eb862) of which could be accessed here and the links to subsequent posts are embedded sequentially in the individual posts.

We will build a binary classifier which given a dialogue, predicts if it's more likely to have been uttered by Captain America or by Iron Man. Once we train a ML model to do the same, we shall expose an API endpoint using **Flask** and **Flasgger** and containerize it with the help of **Docker**. Finally we shall host our docker container on a platform so that people can utilize this endpoint to make inferences.

The project is structured in the following stages

1. [Data Collection & Preprocessing](https://medium.com/swlh/author-identification-using-naive-bayes-algorithm-1-abeeb88eb862): We scrape the fandom website using *requests* library and parse it with *beautifulsoup* and do some preprocessing with *regex* to get the dialogues spoken by Captain America and Iron Man respectively in the three films *Captain America: The first avenger*, *Iron Man* and *Avengers: Endgame*. The dialogues from former two films will serve as the training data and the last one will be our test data.

2. [Training a Naive Bayes Classifier](https://medium.com/swlh/author-identification-with-naive-bayes-algorithm-2-8b43854c1429): We shall understand the Naive Bayes Classifier, it's working and how conditional probability is leveraged in this task using Bayes' Theorem.

3. Creating an API endpoint & Dockerizing the application: Using Flask and Flasgger we expose an API endpoint for our model to perform inference on user defined text and subsequently containerize it using docker.
