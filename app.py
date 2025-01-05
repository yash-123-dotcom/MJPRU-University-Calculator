from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_percentage():
    if request.method == 'POST':
        try:
            # Get SGPA values for all semesters
            sgpa_values = []
            for i in range(1, 7):
                sgpa = float(request.form.get(f'sem{i}'))
                if sgpa < 0 or sgpa > 10:
                    return render_template('index.html', error="SGPA must be between 0 and 10!")
                sgpa_values.append(sgpa)
            
            # Calculate percentage
            average_sgpa = sum(sgpa_values) / 6
            percentage = average_sgpa * 9.5
            
            return render_template('index.html', percentage=round(percentage, 2))
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers in all fields!")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 