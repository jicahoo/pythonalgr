# pythonalgr
Learn algorithm using python on leetcode.

## 385. Mini Parser
* How to find the list's elements? You have to find the comma in the first level. 
* How to deteremine the firt level? Use stack (which is tracking the pair of "[" and "]") to determine if current comma is in the first level.

## 383. Ransom Note [TODO]
* Try to write code directly. Ran into several issues: alogrithm is not right (since not use pseudo code and prove its correct), not familiar with Pythons's list index operation.
* Try to avoid m*n time complexity.
* Now time complexity: n*logn+m*logm+m*n, it seems that I failed on my goal. Space complexity: if sorted is in-place, it should be O(1)
* TODO: Like a sub-set check of set with duplicate elements; Another possible better way is to use Hash. From problem itself, we don't need sort. It's more about set operation.