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
    # SECTION 4.1 - 4.4 (النظريات الأساسية)
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

    st.divider()

    # ============================================================
    # CASE STUDIES (INTERACTIVE)
    # ============================================================
    st.subheader("Interactive Mellin Case Explorer")

    def get_mellin_cases():
        cases = {}

        # Case 1: f(t) = e^{-t}
        cases["Case 1: f(t) = e^{-t}"] = {
            "title": "Case 1: f(t) = e^{-t}",
            "function": r"f(t) = e^{-t}",
            "series": r"e^{-t} = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} t^n",
            "coefficients": r"a_n = \frac{(-1)^n}{n!}",
            "rank": r"n",
            "plant_sum": [
                r"\mathcal{M}_T\{e^{-t}\}(\rho, s) = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} \frac{\Gamma(\rho + n)}{s^{\rho+n}}",
                r"= \Gamma(\rho) s^{-\rho} \sum_{n=0}^{\infty} \frac{(\rho)_n}{n!} \left(-\frac{1}{s}\right)^n",
                r"= \Gamma(\rho) s^{-\rho} \left(1 + \frac{1}{s}\right)^{-\rho}",
                r"= \frac{\Gamma(\rho)}{(s+1)^{\rho}}"
            ],
            "closed_form": r"\mathcal{M}_T\{e^{-t}\}(\rho, s) = \frac{\Gamma(\rho)}{(s+1)^{\rho}}",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{M}_T\{e^{-t}\}(\rho, s) = \Gamma(\rho)",
            "params": ["rho", "s"],
            "compute_result": lambda rho_val, s_val, **kwargs: math.gamma(rho_val) / ((s_val + 1)**rho_val) if rho_val > 0 and s_val > 0 else None,
        }

        # Case 2: f(t) = e^{-at}
        cases["Case 2: f(t) = e^{-at}"] = {
            "title": "Case 2: f(t) = e^{-at}",
            "function": r"f(t) = e^{-at}",
            "series": r"e^{-at} = \sum_{n=0}^{\infty} \frac{(-a)^n}{n!} t^n",
            "coefficients": r"a_n = \frac{(-a)^n}{n!}",
            "rank": r"n",
            "plant_sum": [
                r"\mathcal{M}_T\{e^{-at}\}(\rho, s) = \sum_{n=0}^{\infty} \frac{(-a)^n}{n!} \frac{\Gamma(\rho + n)}{s^{\rho+n}}",
                r"= \Gamma(\rho) s^{-\rho} \sum_{n=0}^{\infty} \frac{(\rho)_n}{n!} \left(-\frac{a}{s}\right)^n",
                r"= \Gamma(\rho) s^{-\rho} \left(1 + \frac{a}{s}\right)^{-\rho}",
                r"= \frac{\Gamma(\rho)}{(s+a)^{\rho}}"
            ],
            "closed_form": r"\mathcal{M}_T\{e^{-at}\}(\rho, s) = \frac{\Gamma(\rho)}{(s+a)^{\rho}}",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{M}_T\{e^{-at}\}(\rho, s) = a^{-\rho} \Gamma(\rho)",
            "params": ["rho", "s", "a"],
            "compute_result": lambda rho_val, s_val, a_val, **kwargs: math.gamma(rho_val) / ((s_val + a_val)**rho_val) if rho_val > 0 and s_val > 0 and a_val > 0 else None,
        }

        # Case 3: f(t) = e^{it} (مفصلة بالكامل كما في الصورة)
        cases["Case 3: f(t) = e^{it}"] = {
            "title": "Case 3: f(t) = e^{it}",
            "function": r"f(t) = e^{it}",
            "series": r"e^{it} = \sum_{n=0}^{\infty} \frac{i^n}{n!} t^n",
            "coefficients": r"a_n = \frac{i^n}{n!}",
            "rank": r"n",
            "plant_sum": [
                r"\text{Series planting law. Using the operator-based Mellin planting rule}",
                r"\mathcal{M}_T\{f\}(\rho, s) = \sum_{n \geq 0} a_n \frac{\Gamma(\rho + n)}{s^{\rho + n}}, \quad s > 0,",
                r"\text{and the Maclaurin series}",
                r"e^{it} = \sum_{n \geq 0} \frac{(it)^n}{n!} \implies a_n = \frac{i^n}{n!},",
                r"\text{we obtain}",
                r"\mathcal{M}_T\{e^{it}\}(\rho, s) = \sum_{n=0}^{\infty} \frac{i^n}{n!} \frac{\Gamma(\rho + n)}{s^{\rho+n}}",
                r"= \Gamma(\rho) s^{-\rho} \sum_{n=0}^{\infty} \frac{(\rho)_n}{n!} \left(\frac{i}{s}\right)^n.",
                r"\text{Using the binomial series } (1 - z)^{-\rho} = \sum_{n=0}^{\infty} \frac{(\rho)_n}{n!} z^n \text{ (for } |z| < 1, \text{ analytic continuation elsewhere), we get the closed form}",
                r"\mathcal{M}_T\{e^{it}\}(\rho, s) = \Gamma(\rho) s^{-\rho} \left(1 - \frac{i}{s}\right)^{-\rho} = \frac{\Gamma(\rho)}{(s - i)^{\rho}}, \quad s > 0.",
                r"\text{Polar form and real/imaginary parts. Write } s - i = re^{-i\theta} \text{ with}",
                r"r = \sqrt{s^2 + 1}, \quad \theta = \arctan\left(\frac{1}{s}\right), \quad (s > 0).",
                r"\text{Then}",
                r"\frac{1}{(s - i)^\rho} = r^{-\rho} e^{i\rho\theta},",
                r"\text{hence}",
                r"\mathcal{M}_T\{e^{it}\}(\rho, s) = \Gamma(\rho) r^{-\rho} e^{i\rho\theta} = \Gamma(\rho) r^{-\rho} \left[\cos(\rho\theta) + i \sin(\rho\theta)\right].",
                r"\text{Taking real/imag parts reproduces the operator Mellin entries for } \cos t \text{ and } \sin t:",
                r"\mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) r^{-\rho} \cos(\rho\theta), \quad \mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho) r^{-\rho} \sin(\rho\theta).",
                r"\text{Classical Mellin limit. Letting } s \to 0^+ \text{ gives } r \to 1 \text{ and } \theta \to \frac{\pi}{2}, \text{ so}",
                r"\lim_{s \to 0^+} \mathcal{M}_T\{e^{it}\}(\rho, s) = \Gamma(\rho) e^{i\rho\pi/2},",
                r"\text{and consequently}",
                r"\lim_{s \to 0^+} \mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) \cos\left(\frac{\pi\rho}{2}\right), \quad \lim_{s \to 0^+} \mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho) \sin\left(\frac{\pi\rho}{2}\right),",
                r"\text{which matches the classical Mellin tables (in the sense of analytic continuation).}"
            ],
            "closed_form": r"\mathcal{M}_T\{e^{it}\}(\rho, s) = \frac{\Gamma(\rho)}{(s - i)^{\rho}}",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{M}_T\{e^{it}\}(\rho, s) = \Gamma(\rho) e^{i\rho\pi/2}",
            "params": ["rho", "s"],
            "compute_result": lambda rho_val, s_val, **kwargs: math.gamma(rho_val) / ((s_val - 1j)**rho_val) if rho_val > 0 and s_val > 0 else None,
        }

        # Case 4: f(t) = cos(t)
        cases["Case 4: f(t) = cos(t)"] = {
            "title": "Case 4: f(t) = cos(t)",
            "function": r"f(t) = \cos t",
            "series": r"\cos t = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n}}{(2n)!}",
            "coefficients": r"a_{2n} = \frac{(-1)^n}{(2n)!}",
            "rank": r"2n",
            "plant_sum": [
                r"\mathcal{M}_T\{\cos t\}(\rho, s) = \sum_{n=0}^{\infty} (-1)^n \frac{\Gamma(\rho + 2n)}{(2n)!} \frac{1}{s^{\rho+2n}}",
                r"= \Gamma(\rho) s^{-\rho} {}_2F_1\left(\frac{\rho}{2}, \frac{\rho+1}{2}; \frac{1}{2}; -\frac{1}{s^2}\right)",
                r"= \Gamma(\rho) (s^2 + 1)^{-\rho/2} \cos\left(\rho \arctan\frac{1}{s}\right)"
            ],
            "closed_form": r"\mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) (s^2 + 1)^{-\rho/2} \cos\left(\rho \arctan\frac{1}{s}\right)",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{M}_T\{\cos t\}(\rho, s) = \Gamma(\rho) \cos\left(\frac{\pi\rho}{2}\right), \quad 0 < \rho < 1",
            "params": ["rho", "s"],
            "compute_result": lambda rho_val, s_val, **kwargs: math.gamma(rho_val) * ((s_val**2 + 1)**(-rho_val/2)) * math.cos(rho_val * math.atan(1/s_val)) if rho_val > 0 and s_val > 0 else None,
        }

        # Case 5: f(t) = sin(t)
        cases["Case 5: f(t) = sin(t)"] = {
            "title": "Case 5: f(t) = sin(t)",
            "function": r"f(t) = \sin t",
            "series": r"\sin t = \sum_{n=0}^{\infty} (-1)^n \frac{t^{2n+1}}{(2n+1)!}",
            "coefficients": r"a_{2n+1} = \frac{(-1)^n}{(2n+1)!}",
            "rank": r"2n+1",
            "plant_sum": [
                r"\mathcal{M}_T\{\sin t\}(\rho, s) = \sum_{n=0}^{\infty} (-1)^n \frac{\Gamma(\rho + 2n + 1)}{(2n+1)!} \frac{1}{s^{\rho+2n+1}}",
                r"= \Gamma(\rho + 1) s^{-(\rho+1)} {}_2F_1\left(\frac{\rho+1}{2}, \frac{\rho+2}{2}; \frac{3}{2}; -\frac{1}{s^2}\right)",
                r"= \Gamma(\rho) (s^2 + 1)^{-\rho/2} \sin\left(\rho \arctan\frac{1}{s}\right)"
            ],
            "closed_form": r"\mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho) (s^2 + 1)^{-\rho/2} \sin\left(\rho \arctan\frac{1}{s}\right)",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{M}_T\{\sin t\}(\rho, s) = \Gamma(\rho) \sin\left(\frac{\pi\rho}{2}\right), \quad 0 < \rho < 1",
            "params": ["rho", "s"],
            "compute_result": lambda rho_val, s_val, **kwargs: math.gamma(rho_val) * ((s_val**2 + 1)**(-rho_val/2)) * math.sin(rho_val * math.atan(1/s_val)) if rho_val > 0 and s_val > 0 else None,
        }

        # Case 6: t^m e^{-t} (Power Multiplication)
        cases["Case 6: t^m e^{-t} (Power Multiplication)"] = {
            "title": "Case 6: t^m e^{-t} (Power Multiplication)",
            "function": r"f(t) = t^m e^{-t}",
            "series": r"t^m e^{-t} = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} t^{n+m}",
            "coefficients": r"a_n = \frac{(-1)^n}{n!}",
            "rank": r"n+m",
            "plant_sum": [
                r"\mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} \frac{\Gamma(\rho + n + m)}{s^{\rho+n+m}}",
                r"= \frac{\Gamma(\rho + m)}{s^{\rho + m}} \sum_{n=0}^{\infty} \frac{(\rho + m)_n}{n!} \left(-\frac{1}{s}\right)^n",
                r"= \frac{\Gamma(\rho + m)}{s^{\rho + m}} \left(1 + \frac{1}{s}\right)^{-(\rho + m)}",
                r"= \frac{\Gamma(\rho + m)}{(s + 1)^{\rho + m}}"
            ],
            "closed_form": r"\mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \frac{\Gamma(\rho + m)}{(s + 1)^{\rho + m}}",
            "classical_limit": r"\lim_{s \to 0^+} \mathcal{MT}_{(\rho,s)}\{t^m e^{-t}\} = \Gamma(\rho + m)",
            "params": ["rho", "s", "m"],
            "compute_result": lambda rho_val, s_val, m_val, **kwargs: math.gamma(rho_val + m_val) / ((s_val + 1)**(rho_val + m_val)) if rho_val > 0 and s_val > 0 and m_val >= 0 else None,
        }

        return cases

    cases = get_mellin_cases()
    selected_case = st.selectbox(
        "Choose a symbolic Mellin case",
        list(cases.keys()),
        index=0,
        key="mellin_detailed_case",
    )

    case = cases[selected_case]

    st.subheader(case["title"])

    st.markdown("**Function**")
    st.latex(case["function"])

    st.markdown("**Series**")
    st.latex(case["series"])

    st.markdown("**Coefficients**")
    st.latex(case["coefficients"])

    st.markdown("**Rank**")
    st.latex(case["rank"])

    st.markdown("**Plant & Sum**")
    for step in case["plant_sum"]:
        st.latex(step)

    st.markdown("**Closed Regulated Form**")
    st.latex(case["closed_form"])

    st.markdown("**Classical Mellin Limit**")
    st.latex(case["classical_limit"])

    # ============================================================
    # PARAMETER INPUTS AND NUMERICAL EVALUATION
    # ============================================================
    st.markdown("---")
    st.subheader("Numerical Evaluation")

    params = case.get("params", [])

    if "rho" in params:
        rho_val = st.number_input(
            "Enter value for $\\rho$ (Mellin parameter)",
            value=0.5,
            step=0.1,
            format="%.2f",
            key=f"rho_{selected_case[:10]}"
        )
    else:
        rho_val = None

    if "s" in params:
        s_val = st.number_input(
            "Enter value for $s$ (regulator)",
            value=1.0,
            step=0.1,
            format="%.2f",
            key=f"s_mellin_{selected_case[:10]}"
        )
    else:
        s_val = None

    if "a" in params:
        a_val = st.number_input(
            "Enter value for $a$",
            value=1.0,
            step=0.1,
            format="%.2f",
            key=f"a_mellin_{selected_case[:10]}"
        )
    else:
        a_val = None

    if "m" in params:
        m_val = st.number_input(
            "Enter value for $m$ (integer)",
            value=0,
            step=1,
            format="%d",
            key=f"m_mellin_{selected_case[:10]}"
        )
    else:
        m_val = None

    # Compute result
    if case.get("compute_result"):
        try:
            result = case["compute_result"](
                rho_val=rho_val if rho_val is not None else 0.5,
                s_val=s_val if s_val is not None else 1.0,
                a_val=a_val if a_val is not None else 1.0,
                m_val=m_val if m_val is not None else 0,
            )
            if result is not None:
                if isinstance(result, complex):
                    st.success(f"**Numerical Result:** $\\mathcal{{M}}_T\\{{f\\}}({rho_val if rho_val else 0.5}, {s_val if s_val else 1.0})$ = {result.real:.6f} + {result.imag:.6f}i")
                else:
                    st.success(f"**Numerical Result:** $\\mathcal{{M}}_T\\{{f\\}}({rho_val if rho_val else 0.5}, {s_val if s_val else 1.0})$ = {result:.6f}")
            else:
                st.warning("The entered values do not satisfy the convergence conditions.")
        except Exception as e:
            st.error(f"Error computing result: {e}")

    st.divider()

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
