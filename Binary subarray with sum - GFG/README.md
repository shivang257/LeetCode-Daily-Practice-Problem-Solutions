# Binary subarray with sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a binary array <strong>arr </strong>of size <strong>N</strong>&nbsp;and an integer <strong>target</strong>, return the number of non-empty <strong>subarrays</strong> with a sum equal to target.</span></p>

<p><br>
<span style="font-size:18px">Note : A <strong>subarray</strong> is the contiguous part of the array.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 5<br>
target = 2<br>
arr[ ] = {1, 0, 1, 0, 1}<br>
<strong>Output:</strong> 4<br>
<strong>Explanation</strong>: The 4 subarrays are:<br>
{1, 0, 1, _, _}<br>
{1, 0, 1, 0, _}<br>
{_, 0, 1, 0, 1}<br>
{_, _, 1, 0, 1}</span><br>
&nbsp;</div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 5<br>
target = 5<br>
arr[ ] = {1, 1, 0, 1, 1}<br>
<strong>Output:</strong> 0<br>
<strong>Explanation</strong>: There is no subarray with sum equal to target.</span></div>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>numberOfSubarrays()&nbsp;</strong>which takes the array <strong>arr</strong>, interger <strong>N</strong> and an integer <strong>target</strong> as input and returns the number of subarrays with a sum equal to target.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N&nbsp;≤ 10<sup>5</sup><br>
1 ≤ target&nbsp;≤ N</span></p>
</div>