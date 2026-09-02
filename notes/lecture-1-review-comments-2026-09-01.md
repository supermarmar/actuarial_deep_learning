# Credit lecture 1: review comments, 1 September 2026

Left by Mario as HTML comments in `credit_lectures/01_credit-use-case.html`,
preserved here before the file was re-rendered. The HTML is generated, so
comments placed in it do not survive a render; the `.qmd` is the durable place.

1. Can we define T_i by using the notation set above that Botha et al define in terms of a default outcome y_t and then tie it with the g_i as the orginination date or whatever best links it to section 2.5

2. Can we pick a different symbol other than {\cal L}_k since that gets used in future lectures and then can you define what the fucntion \left| {\cal L}_k \right| since it seems to be counting it just looks an abs function on a set of elements?

3. Lets drop this one since I think age of borrower is not really a thing in credit risk. I think what I would rather do is adjust the paragraph below to make the t_p_x function analogous to a "the probability of a loan aged t (the substitue for x) defaulting in k months (the sub for the t) - challenge me on this since gi and t are linked to date of birth and age. so the formula for credit risk could be k_p_t. This would mean that your dataset - you then need to drop the condition above where 0<t<k since t can be larger than k in any given dataset before censoring - challenge me on this"

4. Adjust this paragraph as per my comment above

5. Why is g and not g_i used?

6. might need some adjustment but challenge me if needed

7. Lets move this after the next section since this a lot to inrtoduce at once


## Round 2, 1 September 2026

Five further comments, again left as HTML comments in the rendered file and copied
here before re-rendering. Verbatim, including typos.

1. (after the time-axes table in 2.5) happy with the worded explanation but cna you
   write out below in statisical notation using the random variables and proper
   actuarial noation using l_k+t and l_t where survival here means not defaulting.
   this also assumes we are working with loans that have never defaulted

2. (end of 2.5, after the `ReportAsOfEOD` paragraph) can you generate a table using
   the data set showing a few row examples of these variables you defined above. let
   me know if this does not make sense

3. (head of 2.6) Is that n = 148k the n(12) we determined above? if so lets name it

4. (before the mu_k display in 2.6) Define this E[] in TTD as you have it and leave a
   note that this in the survival analysis world and then define it in terms of Di as
   you have it in the PiT And TTC example.

5. (before the "Reading a conditional expectation" callout) I actually want the
   mathematical explanation of the function E[Y|X]

### How each was answered

1. Added the callout "The same statement in life-table notation" after the paragraph
   fixing $t$'s role. It carries $l_t$, the two decrements and ${}_k p_t = l_{k+t}/l_t$,
   and states plainly that reading it as *default* survival needs settlement treated as
   censoring, which is S2's subject. Bondora loans leave two ways, so
   $l_{k+t}/l_t$ is a multiple-decrement probability unless that assumption is made.
   The decrement counts are written $d^{\rm def}_t$ and $d^{\rm set}_t$, never bare
   $d_t$, because $d$ is already Botha's delinquency threshold in 2.1.
2. Added a code cell at the end of 2.5 selecting five real loans by a deterministic
   filter, one per censoring pattern. Columns are `LoanNumber`, $g_i$, $A_i$, $T_i$,
   $D^{(12)}_i$ and membership of ${\cal W}_{12}$. Dropped $\tau$ and $u$ as columns:
   $\tau$ is one constant across the extract and $u = g_i + t$ is an identity, so both
   are stated in the prose instead.
3. Yes. 2.6 now opens on $n(12) = 148{,}733$ and $i \in {\cal W}_{12}$, and abbreviates
   $n = n(12)$ for the rest of the lecture.
4. Reordered: the time-to-default form first, flagged as the survival-analysis
   statement, then the indicator form matching the PiT and TTC callout, with
   $D^{(k)}_i = \mathbf{1}\{T_i \le k\}$ named as the bridge between them.
5. Added "The conditional expectation, formally" before the reading callout: the
   cell-wise sum, the $L^2$ minimiser, and the tower property named as the balance
   property of lecture 7.
