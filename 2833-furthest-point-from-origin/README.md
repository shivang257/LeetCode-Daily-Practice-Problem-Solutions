<h2><a href="https://leetcode.com/problems/furthest-point-from-origin/">2833. Furthest Point From Origin</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code>moves</code> of length <code>n</code> consisting only of characters <code>'L'</code>, <code>'R'</code>, and <code>'_'</code>. The string represents your movement on a number line starting from the origin <code>0</code>.</p>

<p>In the <code>i<sup>th</sup></code> move, you can choose one of the following directions:</p>

<ul>
	<li>move to the left if <code>moves[i] = 'L'</code> or <code>moves[i] = '_'</code></li>
	<li>move to the right if <code>moves[i] = 'R'</code> or <code>moves[i] = '_'</code></li>
</ul>

<p>Return <em>the <strong>distance from the origin</strong> of the <strong>furthest</strong> point you can get to after </em><code>n</code><em> moves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> moves = "L_RL__R"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> moves = "_R__LL_"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> moves = "_______"
<strong>Output:</strong> 7
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length == n &lt;= 50</code></li>
	<li><code>moves</code> consists only of characters <code>'L'</code>, <code>'R'</code> and <code>'_'</code>.</li>
</ul>
</div>