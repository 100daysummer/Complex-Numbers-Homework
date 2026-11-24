import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import math
    import marimo as mo
    from wigglystuff import ObservablePlot, TangleLatex

    return TangleLatex, mo


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
    
    ]
    return people_dates, people_names


@app.cell(hide_code=True)
def _(mo, people_names):
    person_dropdown = mo.ui.dropdown(options= people_names, value = "Борислав");
    return (person_dropdown,)


@app.cell(hide_code=True)
def _(mo, people_dates, people_names, person_dropdown):
    # 0-indexed!!
    person_index = people_names.index(person_dropdown.value)
    HW_A = (person_index + 1) % 10 + 1
    HW_B = people_dates[person_index] % 10 + 1
    mo.vstack(
        [
            person_dropdown,
            mo.md(
                rf"""
                Ти си {person_dropdown.value}. Номерът ти в класа е {person_index+1}, a денят ти на раждане е {people_dates[person_index]}. Съответно **a** = {HW_A} и **b** = {HW_B}
                """
            )
        ]   
    )
    return (HW_B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Задача 1
    Представете в алгебричен вид
    """)
    return


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
def _(mo, problem_1_b):
    from fractions import Fraction

    b = Fraction(str(problem_1_b.value["values"]["b"])).limit_denominator(1000)

    real_part = (6 - b) / 3
    imag_part = b / 3

    def tex_fraction(x):
        sign = "-" if x < 0 else ""
        x = abs(x)

        if x.denominator == 1:
            return sign + str(x.numerator)

        return rf"{sign}\frac{{{x.numerator}}}{{{x.denominator}}}"

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

    mo.vstack([problem_1_b, problem_1_b_answer])
    return


if __name__ == "__main__":
    app.run()
