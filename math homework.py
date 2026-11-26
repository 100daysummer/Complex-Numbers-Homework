import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import math
    import marimo as mo
    from wigglystuff import ObservablePlot, TangleLatex
    from fractions import Fraction

    return Fraction, TangleLatex, math, mo


@app.cell(hide_code=True)
def _():
    people_names = [
        "Александър Котев",
        "Александър Тошев",
        "Александър Бакърджиев",
        "Антон",
        "Боримир",
        "Борислав",
        "Бранимир",
        "Велин",
        "Виктория",
        "Георги",
        "Гергана",
        "Димитър",
        "Ивет",
        "Йоана",
        "Калина",
        "Константин",
        "Кристиан Маникатов",
        "Кристиян Гигов",
        "Кристиян Петров",
        "Крум",
        "Максим",
        "Магдалена",
        "Мая",
        "Момчил",
        "Никола Полименов",
        "Никола Николов",
        "София",
        "Яна"
    ]

    people_dates = [
        29,
        10,
        27,
        23,
        17,
        20,
        25,
        12,
        10,
        13,
        20,
        10,
        5,
        26,
        18,
        30,
        26,
        13,
        27,
        23,
        17,
        17,
        4,
        8,
        13,
        11,
        17,
        26
    ]
    return people_dates, people_names


@app.cell(hide_code=True)
def _(mo, people_names):
    person_dropdown = mo.ui.dropdown(options= people_names, value = "Борислав");
    return (person_dropdown,)


# @app.cell(hide_code=True)
# def _(mo, people_dates, people_names, person_dropdown):
#     # 0-indexed!!
#     person_index = people_names.index(person_dropdown.value)
#     HW_A = (person_index + 1) % 10 + 1
#     HW_B = people_dates[person_index] % 10 + 1
#     mo.vstack(
#         [
#             person_dropdown,
#             mo.md(
#                 rf"""
#                 Ти си {person_dropdown.value}. Номерът ти в класа е {person_index+1}, a денят ти на раждане е {people_dates[person_index]}. Съответно **a** = {HW_A} и **b** = {HW_B}
#                 """
#             )
#         ]   
#     )
#     return HW_A, HW_B

@app.cell(hide_code=True)
def _(mo, people_dates, people_names, person_dropdown):
    # 0-indexed!!
    person_index = people_names.index(person_dropdown.value)

    HW_A_default = (person_index + 1) % 10 + 1
    HW_B_default = people_dates[person_index] % 10 + 1

    override_checkbox = mo.ui.checkbox(
        value=False,
        label="Ръчно задаване на a и b",
    )

    HW_A_slider = mo.ui.slider(
        start=1, stop=10, step=1,
        value=HW_A_default,
        label="a",
        show_value=True,
    )

    HW_B_slider = mo.ui.slider(
        start=1, stop=10, step=1,
        value=HW_B_default,
        label="b",
        show_value=True,
    )

    mo.vstack([
        person_dropdown,
        override_checkbox,
        HW_A_slider,
        HW_B_slider,
    ])

    return (
        HW_A_default,
        HW_B_default,
        HW_A_slider,
        HW_B_slider,
        override_checkbox,
        person_index,
    )

@app.cell(hide_code=True)
def _(
    mo,
    people_dates,
    person_dropdown,
    person_index,
    HW_A_default,
    HW_B_default,
    HW_A_slider,
    HW_B_slider,
    override_checkbox,
):
    if override_checkbox.value:
        HW_A = int(HW_A_slider.value)
        HW_B = int(HW_B_slider.value)
    else:
        HW_A = HW_A_default
        HW_B = HW_B_default

    mo.md(
        rf"""
        Ти си {person_dropdown.value}. Номерът ти в класа е
        {person_index + 1}, а денят ти на раждане е
        {people_dates[person_index]}.

        Съответно **a** = {HW_A} и **b** = {HW_B}.
        """
    )

    return HW_A, HW_B

@app.cell(hide_code=True)
def _(Fraction):
    def as_fraction(value):
        return Fraction(str(value)).limit_denominator(1000)

    def tex_fraction(value):
        value = Fraction(value)
        sign = "-" if value < 0 else ""
        value = abs(value)

        if value.denominator == 1:
            return sign + str(value.numerator)

        return rf"{sign}\frac{{{value.numerator}}}{{{value.denominator}}}"

    return as_fraction, tex_fraction


