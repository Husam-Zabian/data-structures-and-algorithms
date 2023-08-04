# Insertion Sort

## Feature Tasks

Implement the Insertion Sort algorithm based on the given pseudocode.

## visual representations
![visual representations](./Capture.png)


## Step-by-Step Explanation

 let's trace the algorithm step-by-step using the provided sample array [8, 4, 23, 42, 16, 15].

#### Pass 1:

sorted array: [8]


#### Pass 2:

sorted array: [4, 8]

#### Pass 3:

sorted array: [4, 8, 23]

#### Pass 4:

sorted array: [4, 8, 23, 42]

#### Pass 5:

sorted array: [4, 8, 16, 23, 42]

#### Pass 6:

sorted array: [4, 8, 15, 16, 23, 42]


#### After the sixth pass, the array is completely sorted.

## Approach & Efficiency

Time complexity worst-case: O(n^2) 

Time complexity best case: O(n)

Space complexity : O(1)

## Solution

### [Link to code (Insertion Sort) ](./../insertionSort/insertionSort/insertionSort.py)

### [Link to test code (Insertion Sort) ](./../insertionSort/tests/test_insertionSort.py)


### to run this code :
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest

    //after finishing 
    deactivate