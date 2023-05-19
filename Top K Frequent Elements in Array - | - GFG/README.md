# Top K Frequent Elements in Array - |
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a non-empty array of integers, find the top k&nbsp;elements which have the highest frequency in the array. If two numbers have the same frequency then the larger number should be given preference.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Print the elements according to the frequency count (from highest to lowest) and if the frequency is equal then larger number will be given preference.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 6
nums = {1,1,1,2,2,3}
k = 2
<strong>Output: </strong>{1, 2}</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 8
nums = {1,1,2,2,3,3,3,4}
k = 2
<strong>Output: </strong>{3, 2}<strong>
Explanation: </strong>Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 &gt; 1.</span></pre>

<p><span style="font-size:18px"><strong>User Task:</strong><br>
The task is to complete the function <strong>topK()</strong> that takes the array and integer k&nbsp;as input and returns a list of top k&nbsp;frequent elements.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong> : O(NlogN)<br>
<strong>Expected Auxilliary Space</strong> : O(N)</span></p>

<p><span style="font-size:18px"><strong>Constraints: </strong></span><br>
<span style="font-size:18px">1 &lt;= N &lt;= 10<sup>5</sup><br>
1&lt;=A[i]&lt;=10<sup>5</sup></span></p>
</div>