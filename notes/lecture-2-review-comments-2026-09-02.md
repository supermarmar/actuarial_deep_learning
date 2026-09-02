# Credit lecture 2 review comments, 2 September 2026

Three comments were left as HTML comments inside the rendered
`credit_lectures/02_credit-edf-glm.html`. They are copied out here because a re-render
destroys them, per `notes/lecture-1-review-comments-2026-09-01.md` and the note in
`CLAUDE.md`. The same edit of the file also carries a whitespace reflow from an editor
formatter, which the render discards.

| # | Anchor in the HTML | Comment, verbatim |
|---|---|---|
| 1 | start of section 2, "Exponential dispersion family: a bit of theory" | `give a callout box here explaining what pdfs and cdfs and give their mathemtical formulas (discrete and continous)` |
| 2 | after the EDF density display, before the canonical-parameter paragraph | `place a callout box explaining what moments are and moment generating functions if i am not mistaken` |
| 3 | start of section 2.1, "The Bernoulli member" | `update teh notation based on lecture 1` |

## How each was addressed

1. A `callout-note` at the head of section 2 defining the probability mass function, the
   density and the distribution function in both the discrete and the continuous form,
   landing on the two objects lecture 1 already uses: the two-atom pmf of $D_i^{(k)}$ and
   the cdf of the time to default $T_i$ read at $k$, which **is** $\mathrm{PD}_k$. The
   survival function is named there so that lecture S1's hazard has somewhere to attach.
2. A `callout-note` after the EDF density defining raw and central moments, the moment
   generating function and the cumulant generating function, then deriving
   $K_Y(s) = (\kappa(\theta + s\varphi/v) - \kappa(\theta)) / (\varphi/v)$ and
   differentiating at $s = 0$ to recover the two moment formulas the lecture had asserted.
   The Bernoulli specialisation is $M_D(s) = 1 - \mu_k + \mu_k e^{s}$.
3. A notation sweep of the whole lecture rather than section 2.1 alone, so the document
   stays internally consistent: the response is $D_i^{(k)}$ with $k = 12$ months, the
   conditional mean is $\mu_k$ and the probability of default is $\mathrm{PD}_k$, exactly
   as lecture 1 fixes them. Borrower age keeps lecture 1's warning: it is a covariate,
   never the actuarial $x$.
