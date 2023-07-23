# Immediate Smaller Element
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer array <strong>Arr</strong> of size <strong>N</strong>. For each element in the array, check whether the right adjacent element (on the&nbsp;next&nbsp;immediate position) of the array is smaller. If next element is smaller, update the current index to that element.&nbsp;If not, then&nbsp;&nbsp;<strong>-1</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 5
Arr[] = {4, 2, 1, 5, 3}
<strong>Output:</strong>
2 1 -1 3 -1
<strong>Explanation:</strong> Array elements are 4, 2, 1, 5
3. Next to 4 is 2 which is smaller, so we
print 2. Next of 2 is 1 which is smaller,
so we print 1. Next of 1 is 5 which is
greater, so we print -1. Next of 5 is 3
which is smaller, so we print 3.&nbsp; Note
that for last element, output is always 
going to be -1 because there is no element
on right.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
Arr[] = {5, 6, 2, 3, 1,&nbsp;7}
<strong>Output:</strong>
-1 2 -1 1 -1 -1
<strong>Explanation: </strong>Next to 5 is 6 which is
greater, so we print -1.Next of 6 is 2
which is smaller, so we print 2. Next
of 2 is 3 which is greater, so we
print -1. Next of 3 is 1 which is
smaller, so we print 1. Next of 1 is
7 which is greater, so we print -1.
Note that for last element, output is
always going to be -1 because there is
no element on right.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>immediateSmaller()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers&nbsp;<strong>arr&nbsp;</strong>and&nbsp;<strong>n</strong><strong>&nbsp;</strong>as parameters. You need to change the array itself.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>7</sup><br>
1 ≤ Arr[i] ≤ 10<sup>5</sup></span></p>

<p>&nbsp;</p>
</div>