from pyscript import display, document  # pyright: ignore[reportMissingImports]

def calculate_gwa(event=None):
    first = document.querySelector("#firstName").value
    last = document.querySelector("#lastName").value

    science = float(document.querySelector("#Science").value)
    english = float(document.querySelector("#English").value)
    math = float(document.querySelector("#Math").value)
    filipino = float(document.querySelector("#Filipino").value)
    pe = float(document.querySelector("#PE").value)
    ict = float(document.querySelector("#ICT").value)

    grades = [science, english, math, filipino, pe, ict]
    gwa = sum(grades) / len(grades)

    thresholds = [
        (90, "Excellent"),
        (85, "Very Good"),
        (80, "Good"),
        (75, "Satisfactory"),
        (0,  "Failed")
    ]
    remark = next(r for t, r in thresholds if gwa >= t)

    # show result
    display(f"Student: {first} {last}", target="result", append=False)
    display(f"Grades: {grades}", target="result", append=True)
    display(f"GWA: {gwa:.2f}", target="result", append=True)
    display(f"Remark: {remark}", target="result", append=True)
    document.querySelector("#result").classList.remove("d-none")
    