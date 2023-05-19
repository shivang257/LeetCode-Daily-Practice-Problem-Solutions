# Frequencies of Limited Range Array Elements
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array A[] of N&nbsp;positive integers which can contain integers from 1&nbsp;to P&nbsp;where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1&nbsp;to N.</span><br>
<span style="font-size:18px"><strong>Note:</strong> The elements greater than N&nbsp;in the array can be ignored for counting and <strong>do&nbsp;modify the&nbsp;array</strong>&nbsp;<strong>in-place.</strong></span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
<strong>Output:
</strong>0 2 2 0 1<strong>
Explanation: </strong>
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 4
arr[] = {3,3,3,3}
P = 3
<strong>Output:
</strong>0 0 4 0<strong>
Explanation: 
</strong>Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything.&nbsp;</span><span style="font-size:18px">Complete the function <strong>frequencycount() </strong>that takes the array and n&nbsp;as input parameters and <strong>modify the&nbsp;array</strong> <strong>itself</strong> in place to denote the frequency count of each element from 1 to N. i,e&nbsp;element at index 0 should represent the frequency of 1, and so on.</span></p>

<p><br>
<span style="font-size:18px">Can you solve this problem without using extra space (O(1) Space)?</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N&nbsp;≤ 10<sup>5</sup><br>
1 ≤ P&nbsp;≤ 4*10<sup>4</sup><sup>&nbsp;</sup><br>
1 &lt;= A[i] &lt;= P</span></p>
</div>