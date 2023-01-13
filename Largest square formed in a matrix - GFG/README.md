# Largest square formed in a matrix
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a binary matrix <strong>mat</strong>&nbsp;of size <strong>n</strong> * <strong>m</strong>, find out the maximum size square sub-matrix with all 1s.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 2, m = 2
mat = {{1, 1}, 
&nbsp;      {1, 1}}
<strong>Output:</strong> 2
<strong>Explaination:</strong> The maximum size of the square
sub-matrix is 2. The matrix itself is the 
maximum sized sub-matrix in this case.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 2, m = 2
mat = {{0, 0}, 
&nbsp;      {0, 0}}
<strong>Output:</strong> 0
<strong>Explaination:</strong> There is no 1 in the matrix.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>maxSquare()</strong> which takes n, m and mat as input parameters and returns the size of the maximum square sub-matrix of given matrix.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n*m)<br>
<strong>Expected Auxiliary Space:</strong> O(n*m)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n, m ≤ 50<br>
0 ≤ mat[i][j] ≤ 1&nbsp;</span></p>
</div>