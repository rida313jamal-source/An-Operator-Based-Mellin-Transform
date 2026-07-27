import streamlit as st
import sympy as sp
import numpy as np
import math

def render_mellin_section():
    # ============================================================
    # HEADER & INTRODUCTION
    # ============================================================
    st.header("4 part III : An Operator-Based Mellin Transform")

    st.markdown("""
    We introduce an *operator version* of the Mellin transform built by *planting Maclaurin coefficients* inside a gamma-weighted integral kernel. The resulting framework reproduces the classical Mellin table directly from a planted series, demonstrating that the operator viewpoint can be both unifying and computationally efficient.
    """)

    st.subheader("Mellin Operator Transform")

    st.latex(r"""
    t^n \mapsto (-\partial_s)^{n+\rho-1} \frac{1}{s} = \frac{\Gamma(n+\rho)}{s^{n+\rho}}.
    """)

    # ============================================================
    # SECTION 4.1
    # ============================================================
    st.header("4.1 Differential Derivation of the Mellin Integral Form (Planting Method)")

    st.markdown("### 1. Differential Planting Foundation")

    st.markdown(r"""
    Let $f(x)$ be an analytic function expanded as a Maclaurin series:
    """)
    st.latex(r"f(t) = \sum_{n=0}^\infty a_n t^n.")

    st.markdown(r"""
    The Mellin-transform is defined in its *differential planting form* by
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \sum_{n=0}^\infty a_n (-\partial_s)^{\rho+n-1} \left( \frac{1}{s} \right), \quad s > 0.
    """)

    st.markdown(r"""
    Each term $a_n t^n$ of the series is "planted" as a fractional derivative of order $(\rho+n-1)$ applied to the seed function $1/s$.
    """)

    st.markdown("### 4.2 Fractional Derivative Identity")

    st.markdown(r"""
    For $\Re(\alpha) > -1$, the fractional derivative of $1/s$ satisfies
    """)
    st.latex(r"""
    (-\partial_s)^{\alpha} \left( \frac{1}{s} \right) = \frac{\Gamma(\alpha+1)}{s^{\alpha+1}}.
    """)

    st.markdown(r"""
    Substituting $\alpha = \rho+n-1$ gives
    """)
    st.latex(r"""
    (-\partial_s)^{\rho+n-1} \left( \frac{1}{s} \right) = \frac{\Gamma(\rho+n)}{s^{\rho+n}}.
    """)

    st.markdown(r"""
    Hence the differential planting law becomes
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \sum_{n=0}^\infty a_n \frac{\Gamma(\rho+n)}{s^{\rho+n}}.
    """)

    st.markdown("### 3. Transition to the Integral Representation")

    st.markdown(r"""
    Using the Gamma integral identity
    """)
    st.latex(r"""
    \frac{\Gamma(\rho+n)}{s^{\rho+n}} = \int_0^\infty t^{\rho+n-1} e^{-st} \, dt, \quad s > 0,
    """)

    st.markdown(r"""
    we substitute this into the planted series:
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \sum_{n=0}^\infty a_n \int_0^\infty t^{\rho+n-1} e^{-st} \, dt.
    """)

    st.markdown("### 4. Interchanging Sum and Integral")

    st.markdown(r"""
    Under absolute convergence (for standard analytic functions), the sum and the integral may be interchanged (Tonelli–Fubini theorem):
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \int_0^\infty \left( \sum_{n=0}^\infty a_n t^n \right) t^{\rho-1} e^{-st} dt.
    """)

    st.markdown(r"""
    Recognizing the internal series as $f(t)$ yields the canonical integral form:
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \int_0^\infty f(t) t^{\rho-1} e^{-st} dt.
    """)

    st.markdown("### 5. Classical Mellin Limit")

    st.markdown(r"""
    Taking the limit as $s \to 0^+$ removes the exponential regulator:
    """)
    st.latex(r"""
    \lim_{s \to 0^+} MT\{f\}(\rho, s) = \int_0^\infty f(t) t^{\rho-1} dt,
    """)

    st.markdown(r"""
    which is precisely the classical Mellin transform.

    Perfect agreement between the planted differential form and the classical integral form confirms the internal consistency.
    """)

    st.markdown("### 7. Interpretation")

    st.markdown(r"""
    This derivation shows that the Mellin integral form is not a primitive definition, but a natural consequence of the differential planting law. The exponential regulator $e^{-st}$ emerges automatically from the internal structure of the fractional derivative of $1/s$. Thus, the differential approach reconstructs the Mellin transform entirely from planted derivative dynamics, bridging the discrete hierarchy of derivatives with the continuous integral hierarchy governed by the Gamma function.

    **Additional note.** The exponential regulator $e^{-st}$ appearing in the integral form of the Mellin operator is not an externally added convergence factor, but rather an *intrinsic byproduct* of the differential planting sequence. This shows that the exponential damping in Mellin's transform can be *reconstructed endogenously* from the internal structure of the fractional derivatives acting on $1/s$.
    """)

    # ============================================================
    # SECTION 4.3
    # ============================================================
    st.header("4.3 Integral form")

    st.markdown(r"""
    The classical Mellin transform is defined as
    """)
    st.latex(r"""
    M\{f(t)\}(\rho) = \int_0^\infty f(t) t^{\rho-1} dt,
    """)
    st.markdown(r"valid whenever the integral converges.")

    st.markdown(r"""
    In the operator framework, we introduce an exponential regulator:
    """)
    st.latex(r"""
    MT\{f(t)\}(\rho, s) = \int_0^\infty f(t) t^{\rho-1} e^{-st} dt, \quad s > 0.
    """)

    # ============================================================
    # SECTION 4.4
    # ============================================================
    st.header("4.4 Series form (planting law)")

    st.markdown(r"""
    If $f(t)$ has a Maclaurin expansion
    """)
    st.latex(r"f(t) = \sum_{n=0}^\infty a_n t^n,")

    st.markdown(r"""
    then the transform is obtained by planting each term:
    """)
    st.latex(r"""
    MT\{f\}(\rho, s) = \sum_{n=0}^\infty a_n \frac{\Gamma(\rho + n)}{s^{\rho+n}}.
    """)

    st.markdown(r"""
    This is the *series planting law*: each $t^n$ contributes a gamma factor $\Gamma(\rho + n)$ and a regulator $s^{-(\rho+n)}$.
    """)

    # ============================================================
    # SECTION 4.5: Exponential e^{-t}
    # ============================================================
    st.header("4.5 Exponential Function f(t) = e^{-t}")

    st.markdown(r"""
    Series expansion:
    """)
    st.latex(r"e^{-t} = \sum_{n=0}^\infty \frac{(-1)^n}{n!} t^n, \quad \text{rank } n:")

    st.markdown("### Worked Example: Recovering $\Gamma(\rho)$ from $e^{-t}$")

    st.markdown(r"""
    We want to compute the planted Mellin transform of the exponential function:
    """)
    st.latex(r"""
    \mathcal{M}_T\{e^{-t}\}(\rho, s) = \sum_{n=0}^\infty \frac{(-1)^n}{n!} \frac{\Gamma(\rho + n)}{s^{\rho+n}}, \quad s > 0.
    """)

    st.markdown("#### Step 1: Factor out $\Gamma(\rho)$")

    st.markdown(r"""
    Using the rising factorial (Pochhammer symbol),
    """)
    st.latex(r"""
    \Gamma(\rho + n) = \Gamma(\rho) (\rho)_n, \quad (\rho)_n := \frac{\Gamma(\rho + n)}{\Gamma(\rho)},
    """)
    st.markdown(r"we obtain")
    st.latex(r"""
    \mathcal{M}_T\{e^{-t}\}(\rho, s) = \Gamma(\rho) s^{-\rho} \sum_{n=0}^\infty \frac{(\rho)_n}{n!} \left(-\frac{1}{s}\right)^n.
    """)

    st.markdown("#### Step 2: Recognize the binomial expansion")

    st.markdown(r"""
    Recall the binomial expansion for arbitrary $\rho$:
    """)
    st.latex(r"""
    (1 + z)^{-\rho} = \sum_{n=0}^\infty \frac{(\rho)_n}{n!} (-z)^n, \quad (|z| < 1, \text{ analytic continuation elsewhere}).
    """)

    st.markdown(r"""
    Setting $z = \frac{1}{s}$ gives
    """)
    st.latex(r"""
    \sum_{n=0}^\infty \frac{(\rho)_n}{n!} \left(-\frac{1}{s}\right)^n = \left(1 + \frac{1}{s}\right)^{-\rho}.
    """)

    st.markdown("#### Step 3: Final simplification")

    st.markdown(r"""
    Thus,
    """)
    st.latex(r"""
    \mathcal{M}_T\{e^{-t}\}(\rho, s) = \Gamma(\rho) s^{-\rho} \left(1 + \frac{1}{s}\right)^{-\rho} = \frac{\Gamma(\rho)}{(s+1)^{\rho}}.
    """)

    st.markdown("### Step 4: Recovering the classical Mellin transform")

    st.markdown(r"""
    Taking the limit $s \to 0^+$ removes the regulator:
    """)
    st.latex(r"""
    \lim_{s \to 0^+} \mathcal{M}_T\{e^{-t}\}(\rho, s) = \Gamma(\rho).
    """)

    st.markdown(r"""
    This exactly matches the classical Mellin transform:
    """)
    st.latex(r"""
    \int_0^\infty e^{-t} t^{\rho-1} dt = \Gamma(\rho).
    """)

    # ============================================================
    # SECTION 4.6: Exponential e^{-at}
    # ============================================================
    st.header("4.6 Exponential Function f(t) = e^{-at}")

    st.markdown(r"""
    Consider the function
    """)
    st.latex(r"f(t) = e^{-at}, \quad a > 0.")

    st.markdown(r"""
    Using the power series expansion,
    """)
    st.latex(r"e^{-at} = \sum_{n=0}^\infty \frac{(-a)^n t^n}{n!}.")

    st.markdown(r"""
    Applying the generated kernel rule,
    """)
    st.latex(r"t^n \mapsto \frac{\Gamma(\rho + n)}{s^{\rho + n}},")

    st.markdown(r"we obtain")
    st.latex(r"""
    M_T\{e^{-at}\} = \sum_{n=0}^\infty \frac{(-a)^n \Gamma(\rho + n)}{n!} \frac{1}{s^{\rho + n}}.
    """)

    st.markdown(r"""
    Factoring out the common terms,
    """)
    st.latex(r"""
    M_T\{e^{-at}\} = \frac{\Gamma(\rho)}{s^\rho} \sum_{n=0}^\infty \frac{(\rho)_n}{n!} \left(-\frac{a}{s}\right)^n.
    """)

    st.markdown(r"""
    Using the binomial expansion,
    """)
    st.latex(r"""
    \sum_{n=0}^\infty \frac{(\rho)_n}{n!} z^n = (1 - z)^{-\rho},
    """)

    st.markdown(r"""
    with $z = -\frac{a}{s}$, we obtain
    """)
    st.latex(r"""
    M_T\{e^{-at}\} = \frac{\Gamma(\rho)}{s^\rho} \left(1 + \frac{a}{s}\right)^{-\rho}.
    """)

    st.markdown(r"""
    Therefore,
    """)
    st.latex(r"""
    M_T\{e^{-at}\} = \frac{\Gamma(\rho)}{(s + a)^{\rho}}.
    """)

    st.markdown(r"""
    Finally, taking the Mellin limit $s \to 0^+$ we recover the classical Mellin transform,
    """)
    st.latex(r"""
    M_T\{e^{-at}\}(\rho, s) = a^{-\rho} \Gamma(\rho).
    """)

    st.latex(r"""
    M_T\{e^{-at}\}(\rho, s) = a^{-\rho} \frac{\Gamma(\rho)}{(s + a)^{\rho}}.
    """)

    # ============================================================
    # SECTION 4.7: Exponential e^{it}
    # ============================================================
    st.header("4.7 Case: f(t) = e^{it}")

    st.markdown("**Series planting law.**")

    st.markdown(r"""
    Using the operator-based Mellin planting rule
    """)
    st.latex(r"""
    M_T\{f\}(\rho, s) = \sum_{n \geq 0} a_n \frac{\Gamma(\rho + n)}{s^{\rho + n}}, \quad s > 0,
    """)

    st.markdown(r"""
    and the Maclaurin series
    """)
    st.latex(r"""
    e^{it} = \sum_{n \geq 0} \frac{(it)^n}{n!} \implies a_n = \frac{i^n}{n!},
    """)

    st.markdown(r"we obtain")
    st.latex(r"""
    M_T\{e^{it}\}(\rho, s) = \sum_{n \geq 0} \frac{i^n}{n!} \frac{\Gamma(\rho + n)}{s^{\rho + n}} = \Gamma(\rho) s^{-\rho} \sum_{n \geq 0} \frac{(\rho)_n}{n!} \left(\frac{i}{s}\right)^n.
    """)

    st.markdown(r"""
    Using the binomial series $(1 - z)^{-\rho} = \sum_{n \geq 0} \frac{(\rho)_n}{n!} z^n$ (for $|z| < 1$, analytic continuation elsewhere), we get the closed form
    """)
    st.latex(r"""
    M_T\{e^{it}\}(\rho, s) = \Gamma(\rho) s^{-\rho} \left(1 - \frac{i}{s}\right)^{-\rho} = \frac{\Gamma(\rho)}{(s - i)^\rho}, \quad s > 0.
    """)

    st.markdown("**Polar form and real/imaginary parts.**")

    st.markdown(r"""
    Write $s - i = re^{-i\theta}$ with
    """)
    st.latex(r"""
    r = \sqrt{s^2 + 1}, \quad \theta = \arctan\left(\frac{1}{s}\right), \quad (s > 0).
    """)

    st.markdown(r"""
    Then
    """)
    st.latex(r"""
    \frac{1}{(s - i)^\rho} = r^{-\rho} e^{i\rho\theta},
    """)

    st.markdown(r"hence")
    st.latex(r"""
    M_T\{e^{it}\}(\rho, s) = \Gamma(\rho) r^{-\rho} e^{i\rho\theta} = \Gamma(\rho) r^{-\rho} \left[\cos(\rho\theta) + i \sin(\rho\theta)\right].
    """)

    st.markdown(r"""
    Taking real/imag parts reproduces the operator Mellin entries for $\cos t$ and $\sin t$:
    """)
    st.latex(r"""
    M_T\{\cos t\}(\rho, s) = \Gamma(\rho) r^{-\rho} \cos(\rho\theta), \quad M_T\{\sin t\}(\rho, s) = \Gamma(\rho) r^{-\rho} \sin(\rho\theta).
    """)

    st.markdown("**Classical Mellin limit.**")

    st.markdown(r"""
    Letting $s \to 0^+$ gives $r \to 1$ and $\theta \to \frac{\pi}{2}$, so
    """)
    st.latex(r"""
    \lim_{s \to 0^+} M_T\{e^{it}\}(\rho, s) = \Gamma(\rho) e^{i\rho\pi/2},
    """)

    st.markdown(r"and consequently")
    st.latex(r"""
    \lim_{s \to 0^+} M_T\{\cos t\}(\rho, s) = \Gamma(\rho) \cos\left(\frac{\pi\rho}{2}\right), \quad \lim_{s \to 0^+} M_T\{\sin t\}(\rho, s) = \Gamma(\rho) \sin\left(\frac{\pi\rho}{2}\right),
    """)

    st.markdown(r"""
    which matches the classical Mellin tables (in the sense of analytic continuation).
    """)

    st.markdown("**Integral cross-check.**")

    st.markdown(r"""
    Directly from the regulated Mellin integral,
    """)
    st.latex(r"""
    M_T\{e^{it}\}(\rho, s) = \int_0^\infty x^{\rho - 1} e^{-st} e^{it} dt = \int_0^\infty x^{\rho - 1} e^{-(s - i)t} dt = \frac{\Gamma(\rho)}{(s - i)^\rho},
    """)

    st.markdown(r"which agrees with the planted result.")

    # ============================================================
    # SECTION 4.8: Cosine
    # ============================================================
    st.header("4.8 Cosine Function f(t) = cos t")

    st.markdown("**1. Series expansion.**")
    st.latex(r"""
    \cos t = \sum_{n=0}^\infty (-1)^n \frac{t^{2n}}{(2n)!}, \quad \text{rank}: 2n
    """)

    st.markdown("**2. Planting.**")
    st.latex(r"""
    \mathcal{M}_T\{\cos t\}(\rho, s) = \sum_{n=0}^\infty (-1)^n \frac{\Gamma(\rho + 2n)}{(2n)!} \frac{1}{s^{\rho+2n}}.
    """)

    st.markdown("**3. Hypergeometric form.**")
    st.markdown(r"""
    Using duplication,
    """)
    st.latex(r"""
    \Gamma(\rho + 2n) = \Gamma(\rho) 2^{2n} \left( \frac{\rho}{2} \right)_n \left( \frac{\rho+1}{2} \right)_n, \quad (2n)! = 2^{2n} \left( \frac{1}{2} \right)_n n!,
    """)

    st.markdown(r"we obtain")
    st.latex(r"""
    \mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) s^{-\rho} {}_2F_1\left(\frac{\rho}{2}, \frac{\rho+1}{2}; \frac{1}{2}; -\frac{1}{s^2}\right).
    """)

    st.markdown("**4. Closed form.**")
    st.markdown(r"Equivalently,")
    st.latex(r"""
    \mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) (s^2 + 1)^{-\rho/2} \cos\left(\rho \arctan\frac{1}{s}\right).
    """)

    st.markdown("**5. Classical Mellin.**")
    st.markdown(r"Taking $s \to 0^+$:")
    st.latex(r"""
    \int_0^\infty t^{\rho-1} \cos t \, dt = \Gamma(\rho) \cos\left(\frac{\pi\rho}{2}\right), \quad 0 < \Re(\rho) < 1.
    """)

    # ============================================================
    # SECTION 4.9: Sine
    # ============================================================
    st.header("4.9 Sine Function f(t) = sin t")

    st.markdown("**1. Series expansion.**")
    st.latex(r"""
    \sin t = \sum_{n=0}^\infty (-1)^n \frac{t^{2n+1}}{(2n+1)!}, \quad \text{rank}: 2n+1
    """)

    st.markdown("**2. Planting.**")
    st.latex(r"""
    \mathcal{M}_T\{\sin t\}(\rho, s) = \sum_{n=0}^\infty (-1)^n \frac{\Gamma(\rho + 2n + 1)}{(2n + 1)!} \frac{1}{s^{\rho + 2n + 1}}.
    """)

    st.markdown("**3. Hypergeometric form.**")
    st.markdown(r"""
    Using duplication,
    """)
    st.latex(r"""
    \Gamma(\rho + 2n + 1) = \Gamma(\rho + 1) 2^{2n} \left( \frac{\rho+1}{2} \right)_n \left( \frac{\rho+2}{2} \right)_n, \quad (2n + 1)! = 2^{2n} \left( \frac{3}{2} \right)_n n!,
    """)

    st.markdown(r"so")
    st.latex(r"""
    \mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho + 1) s^{-(\rho+1)} {}_2F_1\left(\frac{\rho+1}{2}, \frac{\rho+2}{2}; \frac{3}{2}; -\frac{1}{s^2}\right).
    """)

    st.markdown("**4. Closed form.**")
    st.markdown(r"Equivalently,")
    st.latex(r"""
    \mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho) (s^2 + 1)^{-\rho/2} \sin\left(\rho \arctan\frac{1}{s}\right).
    """)

    st.markdown("**5. Classical Mellin.**")
    st.markdown(r"Taking $s \to 0^+$:")
    st.latex(r"""
    \int_0^\infty t^{\rho-1} \sin t \, dt = \Gamma(\rho) \sin\left(\frac{\pi\rho}{2}\right), \quad 0 < \Re(\rho) < 1.
    """)

    # ============================================================
    # SECTION 4.10: Power Multiplication Property
    # ============================================================
    st.header("4.10 Power Multiplication Property in the Generated Kernel Method")

    st.markdown(r"""
    Let the function be represented by its power series expansion
    """)
    st.latex(r"f(t) = \sum_{n=0}^\infty a_n t^n.")

    st.markdown(r"""
    Multiplication by a power $t^m$ gives
    """)
    st.latex(r"t^m f(t) = \sum_{n=0}^\infty a_n t^{n+m}.")

    st.markdown(r"""
    According to the generated kernel rule,
    """)
    st.latex(r"t^k \to \frac{\Gamma(\rho + k)}{s^{\rho+k}},")

    st.markdown(r"""
    where $k$ represents the power of $t$. Therefore, for the shifted power $n+m$,
    """)
    st.latex(r"""
    t^{n+m} \to \frac{\Gamma(\rho + n + m)}{s^{\rho+n+m}}.
    """)

    st.markdown(r"""
    Hence, the multiplication property generated from the series method is
    """)
    st.latex(r"""
    \mathcal{MT}_{(\rho,s)}\{t^m f(t)\} = \sum_{n=0}^\infty a_n \frac{\Gamma(\rho + n + m)}{s^{\rho+n+m}}.
    """)

    st.markdown(r"""
    This property shows that multiplication by $t^m$ produces a shift in the Gamma index and the power of the kernel variable $s$.
    """)

    st.markdown("#### Example")

    st.markdown(r"""
    For
    """)
    st.latex(r"f(t) = e^{-t} = \sum_{n=0}^\infty \frac{(-1)^n}{n!} t^n,")

    st.markdown(r"we have")
    st.latex(r"""
    t^m e^{-t} = \sum_{n=0}^\infty \frac{(-1)^n}{n!} t^{n+m}.
    """)

    st.markdown(r"""
    Applying the generated kernel rule gives
    """)
    st.latex(r"""
    \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \sum_{n=0}^\infty \frac{(-1)^n}{n!} \frac{\Gamma(\rho + n + m)}{s^{\rho+n+m}}.
    """)

    st.markdown(r"""
    Using the Gamma recurrence relation in terms of the Pochhammer symbol,
    """)
    st.latex(r"""
    \Gamma(\rho + m + n) = \Gamma(\rho + m)(\rho + m)_n,
    """)

    st.markdown(r"we obtain")
    st.latex(r"""
    \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \frac{\Gamma(\rho + m)}{s^{\rho + m}} \sum_{n=0}^{\infty} \frac{(\rho + m)_n}{n!} \left(-\frac{1}{s}\right)^n.
    """)

    st.markdown(r"""
    Using the binomial series identity,
    """)
    st.latex(r"""
    (1 - z)^{-a} = \sum_{n=0}^{\infty} \frac{(a)_n}{n!} z^n,
    """)

    st.markdown(r"""
    with $a = \rho + m, \quad z = -\frac{1}{s}$, the summation becomes
    """)
    st.latex(r"""
    \sum_{n=0}^{\infty} \frac{(\rho + m)_n}{n!} \left(-\frac{1}{s}\right)^n = \left(1 + \frac{1}{s}\right)^{-(\rho + m)}.
    """)

    st.markdown(r"""
    Therefore,
    """)
    st.latex(r"""
    \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \frac{\Gamma(\rho + m)}{s^{\rho + m}} \left(\frac{s + 1}{s}\right)^{-(\rho + m)}.
    """)

    st.markdown(r"""
    Simplifying the powers of $s$, we obtain
    """)
    st.latex(r"""
    \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \frac{\Gamma(\rho + m)}{(s + 1)^{\rho + m}}.
    """)

    st.markdown(r"""
    Taking the limit as $s \to 0^+$, we obtain
    """)
    st.latex(r"""
    \lim_{s \to 0^+} \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \lim_{s \to 0^+} \frac{\Gamma(\rho + m)}{(s + 1)^{\rho + m}} = \Gamma(\rho + m).
    """)

    st.markdown(r"""
    which agrees with the classical Mellin transform result
    """)
    st.latex(r"""
    \int_0^{\infty} t^{\rho + m - 1} e^{-t} dt = \Gamma(\rho + m).
    """)

    st.markdown(r"""
    Hence, the generated kernel method recovers the classical Mellin transform for the power-exponential function.
    """)

    st.markdown("**Remark on the Applicability of the Generated Kernel Method**")

    st.markdown(r"""
    The generated kernel method is most direct for functions whose series expansions lead to convergent transformed series and explicit Gamma reductions.

    For some functions, the generated series may be asymptotic or require special-function representations. In such cases, recovering the classical closed form may involve analytic continuation or additional summability techniques.

    Thus, the method provides the generated representation, while the final evaluation depends on the analytical properties of the resulting series. Like
    """)
    st.latex(r"f(t) = (1 + t)^{-a}")
    st.latex(r"f(t) = e^{-t^2}")

    # ============================================================
    # TABLE 2
    # ============================================================
    st.header("Table 2: Comparison Table: Expanded Series, Planted Operator Form, and Classical Mellin Results")

    st.markdown("""
    | Function $f(t)$ | Series Expansion | Planted Operator Form | Classical Mellin Result |
    |---|---|---|---|
    | $e^{-t}$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n t^n}{n!}$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n \\Gamma(\\rho + n)}{n!} s^{\\rho + n}$ | $\\Gamma(\\rho), \\ \\rho > 0$ |
    | $e^{-at}$ | $\\sum_{n=0}^{\\infty} \\frac{(-a)^n t^n}{n!}$ | $\\sum_{n=0}^{\\infty} \\frac{(-a)^n \\Gamma(\\rho + n)}{n!} s^{\\rho + n}$ | $a^{-\\rho} \\Gamma(\\rho), \\ a > 0, \\ \\rho > 0$ |
    | $\\cos(t)$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n t^{2n}}{(2n)!}$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n \\Gamma(\\rho + 2n)}{(2n)!} s^{\\rho + 2n}$ | $\\Gamma(\\rho) \\cos\\left(\\frac{\\pi \\rho}{2}\\right), \\ 0 < \\rho < 1$ |
    | $\\sin(t)$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n t^{2n+1}}{(2n+1)!}$ | $\\sum_{n=0}^{\\infty} \\frac{(-1)^n \\Gamma(\\rho + 2n+1)}{(2n+1)!} s^{\\rho + 2n+1}$ | $\\Gamma(\\rho) \\sin\\left(\\frac{\\pi \\rho}{2}\\right), \\ 0 < \\rho < 1$ |
    | $t^m f(t)$ | $\\sum_{n=0}^{\\infty} a_n t^n = \\sum_{n=0}^{\\infty} a_n t^{n+m}$ | $\\sum_{n=0}^{\\infty} a_n \\frac{\\Gamma(\\rho + n + m)}{s^{\\rho + n + m}}$ | $M\\{t^m f(t)\\}(\\rho) = F(\\rho + m)$ |
    """)

    # ============================================================
    # SECTION 5: Fractional derivative link
    # ============================================================
    st.header("5 Fractional derivative link")

    st.markdown(r"""
    We note the key operator identity:
    """)
    st.latex(r"""
    (-\partial_s)^n \left(\frac{1}{s}\right) = \frac{n!}{s^{n+1}}.
    """)

    st.markdown(r"""
    Fractional calculus extends this to arbitrary $\alpha$:
    """)
    st.latex(r"""
    (-\partial_s)^\alpha \left(\frac{1}{s}\right) = \frac{\Gamma(\alpha + 1)}{s^{\alpha + 1}}, \ \Re(\alpha) > -1.
    """)

    st.markdown("### 5.1 Key implication")

    st.markdown(r"""
    By setting $\alpha = n + \rho - 1$, we obtain
    """)
    st.latex(r"""
    (-\partial_s)^{n+\rho-1} \left(\frac{1}{s}\right) = \frac{\Gamma(n + \rho)}{s^{n+s}}.
    """)

    st.markdown(r"""
    This is exactly the Mellin planting law.

    ### Summary: Unified Operator Planting
    """)

    # ============================================================
    # TABLE 3
    # ============================================================
    st.header("Table 3: Unified operator planting framework for Laplace, Fourier, Mellin, and Hankel transforms")

    st.markdown("""
    | Transform | Rank $\\alpha$ | Operator planting form |
    |---|---|---|
    | Laplace | $\\alpha = n$ | $(-\\partial_s)^\\alpha \\left( \\frac{1}{s} \\right) = \\frac{\\Gamma(\\alpha + 1)}{s^{\\alpha+1}}$ |
    | Fourier | $\\alpha = n$ | $(-\\partial_s)^\\alpha \\left( \\frac{1}{s} \\right) + (\\partial_s)^\\alpha \\left( \\frac{1}{\\bar{s}} \\right) = \\Gamma(\\alpha + 1) \\left( \\frac{1}{s^{\\alpha+1}} + \\frac{(-1)^\\alpha}{\\bar{s}^{\\alpha+1}} \\right)$ |
    | Mellin | $\\alpha = n + \\rho - 1$ | $(-\\partial_s)^\\alpha \\left( \\frac{1}{s} \\right) = \\frac{\\Gamma(n + \\rho)}{s^{n+\\rho}}$ |
    | Hankel | $\\alpha = n + \\nu$ | $(-\\partial_s)^\\alpha \\left( \\frac{1}{s} \\right) = \\frac{\\Gamma(n + \\nu + 1)}{s^{n+\\nu+1}}$ |
    """)

    st.markdown(r"""
    **Laplace planting.** This corresponds to an integer planting rank $\alpha = n$, acting on the kernel $1/s$, yielding
    """)
    st.latex(r"""
    (-\partial_s)^\alpha \left( \frac{1}{s} \right) = \frac{\Gamma(\alpha + 1)}{s^{\alpha+1}}.
    """)

    st.markdown(r"""
    **Fourier planting.** This appears as the bilateral extension of the Laplace framework, encoded through the conjugate pair $(s, \bar{s})$ with $s = \sigma + i\omega$. The planting rank remains integer, $\alpha = n$, acting simultaneously on both kernels $(\sigma + i\omega)^{-1}$ and $(\sigma - i\omega)^{-1}$.
    """)
    st.latex(r"""
    (-\partial_s)^\alpha \left( \frac{1}{s} \right) + (\partial_s)^\alpha \left( \frac{1}{\bar{s}} \right) = \Gamma(\alpha + 1) \left( \frac{1}{s^{\alpha+1}} + \frac{(-1)^\alpha}{\bar{s}^{\alpha+1}} \right)
    """)

    st.markdown(r"""
    **Mellin planting.** This extends the planting rank to fractional and complex values, $\alpha = n + \rho - 1$, acting on the kernel $1/s$, which produces
    """)
    st.latex(r"""
    (-\partial_s)^\alpha \left( \frac{1}{s} \right) = \frac{\Gamma(n + \rho)}{s^{n+\rho}}.
    """)

    st.markdown(r"""
    **Hankel planting.** This introduces a radial shift governed by the Bessel order $\nu$, with planting rank $\alpha = n + \nu$, again acting on the kernel $1/s$.
    """)

if __name__ == "__main__":
    render_mellin_section()
