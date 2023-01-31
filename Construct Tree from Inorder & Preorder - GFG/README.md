# Construct Tree from Inorder & Preorder
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given 2 Arrays of Inorder and preorder traversal. The tree can contain duplicate elements. Construct a tree and print the Postorder traversal.&nbsp;</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 4
inorder[] = {1&nbsp;6 8 7}
preorder[] = {1 6 7 8}
<strong>Output: </strong>8 7 6 1</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 6
inorder[] = {3 1 4 0 5 2}
preorder[] = {0 1 3 4 2 5}
<strong>Output: </strong>3 4 1 5 2 0<strong>
Explanation: </strong>The tree will look like
&nbsp; &nbsp;    0
&nbsp; &nbsp;&nbsp;/&nbsp; &nbsp; &nbsp;\
&nbsp; &nbsp;1&nbsp; &nbsp; &nbsp; &nbsp;2
&nbsp;/&nbsp; &nbsp;\&nbsp; &nbsp; /
3&nbsp; &nbsp; 4&nbsp; &nbsp;5</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Your task is to complete the function <strong>buildTree()&nbsp;</strong>which takes 3 arguments(inorder traversal array, preorder traversal array, and size of tree n) and returns the root node to the tree constructed. You are not required to print anything and a new line is added automatically (The post order of the returned tree is printed by the driver's code.)</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong>: O(N*N).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=Number of Nodes&lt;=1000</span></p>
</div>