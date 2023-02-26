# Three way partitioning
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of size n&nbsp;and a range [<strong>a</strong>, <strong>b</strong>]. The task is to partition the array around the range such that array is divided into three parts.<br>
1) All elements smaller than <strong>a</strong> come first.<br>
2) All elements in range <strong>a</strong> to <strong>b</strong> come next.<br>
3) All elements greater than <strong>b</strong> appear in the end.<br>
The individual elements of three sets can appear in any order. You are required to return the modified array.<br>
<br>
<strong>Note</strong>: The generated output is 1 if you modify the given array successfully.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
<strong>Output:</strong> 1
<strong>Explanation</strong>: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.</span>

</pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
n = 3 
A[] = {1, 2, 3}
[a, b] = [1, 3]
<strong>Output</strong>: 1
<strong>Explanation: </strong>One possible arrangement 
is: {1, 2, 3}. If you return a valid
arrangement, output will be 1.

</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task: </strong><br>
You don't need to read input or print anything.&nbsp;The task is to complete the function <strong>threeWayPartition()</strong> which takes the array[], a, and b as input parameters and modifies the array in-place according to the given conditions.</span><br>
<br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(n)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span><br>
<br>
<br>
<span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 &lt;= n&nbsp;&lt;= 10</span><sup><span style="font-size:15px">6</span></sup><br>
<span style="font-size:18px">1 &lt;= A[i] &lt;= 10<sup>6</sup></span></p>
</div>