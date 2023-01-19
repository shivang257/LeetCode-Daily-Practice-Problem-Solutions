# Disarrangement of balls
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given N balls numbered from 1 to N and there are N baskets numbered from 1 to N in front of you, the i<sup>th</sup> basket is meant for the i<sup>th</sup> ball. Calculate the number of ways in which <strong>no</strong>&nbsp;ball&nbsp;goes into its&nbsp;respective basket.</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> The balls are numbered 1 and 2. 
Then there is only one way to dearrange them. 
The (number-basket) pairs will be [(1-2),(2-1)].</span></pre>

<p><br>
<strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The (number-basket) pairs are 
[(1-3),(2-1),(3-2)] and [(1-2),(2-3),(3-2)].</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>disarrange() </strong>, which takes the number N as input parameter and returns the number of ways to disarrange them. As the number can be very big return it modulo <strong>10<sup>9</sup> + 7</strong></span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space: </strong>O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>4</sup></span></p>
</div>