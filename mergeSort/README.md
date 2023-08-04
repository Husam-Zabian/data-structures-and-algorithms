# Insertion Sort

## Feature Tasks

Implement the Merge Sort algorithm based on the given pseudocode.

## visual representations
![visual representations](./Capture.png)


## Step-by-Step Explanation

Merge Sort is a popular sorting algorithm that follows the divide-and-conquer approach. It breaks down the input array into smaller sub-arrays, sorts them, and then merges them back together to obtain the final sorted array. Let's step through the process of Merge Sort using this sample array [8, 4, 23, 42, 16, 15].


The initial array is [8, 4, 23, 42, 16, 15]. 

### Step 1: Mergesort([8, 4, 23, 42, 16, 15])

The length of the array is 6, which is greater than 1. So we proceed to split the array into two halves.

* Left: [8, 4, 23]

* Right: [42, 16, 15]


### Step 2: Mergesort([8, 4, 23])

The length of the array is 3, so we split it again.

* Left: [8]

* Right: [4, 23]


### Step 3: Mergesort([4, 23])

The length of the array is 2, so we split it again.

* Left: [4]

* Right: [23]

### Step 4: Merge([4], [23], [4, 23])
Since both left and right arrays have only one element each, we compare and merge them.

Merging the arrays:

Comparing 4 and 23: [4, 23]

* The array [4, 23] is now sorted.

### Step 5: Merge([8], [4, 23], [8, 4, 23])

We have sorted the left and right arrays from Step 3, and now we merge them with the original array.

Merging the arrays:

Comparing 8 and 4: [4, 8]
Comparing 8 and 23: [4, 8, 23]

* The array [4, 8, 23] is now sorted.

### Step 6: Mergesort([42, 16, 15])

The length of the array is 3, so we split it again.

* Left: [42]

* Right: [16, 15]

### Step 7: Merge([16], [15], [16, 15])

Since both left and right arrays have only one element each, we compare and merge them.

Merging the arrays:

Comparing 16 and 15: [15, 16]

* The array [15, 16] is now sorted.

### Step 8: Merge([42], [15, 16], [42, 15, 16])

We have sorted the left and right arrays from Step 6, and now we merge them with the original array.

Merging the arrays:

Comparing 42 and 15: [15, 42]
Comparing 42 and 16: [15, 16, 42]

* The array [15, 16, 42] is now sorted.

### Step 9: Merge([4, 8, 23], [15, 16, 42], [8, 4, 23, 42, 16, 15])

Finally, we merge the two sorted halves from Step 5 and Step 8 to obtain the fully sorted array.

Merging the arrays:

Comparing 4 and 15: [4, 15]
Comparing 8 and 15: [4, 8, 15]
Comparing 8 and 16: [4, 8, 15, 16]
Comparing 23 and 16: [4, 8, 15, 16, 23]
Comparing 23 and 42: [4, 8, 15, 16, 23, 42]

* The array [4, 8, 15, 16, 23, 42] is the final sorted array.

### Step 10: Final Sorted Array

* The final sorted array is [4, 8, 15, 16, 23, 42].

## Approach & Efficiency

Time complexity : O(nlogn) 

Space complexity : O(n)

## Solution

### [Link to code (merge Sort) ](./../mergeSort/mergeSort/mergeSort.py)

### [Link to test code (merge Sort) ](./../mergeSort/tests/test_mergeSort.py)


### to run this code :
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest

    //after finishing 
    deactivate