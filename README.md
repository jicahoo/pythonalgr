# pythonalgr
Learn algorithm using python on leetcode.

## 94. Binary Tree In Order Traversal
今天, 在脑海里, 总结了一下三种二叉树遍历的迭代实现方式, 有一些感悟:
1. 先序的迭代实现是最简单的, 因为你只需要访问根节点一次, 访问之后, 就可以从栈中丢弃, 放入子树的节点, 就可以完成后续的工作.
2. 中序遍历的迭代实现, 核心操作, POP时,如果有右孩子, 把右孩子的最左一串入栈. 出栈的是, 这个节点的相对角色是个root节点. 所以
出栈时, 左子树已遍历完毕, 然后, root出栈, 再将右子树遍历. 次栈顶元素是刚POP出的元素的父节点, 关系反过来, POP出元素是次栈顶元素的左孩子, 逻辑以和上面的
'root出栈时, 它的左子树以遍历完毕'形成完备的逻辑和算法流程.
3. 注意栈中相邻节点的逻辑关系, 在中序遍历中, 相邻节点是左孩子和父节点的关系, 父节点更靠栈底, 或者是 父节点的左孩子的右子树的某些节点与父节点的关系. 有助于理解算法.
4. 迭代中, 仍有递归的思想. 要以子树作为一个整体去构造算法和理解算法. 而不仅仅是, 左孩子, 右孩子。要理解为左子树, 右子树.
5. 后序遍历, 要走根节点两次, 复杂些. 父节点是从左节点到右节点的桥梁, 因为是后续, 所以要保存父节点, 走完左子树, 从父节点, 找到右子树啊, 再回到父节点.
6. 在中序遍历和后续遍历中, 最左串是算法的脉络或者二叉树的脉络.

## 136. Single Number
* Just use xor. 
* xor operation has below mathematical property: 0 xor n = n; n xor n = 0; n xor m = m xor n. You can easily prove that below solution is correct.

```python
return reduce(lambda x, y : x ^ y, numbers, 0);
```

## 144. Binary Tree Preorder Traveral. 二叉树先序遍历
* 算法复杂度是怎样的?

## 145. Binary Tree Postorder Traversal. 二叉树后序遍历
* 经过不懈努力, 写出了一个简洁版本. 如果你的代码看着有重复的地方, 重复的逻辑, 重复的循环, 总有奇奇怪怪的变量, 你总是可以去除它.
* 我写的解法的结构和94题的二叉树中序遍历是一模一样的. 其实是受了94题的解法的启发, while循环担任了两层循环职责. 一个是驱动整体逻辑, 一个是驱动不断地POP栈顶元素.
* 在遍历树的节点的时候, 你要不断地改变自己的参照系. 在不同的步骤中, 你可能会选择不同的节点作为所谓的当前的根节点, 以选中的根节点, 思考如何进行
下一步操作, 所以, 你要足够小心, 不要把这个参照系, 在不断的变换中, 弄混了.


## 146. LRU Cache
* Result: Beat 43%. Time: O(1), Space: O(n). Time spent: 4 hours.
* Not easy to operate the pointers in the doubly linked list correctly. Need to be very carefully. 
* Many internal structure and variable for maintaining a O(1) LRU cache. Need to update them carefully. 

## 155. Min Stack
* The simple and straightforward way may be the fast one.
* Use MaxHeap structure is not good choice, comparing the simple solution. The simpe solution beats 60%, the bad one beats only <10%.

## 227. Basic Calculator II
* Result: Beat 63%. Time: O(n), Space: O(n)
* Think about how do you calculate + - * /
* String basic paring method: regex, split, strip, then process tokens as list. Just  string -> split -> list -> process linearly.
* We can handle them linearly, since it is simple string without '(' or negative number. How to handle more complex expression?
* More better way?

## 241. Different ways to add parentheses.
* TODO

## 338. Count Bits
* Result: Best score 95%  Time:O(n) Space: O(n)
* Question Tag: DP, Bit Operation.
* The mechanism of binary digits: try to get the DP formula: 
* number_of_bits(n) = number_of_bits(n/2) if n is even;
* number_of_bits(n) = number_of_bits(n/2) + 1 if n is odd.
* number_of_bits(0) = 0.
* Learned: the step in DP may not be n -> n + 1. In this question, the step in DP is n/2 -> n. Generally, f(n) = DP(m). 1 < m < n.


## 385. Mini Parser
* How to find the list's elements? You have to find the comma in the first level. 
* How to determine the first level? Use stack (which is tracking the pair of "[" and "]") to determine if current comma is in the first level.

## 387. First unique character in a string.
* Score: 80%. Time: O(n) Space: O(n).
* Note: Not store useless info. Just store the index of char if there is no dup currently. If found dup, just set -1.

## 383. Ransom Note [TODO]
* Just follow the most natural way. Time complexity: m+n+n. Space complexity: 26*size( store "letter":[count_a,count_b] )
* Try to write code directly. Ran into several issues: alogrithm is not right (since not use pseudo code and prove its correct), not familiar with Pythons's list index operation.
* Try to avoid m*n time complexity.
* Now time complexity: n*logn+m*logm+m*n, it seems that I failed on my goal. Space complexity: if sorted is in-place, it should be O(1)
* TODO: Like a sub-set check of set with duplicate elements or common sub-string check problem;
Another possible better way is to use Hash. From problem itself, we don't need sort. It's more about set operation.
* I learned to use assert of Python to run my test case.
* I didn't think out complete & useful test cases, just hurried up to submit my code.
* Two things I got: Think clear about the algorithm: pseudo code prove and complete test case. Maybe 80% is on it, 20% to write code. Try to stick to it.

## 421. Max XOR value in array.
* Current result beats 7% in python. More details, see the comments of code.

## 422. Find duplicates (twice) in array.
* Beats 72%. Time: O(n), Space: O(1). 
* Solution: Leverage mod operation. 
* What I learned: read question carefully, especially the key condition: 1 <= a[i] <= n and repeats **twice**
