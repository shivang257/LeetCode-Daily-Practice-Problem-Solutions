# Determine if Two Trees are Identical
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two binary trees, the task is to find if both of them are identical or not.&nbsp; </span></p>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>     1          1
&nbsp;  /   \      /   \
&nbsp; 2     3    2     3
<strong>Output: </strong>Yes<strong>
Explanation: </strong>There are two trees both
having 3 nodes and 2 edges, both&nbsp;trees
are identical having the&nbsp;root as&nbsp;1,
left child of 1 is 2&nbsp;and right child
of 1 is 3.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>    1       1
&nbsp; /  \     /  \
&nbsp;2    3   3    2
<strong>Output: </strong>No<strong>
Explanation: </strong>There are two trees both
having 3 nodes and 2 edges, but both
trees are not identical.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your&nbsp;task:</strong><br>
Since this is a functional problem you don't have to worry about input, you just have to complete the function <strong>isIdentical()</strong> that takes two roots as parameters and returns true or false. The printing is done by the driver code.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(Height of the Tree).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= Number of nodes &lt;= 10<sup>5</sup><br>
1 &lt;=Data of a node &lt;= 10<sup>5</sup></span></p>
</div>