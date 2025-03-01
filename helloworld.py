from flask import Flask, request, render_template_string

app = Flask(__name__)

def calculate_factorial(x):
    """
    Calculate the factorial of a given integer x.
    
    :param x: Integer to calculate the factorial for.
    :return: Factorial of x, or None if x is not an integer.
    """
    if isinstance(x, int) and x >= 0:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            x = int(request.form["x"])
            if x < 0:
                result = "Veuillez entrer un entier positif."
            else:
                factorial_result = calculate_factorial(x)
                if factorial_result is not None:
                    result = f"La factorielle de {x} est: {factorial_result}"
                else:
                    result = "Une erreur s'est produite lors du calcul."
        except ValueError:
            result = "Veuillez entrer un entier valide."

    return render_template_string("""
    <html>
    <head>
        <title>Calcul de factorielle</title>
    </head>
    <body>
    <h2>Calcul de factorielle</h2>
        <form method="POST">
        <label for="x">x :</label>
        <input type="text" name="x" required><br><br>
        <button type="submit">Calculer</button>
    </form>
    <br>
        {{ result | safe }} 
    </body>
    </html>""", result=result)

if __name__ == "__main__":
    app.run(debug=True)