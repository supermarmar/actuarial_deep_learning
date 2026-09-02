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

## Round 3, 2 September 2026

Three comments, all inside the point-in-time and through-the-cycle callout in 2.6.
Verbatim, including typos.

1. Can you write a mathematical notation to say what the PiT PD formula can be
   represented by. can you also write a formula for a TTC PD which i imagine is some
   average of default rates but I could be wrong so challenge me

2. Can you also explain what a hybrid model could look like in a formula terms

3. update the terms of this formula ever so slightly to be consistent with above e.g.
   nt' and the identity function coudl be some D(k) of sorts also update the D_t so
   with a k so we know what we are talking about in terms of the window

### How each was answered

1. The callout now carries a PiT display conditioning on a macro state
   $\boldsymbol{Z}_u$ rather than on the calendar month itself, since a future $u$
   carries no data, and two TTC displays. On the challenge: the instinct is right, and
   the one-factor probit construction makes it exactly right, because
   $\mathbb{E}_Z[\Phi((\Phi^{-1}(p) - \sqrt{\rho} Z)/\sqrt{1-\rho})] = p$ identically.
   Where it fails is the practitioner's shortcut of feeding average macro conditions
   into a fitted logistic PiT model, which Jensen's inequality rules out. The
   regulatory TTC is the other display: an average of observed one-year default rates,
   which is the same $\mathrm{DR}^{(12)}_u$ series the PiT model regresses.
2. Two hybrid representations. A convex combination on the logit scale with a weight
   $\lambda$, and the Vasicek one-factor form with a loading $\rho$, whose $\rho = 0$
   and $\rho \to 1$ ends are TTC and fully cyclical. The IRB capital formula is the
   same expression at the 99.9th percentile of the factor, which is the tie a credit
   audience already knows.
3. Renotated. The calendar axis moves from the paper's $t$ to the lecture's $u$, which
   matters more than the missing $k$: $t$ is months on book everywhere else in this
   lecture. The indicator becomes the loan-level $D^{(k)}_{i,t}$, the window-start
   generalisation of 2.4's flag, since a maximum of 0/1 flags is that indicator. The
   performing set becomes ${\cal P}_u$ with size $n_u$, and the portfolio series
   becomes $\mathrm{DR}^{(k)}_u$: written $\mathrm{DR}$ rather than $D$ because the
   loan-level $D^{(k)}_{i,t}$ is now in the same display. The paper's own symbols
   ($D_t$, ${\cal S}_P(t)$, $n'_t$) are named in the prose so the source stays
   findable.

## Round 3, 2 September 2026

Four further comments, left as HTML comments in the rendered file and copied here
before re-rendering. Verbatim, including typos. The first three ask for **new
lectures** rather than edits to lecture 1, so each has a plan of its own under
`notes/plans/`; the fourth is a figure change to lecture 1 itself.

1. (head of the PiT and TTC callout, `01_credit-use-case.qmd:679`) This section is
   getting quite large I think it might need it as its own lecture given the
   complexity expands in a IFRS 9 space. Lets plan out a lecture where we look to
   build that up from this lecture and the notation is aligned to what you have, what
   I want you to touch on is concepts like conditional PiT PDs, unconditional PiT PDs,
   FiT (Forward in Time) which is when you incorporating macro economic information.
   Do some deep research perhaps to find papers that speak about this and refernce
   many of the Botha papers that go into different methods of estimating such PiT PDs
   (markov chains, regressions, survival models etc) and the pros and cons of eahc

2. (head of the hybrid PD callout, `01_credit-use-case.qmd:778`) For this section I
   think this will become an IRB lecture which I think I have done some good work on
   in my guides repo in the wiki and lecture folder so read through that to get the
   structure and story and we can plan this out as well and create a second plan to
   run in another Claude session. It can be briefly mentioned here

3. (head of section 3.1 "Covariates interact", `01_credit-use-case.qmd:993`) The
   interactions and covariates and causation stuff I would like to do some deep
   research into the medical stats field to see how they deal with this - add to vault
   and plan this out as your 3rd plan this will be a seperate lecture or more

4. (on the kernel-smoothed default-rate figure, `01_credit-use-case.qmd:1037`) can we
   also show this as a 3d graph together with the 2d ggraph

### How each was answered

1. **Answered on 2 September 2026.** The lecture is
   `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`, on a new regulatory track prefixed `R`,
   and lecture 1's callout is cut to 43 per cent of its length with a forward reference in
   place of the material that moved. It opens by separating the two axes the comment asked
   about, and the separation is corroborated rather than asserted: the guides' own
   `03_notation.md` defines conditional and unconditional PiT PDs by the conditioning event
   $D_{i,t}(p) = 0$, so the axis is survival, while PiT against TTC is the macro axis. FiT is
   adopted as the course's label with its provenance stated plainly, since the term appears
   in neither IFRS 9 nor the literature, and the standard's own "forward-looking information"
   leads. The guides define a FiT PD twice in incompatible ways, and the lecture takes the
   probit form, with the multiplicative FLI factor named as the shortcut it is; `R2` must
   answer the same way. Eleven methods are reviewed, each with a cost as well as a benefit,
   covering all three Botha papers plus Bellotti and Crook, Belkin and Breeden, and two
   reserving techniques an actuarial audience already owns. Finally the point-in-time claim
   is demonstrated on Bondora rather than asserted, and the demonstration is more useful
   than a clean one would have been: the pooled fit over three markets returns economically
   backwards signs at overwhelming significance, because the Finnish and Spanish books
   expanded through a period of falling unemployment, and Estonia alone gives GDP growth at
   -0.083 and inflation at +0.093 with a twelve-month PD swinging 9.1 percentage points on
   the macro state. Research and notation contract in `notes/ifrs9-pit-pd-research.md`.
2. Planned, not implemented. See `notes/plans/02-irb-capital-lecture.md`.
3. Planned, not implemented. See `notes/plans/03-causal-inference-lecture.md`.
4. **Answered on 2 September 2026.** Treated as a small change to lecture 1 rather than a
   plan, and mirrored into the `.qmd` at the figure so it survives the next render. The
   figure is now two panels, a heatmap beside a `plot_surface` view, and the guard against
   the obvious failure is that both are drawn from the one smoothed `rate` array on one
   `Normalize(0.1, 0.5)` under one colourbar, so the surface cannot disagree with the map.
   Three details were easy to get wrong. The surface takes bin **centres** rather than
   edges, since `linspace(18, 76, 59)` and `linspace(5.5, 9.0, 71)` give 58 and 70 bins and
   `rate` is therefore `(58, 70)`, which `np.meshgrid(..., indexing="ij")` matches without a
   silent transpose. The `cnt_s > 8` NaN mask is kept on both panels, because the white
   space is the honest part of the figure. And the `elev=28, azim=-125` view was chosen over
   matplotlib's default `-58`, which throws the z-axis furniture into the colourbar; the
   z-axis label is dropped for the same reason, the colourbar already naming the quantity.
   The prose beside the figure now argues the interaction the surface makes visible: the age
   profile is pronounced at high incomes and close to flat at low ones, so no tilted plane
   reproduces it. A first draft of that sentence placed the ridge on the low-income edge,
   which the rendered figure contradicts, and it was corrected against the render rather
   than against expectation.
