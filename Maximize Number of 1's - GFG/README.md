# Maximize Number of 1's
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a binary array <strong>arr</strong> of size <strong>N</strong> and an integer <strong>M</strong>. Find the maximum number of <strong>consecutive 1's</strong> produced by flipping at most <strong>M 0's</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3
arr[] = {1, 0, 1}
M = 1
<strong>Output:</strong>
3
<strong>Explanation:</strong>
Maximum subarray is of size 3
which can be made subarray of all 1 after
flipping one zero to 1.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 11
arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
M = 2
<strong>Output:</strong>
8
<strong>Explanation:</strong>
Maximum subarray is of size 8
which can be made subarray of all 1 after
flipping two zeros to 1.
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Complete the function <strong>findZeroes()</strong>&nbsp;which takes&nbsp;array&nbsp;<strong>arr&nbsp;</strong>and two integers&nbsp;<strong>n, m</strong>,&nbsp;as input parameters&nbsp;and <strong>returns</strong> an integer denoting the answer. </span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>7</sup><br>
0 &lt;= M &lt;= N<br>
0 &lt;= arr<sub>i</sub> &lt;= 1</span></p>
</div>