@app.cell(hide_code=True)
def _():
    #problem_1_a = mo.ui.anywidget(
    #    Latex(
    #        latex=r"(5 - i)(4 + 2i)",
    #    )
    #)
    return


@app.cell(hide_code=True)
def _(HW_B, TangleLatex, mo):
    problem_1_b = mo.ui.anywidget(
        TangleLatex(
            latex=r"\frac{\tangle{b} \cdot i}{\sqrt{2} - i}+2 = \\[1em] = \frac{\tangle{b} \cdot i}{\sqrt2 - i} \cdot \frac{\sqrt2 + i}{\sqrt 2 + i} + 2 = \\[1em] = \frac{\sqrt2 \cdot \tangle{b} \cdot i + \tangle{b} \cdot i \cdot i}{2 - i^2} + 2= \\[1em] = \frac{ - \tangle{b} + \sqrt2 \cdot \tangle{b} \cdot i}{3} + 2 = \\[1em] = \frac{6 -\tangle{b} + \sqrt 2 \cdot \tangle{b} \cdot i}{3} =",
            parameters={
                "b" : {"value": HW_B, "symbol": "b", "max_value": 10, "min_value": 1},
    #            "B" : {"value": HW_B}
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_1_b,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 1
    Представете в алгебричен вид
    """)
    return


@app.cell(hide_code=True)
def _(Fraction, mo, problem_1_b, tex_fraction):
    def _():
        b = Fraction(str(problem_1_b.value["values"]["b"])).limit_denominator(1000)

        real_part = (6 - b) / 3
        imag_part = b / 3

        real_tex = tex_fraction(real_part)

        if imag_part == 0:
            result_tex = real_tex
        else:
            sign = "+" if imag_part > 0 else "-"
            coefficient = abs(imag_part)
            coefficient_tex = "" if coefficient == 1 else tex_fraction(coefficient)

            result_tex = rf"{real_tex} {sign} {coefficient_tex}\sqrt{{2}}\,i"

        problem_1_b_answer = mo.md(
            rf"""
            \[
            = {result_tex}
            \]
            """
        )
        return mo.vstack([problem_1_b, problem_1_b_answer])


    _()
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_1_d = mo.ui.anywidget(
        TangleLatex(
            latex=r"2e^{i\frac{\tangle{a}\pi}{6}} = 2\left(\cos\frac{\tangle{a}\pi}{6}+i\sin\frac{\tangle{a}\pi}{6}\right) =",
            parameters={
                "a": {"value": HW_A, "symbol": "a", "max_value": 10, "min_value": 1, "color": "red"},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_1_d,)


@app.cell(hide_code=True)
def _(Fraction, math, mo, problem_1_d):
    def _():
        def _():
            a = Fraction(str(problem_1_d.value["values"]["a"])).limit_denominator(1000)

            exact_answers = {
                1: r"\sqrt{3}+i",
                2: r"1+\sqrt{3}i",
                3: r"2i",
                4: r"-1+\sqrt{3}i",
                5: r"-\sqrt{3}+i",
                6: r"-2",
                7: r"-\sqrt{3}-i",
                8: r"-1-\sqrt{3}i",
                9: r"-2i",
                10: r"1-\sqrt{3}i",
            }

            if a.denominator == 1 and 1 <= a <= 10:
                result_tex = exact_answers[int(a)]
            else:
                angle = math.pi * float(a) / 6
                real = 2 * math.cos(angle)
                imag = 2 * math.sin(angle)

                def decimal_tex(value):
                    return "0" if abs(value) < 1e-10 else f"{abs(value):.6g}"

                if abs(real) < 1e-10:
                    result_tex = f"{decimal_tex(imag)}i"
                    if imag < 0:
                        result_tex = "-" + result_tex
                elif abs(imag) < 1e-10:
                    result_tex = f"{real:.6g}"
                else:
                    sign = "+" if imag > 0 else "-"
                    result_tex = rf"{real:.6g} {sign} {decimal_tex(imag)}i"

            problem_1_d_answer = mo.md(rf"\[= {result_tex}\]")
            return mo.vstack([problem_1_d, problem_1_d_answer])
        return _()


    _()
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_2_a = mo.ui.anywidget(
        TangleLatex(
            latex=r"r=\sqrt{\tangle{a}^2+(-\tangle{a})^2}=\tangle{a}\sqrt{2}\\[1em] \cos\varphi=\frac{1}{\sqrt{2}},\quad \sin\varphi=-\frac{1}{\sqrt{2}},\quad \varphi=\frac{7\pi}{4}\\[1em] \tangle{a}-\tangle{a}i=\tangle{a}\sqrt{2}\left(\cos\frac{7\pi}{4}+i\sin\frac{7\pi}{4}\right)",
            parameters={
                "a": {"value": HW_A, "symbol": "a", "max_value": 10, "min_value": 1, "color": "red"},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_2_a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 2
    Представете в тригонометричен вид. в) и г)
    """)
    return


@app.cell(hide_code=True)
def _(as_fraction, mo, problem_2_a, tex_fraction):
    def _():
        a = as_fraction(problem_2_a.value["values"]["a"])
        a_tex = tex_fraction(a)

        problem_2_a_answer = mo.md(
            rf"""
            \[
            = {a_tex}\sqrt{{2}}\left(\cos\frac{{7\pi}}{{4}}+i\sin\frac{{7\pi}}{{4}}\right)
            \]
            """
        )
        return mo.vstack([problem_2_a, problem_2_a_answer])


    _()
    return


@app.cell(hide_code=True)
def _(HW_B, TangleLatex, mo):
    problem_2_b = mo.ui.anywidget(
        TangleLatex(
            latex=r"e^{\ln{\tangle{b}}+i\frac{\pi}{6}} = e^{\ln{\tangle{b}}}\cdot e^{i\frac{\pi}{6}} = \\[1em] = \tangle{b}\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)",
            parameters={
                "b": {"value": HW_B, "symbol": "b", "max_value": 10, "min_value": 1},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_2_b,)


@app.cell(hide_code=True)
def _(as_fraction, mo, problem_2_b, tex_fraction):
    def _():
        b = as_fraction(problem_2_b.value["values"]["b"])
        b_tex = tex_fraction(b)

        problem_2_b_answer = mo.md(
            rf"""
            \[
            = {b_tex}\left(\cos\frac{{\pi}}{{6}}+i\sin\frac{{\pi}}{{6}}\right)
            \]
            """
        )
        return mo.vstack([problem_2_b, problem_2_b_answer])


    _()
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_3_b = mo.ui.anywidget(
        TangleLatex(
            latex=r"r=\sqrt{\tangle{a}^2+(\sqrt{3}\cdot\tangle{a})^2}=2\cdot\tangle{a}\\[1em] \cos\varphi=\frac{1}{2},\quad \sin\varphi=\frac{\sqrt{3}}{2},\quad \varphi=\frac{\pi}{3}\\[1em] \tangle{a}+\sqrt{3}\cdot\tangle{a}\cdot i=2\cdot\tangle{a}\cdot e^{i\frac{\pi}{3}}",
            parameters={
                "a": {"value": HW_A, "symbol": "a", "max_value": 10, "min_value": 1, "color":"red"},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_3_b,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 3
    Представете в ойлерова форма, б) и в)
    """)
    return


@app.cell(hide_code=True)
def _(as_fraction, mo, problem_3_b, tex_fraction):
    def _():
        a = as_fraction(problem_3_b.value["values"]["a"])
        a_tex = tex_fraction(a)

        problem_3_b_answer = mo.md(
            rf"""
            \[
            = 2\cdot {a_tex}\,e^{{i\frac{{\pi}}{{3}}}}
            \]
            """
        )
        return mo.vstack([problem_3_b, problem_3_b_answer])


    _()
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_3_a = mo.ui.anywidget(
        TangleLatex(
            latex=r"\cos{\tangle{a}}-i\sin{\tangle{a}} = \cos(-\tangle{a})+i\sin(-\tangle{a}) = e^{-i\cdot\tangle{a}}",
            parameters={
                "a": {"value": HW_A, "symbol": "a", "max_value": 10, "min_value": 1, "color": "red"},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_3_a,)


@app.cell(hide_code=True)
def _(as_fraction, mo, problem_3_a, tex_fraction):
    a = as_fraction(problem_3_a.value["values"]["a"])
    a_tex = tex_fraction(a)

    problem_3_a_answer = mo.md(
        rf"""
        \[
        = e^{{-i{a_tex}}}
        \]
        """
    )

    mo.vstack([problem_3_a, problem_3_a_answer])
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_4_a = mo.ui.anywidget(
        TangleLatex(
            latex=r"""
            (x+i)(\tangle{a}-iy)=1+13i
            \\[0.5em]
            (\tangle{a}x+y)+i(\tangle{a}-xy)=1+13i
            \\[0.5em]
            \left|
                \begin{aligned}
                    \tangle{a}x+y&=1\\
                    \tangle{a}-xy&=13
                \end{aligned}
            \right.
            \\[1em]
            \left|
                \begin{aligned}
                    y=1-\tangle{a}x \\[1em]
                    x(1-\tangle{a}x)=\tangle{a}-13
                \end{aligned}
            \right.
            \\[1em]
            \tangle{a}x^2-x+\tangle{a}-13=0
            \\[1em]
            D=1-4\cdot\tangle{a}(\tangle{a}-13)
            =1+52\cdot\tangle{a}-4\cdot\tangle{a}^2
            \\[1em]
            x_{1,2}=\frac{1\pm\sqrt{D}}{2\cdot\tangle{a}}
            """
            ,
            parameters={
                "a": {"value": HW_A, "symbol": "a", "max_value": 10, "min_value": 1, "color": "red"},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_4_a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 4
    Решете уравнението, а) и б)
    """)
    return


@app.cell(hide_code=True, expand_output=True)
def _(Fraction, as_fraction, math, mo, problem_4_a, tex_fraction):
    def _():
        a = as_fraction(problem_4_a.value["values"]["a"])
        d = 1 + 52 * a - 4 * a * a

        if a == 0:
            raise ValueError("a cannot be zero")
        if d < 0:
            raise ValueError("The discriminant must be non-negative")

        # Check whether sqrt(d) is rational.
        nr = math.isqrt(d.numerator)
        dr = math.isqrt(d.denominator)

        is_rational_root = (
            nr**2 == d.numerator
            and dr**2 == d.denominator
        )

        if is_rational_root:
            root = Fraction(nr, dr)

            x1 = (1 + root) / (2 * a)
            y1 = (1 - root) / 2
            x2 = (1 - root) / (2 * a)
            y2 = (1 + root) / 2

            answer = mo.md(rf"""
            \[
            (x,y)=
            \left({tex_fraction(x1)}, {tex_fraction(y1)}\right)
            \quad\text{{или}}\quad
            \left({tex_fraction(x2)}, {tex_fraction(y2)}\right)
            \]
            """)

        else:
            # Keep the irrational square root, but simplify its coefficient.
            d_root = rf"\sqrt{{{tex_fraction(d)}}}"

            def scaled_binomial(sign, coefficient):
                coefficient = Fraction(coefficient)
                expression = rf"\left(1 {sign} {d_root}\right)"

                if coefficient == 1:
                    return expression
                if coefficient == -1:
                    return "-" + expression

                numerator = abs(coefficient.numerator)
                denominator = coefficient.denominator

                if denominator == 1:
                    result = rf"{numerator}{expression}"
                elif numerator == 1:
                    result = rf"\frac{{{expression}}}{{{denominator}}}"
                else:
                    result = rf"\frac{{{numerator}{expression}}}{{{denominator}}}"

                return ("-" if coefficient < 0 else "") + result

            x_plus = scaled_binomial("+", Fraction(1, 1) / (2 * a))
            x_minus = scaled_binomial("-", Fraction(1, 1) / (2 * a))
            y_minus = scaled_binomial("-", Fraction(1, 2))
            y_plus = scaled_binomial("+", Fraction(1, 2))

            answer = mo.md(rf"""
            \[
            (x,y)=
            \left({x_plus}, {y_minus}\right)\\[1em]
            \quad\text{{или}}\quad\\[1em]
            (x,y)=
            \left({x_minus}, {y_plus}\right)
            \]
            """)

        return mo.vstack([
            problem_4_a,
            answer
        ])

    problem_4_a_answer_simplified = _()

    problem_4_a_answer_simplified
    return


@app.cell(hide_code=True)
def _(HW_B, TangleLatex, mo):
    problem_4_b = mo.ui.anywidget(
        TangleLatex(
            latex=r"""
            (x+yi)(\tangle{b}+i)=2x-(y+1)i
            \\[1em]
            (\tangle{b}x-y)+i(x+\tangle{b}y)=2x-(y+1)i
            \\[1em]
            \begin{cases}
            \tangle{b}x-y=2x\\
            x+\tangle{b}y=-(y+1)
            \end{cases}
            \\[1em]
            y=(\tangle{b}-2)x
            \\[1em]
            x+(\tangle{b}+1)(\tangle{b}-2)x=-1
            \\[1em]
            (\tangle{b}^2-\tangle{b}-1)x=-1
            \\[1em]
            x=-\frac{1}{\tangle{b}^2-\tangle{b}-1}
            """
            ,
            parameters={
                "b": {"value": HW_B, "symbol": "b", "max_value": 10, "min_value": 1},
            },
            reveal_all_on_drag=True
        )
    )
    return (problem_4_b,)


@app.cell(hide_code=True, expand_output=True)
def _(as_fraction, mo, problem_4_b, tex_fraction):
    def _():
        b = as_fraction(problem_4_b.value["values"]["b"])

        denominator = b * b - b - 1
        x = -1 / denominator
        y = (2 - b) / denominator

        problem_4_b_answer = mo.md(
            rf"""
            \[
            x={tex_fraction(x)},\qquad y={tex_fraction(y)}
            \]

            \[
            \boxed{{(x,y)=\left({tex_fraction(x)},{tex_fraction(y)}\right)}}
            \]
            """
        )
        return mo.vstack([problem_4_b, problem_4_b_answer])


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 6
    Изразете чрез комбинации на \((e^{i\alpha})^n\)
    """)
    return


@app.cell(hide_code=True)
def _(HW_A, TangleLatex, mo):
    problem_6 = mo.ui.anywidget(
        TangleLatex(
            latex=r"""
            \text{Нека } z=e^{i\cdot\tangle{a}}.
            \\[1em]

            \text{За четно } \tangle{a}:
            \\[0.5em]

            2\cos\tangle{a}
            =e^{i\cdot\tangle{a}}+e^{-i\cdot\tangle{a}}
            \\[0.5em]
            =(e^{i\cdot\tangle{a}})^1+(e^{i\cdot\tangle{a}})^{-1}
            \\[1em]

            \frac{1}{\cos (2\cdot\tangle{a})+i\sin (2\cdot\tangle{a})}
            =\frac{1}{e^{i2\cdot\tangle{a}}}=(e^{i\cdot\tangle{a}})^{-2}
            \\[2em]

            \text{За нечетно } \tangle{a}:
            \\[1em]

            \cos (4\cdot\tangle{a})+i\sin (4\cdot\tangle{a})
            =e^{i4\cdot\tangle{a}}=(e^{i\cdot\tangle{a}})^4
            \\[1em]

            \cos\tangle{a}-i\sin\tangle{a}
            =e^{-i\cdot\tangle{a}}
            \\[0.5em]
            =(e^{i\cdot\tangle{a}})^{-1}
            """,
            parameters={
                "a": {
                    "value": HW_A,
                    "symbol": "a",
                    "max_value": 10,
                    "min_value": 1,
                },
            },
            reveal_all_on_drag=True,
        )
    )
    return (problem_6,)


@app.cell(hide_code=True, expand_output=True)
def _(mo, problem_6):
    def _():
        a = int(round(float(problem_6.value["values"]["a"])))

        if a % 2 == 0:
            problem_6_answer = mo.md(
                rf"""
                Тъй като \(a={a}\) е четно, получаваме:

                \[
                {{2\cos({a})=(e^{{i{a}}})^1+(e^{{i{a}}})^{{-1}}}} \\[1em]
                {{\frac{{1}}{{\cos({2*a})+i\sin({2*a})}}
                =(e^{{i{a}}})^{{-2}}}}
                \]
                """
            )
        else:
            problem_6_answer = mo.md(
                rf"""
                Тъй като \(a={a}\) е нечетно, получаваме:
                \[
                {{\cos({4*a})+i\sin({4*a})=(e^{{i{a}}})^4}}\\[1em]
                {{\cos({a})-i\sin({a})=(e^{{i{a}}})^{{-1}}}}
                \]
                """
            )

        return mo.vstack([problem_6, problem_6_answer])

    _()
    return


if __name__ == "__main__":
    app.run()
