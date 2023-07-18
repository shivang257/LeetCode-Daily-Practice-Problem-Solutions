# Longest Repeating Character Replacement
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string <strong>S </strong>and an integer <strong>K</strong>. In <strong>one operation</strong>, you are allowed to choose any character of the string and change it to any other uppercase English character.You can perform this operation <strong>atmost</strong> K&nbsp;times.<br>
Return the length of the <strong>longest substring</strong> containing same letter you can get after performing the above operations.<br>
<strong>Note</strong> : S consists of only uppercase English letters.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<div style="--darkreader-inline-bgcolor:#222426; --darkreader-inline-bgimage:initial; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-top:#3e4446; background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><span style="font-size:18px"><strong>Input : </strong><br>
S = "ABBA"<br>
K = 2<br>
<strong>Output:</strong>&nbsp;4<br>
<strong>Explanation: </strong>Replace the 2 occurrences&nbsp;of 'A' with 2 'B's&nbsp;or vice-versa.</span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="--darkreader-inline-bgcolor:#222426; --darkreader-inline-bgimage:initial; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-top:#3e4446; background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><span style="font-size:18px"><strong>Input :</strong><br>
S = "AABAABB"<br>
k = 2<br>
<strong>Output:</strong>&nbsp;6<br>
<strong>Explanation: </strong>Replace the occurrence&nbsp;of 'B' with 'A' and form "AAAAAAB".<br>
The substring "AAAAAA" has the most extended repeating letters, which is 6.</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your task :</strong></span></p>

<p><span style="font-size:18px">You don't have to read input or print anything. Your task is to complete the function <strong>characterReplacement()&nbsp;</strong>which takes the string <strong>S </strong>and integer <strong>K</strong>&nbsp;as input and returns the longest substring containing same letter after performing specified operations.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity : </strong>(|S|)</span></p>

<p><span style="font-size:18px"><strong>Expected Auxiliary Space : </strong>O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints :</strong></span></p>

<p><span style="font-size:18px">1 &lt;= |S|&nbsp;&lt;= 10<sup>5</sup></span></p>
</div>