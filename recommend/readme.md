# Recommend

Recommend is a demonstration python recommendation engine, using Standard Deviation and Thershold to recommend missing items.

# Files
## main.py
This algorithm uses various methods to compare against users to find the most similar in order to recommend units which they haven't completed

## facultyRec/*
Main file to execute is `recommend.py`, which looks at faculty and currently does a mapping based on what units an user has reviewed, does an API call to monPlan-API, then
it calculates distance based off the faculty. This will be a major component in eliminating 'unsimilar' users.

# Why?
The idea is to test out and design an algorithm to recommend items, based on 2D. Then expand forwards to 3 and more dimensions for more complex items

# How?
Firstly, where a record exists, a selected user is compared across to other users within its scope. Then using standard dev (should really use Standard Error) a factor is calculated on wether or not its close. This is then implemented into a tree with the weights as the distancce between each user. Then using the threshold, it eliminates the non close items, the default threshold is calculated using `sqrt(number of users)`.

After drawing the tree, the algorithm calculates which items are 'missing', then based on the closer user recommendations (using the tree), we calculate the average rating of each item, sorting it in ascending order.

# How can it be improved.
The algorithm has a big recursion depth `O(n^2 log(n))`, it can be improved via Machine Learning and elimination across the other dimensions. Though using Binary Search and the default python `sorted` sorting method improves complexity. It should be recommended that looping through every user is not the best way of doing this across many thousand items and tens of thousands of users, the best way of doing it is through having items which have tags, as well as using analysis on both users and items to improve complexity.  

# License

Copyright (C) Monash University 2017

Built by Eric Jiang

Licensed under the MIT License
