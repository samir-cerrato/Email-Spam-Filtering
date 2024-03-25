# Email-Spam-Filtering
Get familiar with randomized algorithm design and development


1.1 Problem description

You are implementing a Bloom filter for email spam filtering given
that you know the set A of n trusted email addresses. If the email
comes from one of these trusted addresses, it is not a spam. Otherwise, it will be a spam. Since the
server memory is very limited, you can not keep the list of trusted addresses on its memory (if an email
address requires 25 bytes on average and you have 1 billion trusted emails, it would take 25 GB to store
A in the memory).
Due to the limited resources, instead of using a string, we use a random integer in [0 . . . 2^31]
to present an email address. Also, to simpify the task, please use the following code to generate the list
of n integers that represent for n email addresses. Note that you have to use random.seed(320) to
ensure that you generate the same set of integers as automarker.

You would need to write a Python script to implement a Bloom filter given the setting of m = 8n bits and
different numbers of hash functions k = {2, 4, 6, 8}. The used hash function is: f (x) = (a ·x + b) mod m
where a and b are generated using the following code:

import random

random.seed(320)

n = 100

a = [1, 2, 3, 4, 5, 6, 7, 8]

b = [8, 7, 6, 5, 4, 3, 2, 1]

for i in range(n):

x = random.randint(0, 2**31)


Note that you must not call x = random.randint(0, 2**31) several times since it will generate different sets S.

Given k = i, you will use i hash functions, from f1 to fi(x) = (a[i −1] ·x + b[i −1]) mod m. For
example, given k = 2, you will use
f1(x) = (a[0] ·x + b[0]) mod m = (x + 8) mod m
and
f2(x) = (a[1] ·x + b[1]) mod m = (2x + 7) mod m.

1.2 Test case description

Your test will be a sequence of 2000 integers, each value per line corresponding to the email address,
containing non-spam and spam emails. Your output will be 4 integers, each per line, that count the
number of detected spam emails for each value of k = {2, 4, 6, 8}
