from flask import Flask, render_template, request, redirect, url_for
from frequency_calculator import calculate_frequency_multiplier
from calculate_coupling_multiplier import calculate_coupling_multiplier




app = Flask(__name__)

# Define a list to store user inputs
#user_inputs = {'H':0,'D':0,'V':0,'A':0,'lifting_frequency':0,'task_duration':0,'coupling':0}

user_inputs={}
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/equation1", methods=['GET', 'POST'])
def equation1():
    if request.method == 'POST' and request.form.get('horizontalDistance') is not None:
        # Check if horizontalDistance is a valid number
        try:
            print(request.form.get('horizontalDistance'))
            horizontal_distance = float(request.form['horizontalDistance'])
            if horizontal_distance or horizontal_distance ==0:
                print(horizontal_distance)
                # Get input from the first page
                user_inputs['H'] = horizontal_distance
                return redirect(url_for('equation2'))
            else:
                value=request.form.get('horizontalDistance')
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation1.html", page_title="Horizontal Distance Page", error=error_message,value=value)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation1.html", page_title="Horizontal Distance Page", error=error_message)

    return render_template("equation1.html", page_title="Horizontal Distance Page")


@app.route("/equation2", methods=['GET', 'POST'])
def equation2():
    if request.method == 'POST' and request.form.get('verticalDistance') is not None:
        # Check if verticalDistance is a valid number
        try:
            print(request.form.get('verticalDistance'))
            verticalDistance = float(request.form['verticalDistance'])
            if verticalDistance  or verticalDistance ==0:
                print(verticalDistance)
                # Get input from the first page
                user_inputs['V'] = verticalDistance
                return redirect(url_for('equation3'))
            else:
                value=request.form.get('verticalDistance')
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation2.html", page_title="vertical Distance Page", error=error_message,value=value)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation2.html", page_title="vertical Distance Page", error=error_message)

    return render_template("equation2.html", page_title="vertical Distance Page")



@app.route("/equation3", methods=['GET', 'POST'])
def equation3():
    if request.method == 'POST' and request.form.get('cardboardBoxHeight') is not None:
        # Check if cardboardBoxHeight is a valid number
        try:
            print(request.form.get('cardboardBoxHeight'))
            cardboardBoxHeight = float(request.form['cardboardBoxHeight'])
            if cardboardBoxHeight or cardboardBoxHeight==0 :
                print(cardboardBoxHeight)
                # Get input from the first page
                user_inputs['D'] = cardboardBoxHeight
                return redirect(url_for('equation4'))
            else:
                value=request.form.get('cardboardBoxHeight')
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation3.html", page_title="cardboardBoxHeight Distance Page", error=error_message,value=value)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation3.html", page_title="cardboardBoxHeight Distance Page", error=error_message)

    return render_template("equation3.html", page_title="cardboardBoxHeight Distance Page")




@app.route("/equation4", methods=['GET', 'POST'])
def equation4():
    if request.method == 'POST' and request.form.get('asymmetricAngle') is not None:
        # Check if asymmetricAngle is a valid number
        try:
            print(request.form.get('asymmetricAngle'))
            asymmetricAngle = float(request.form['asymmetricAngle'])
            if asymmetricAngle or asymmetricAngle ==0:
                print(asymmetricAngle)
                # Get input from the first page
                user_inputs['A'] = asymmetricAngle
                return redirect(url_for('equation5'))
            else:
                value=request.form.get('asymmetricAngle')
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation4.html", page_title="Asymmetric Angle Page", error=error_message,value=value)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation4.html", page_title="Asymmetric Angle Page", error=error_message)

    return render_template("equation4.html", page_title="Asymmetric AnglePage")





@app.route("/equation5", methods=['GET', 'POST'])
def equation5():
    if request.method == 'POST' and request.form.get('liftingFrequency') is not None and request.form.get('taskDuration'):
        # Check if taskduration is a valid number
        try:
            
            taskduration=float(request.form['taskDuration'])
            liftingFrequency=float(request.form['liftingFrequency'])
            if taskduration in range(0,9):
                print(taskduration,liftingFrequency)
                # Get input from the first page
                user_inputs['taskDuration'] = taskduration
                user_inputs['liftingFrequency'] = liftingFrequency
                return redirect(url_for('equation6'))
            else:
                value1=request.form['taskDuration']
                value2=request.form['liftingFrequency']
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation5.html", page_title="Lifting Frequency Page", error=error_message,value1=value1,value2=value2)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation5.html", page_title="Lifting Frequency Page", error=error_message)

    return render_template("equation5.html", page_title=" Lifting Frequency Page")



@app.route("/equation6", methods=['GET', 'POST'])
def equation6():
    if request.method == 'POST' and request.form.get('coupling') is not None:
        # Check if asymmetricAngle is a valid number
        try:
            print(request.form.get('coupling'))
            coupling = request.form['coupling']
            if coupling in ["Good", "Fair", "Poor"]:
                print(coupling)
                # Get input from the first page
                user_inputs['coupling'] = coupling
                return redirect(url_for('weight'))
            else:
                
                error_message = "Please enter a valid Input."
                print(error_message)
                return render_template("equation6.html", page_title="coupling Page", error=error_message)
        except ValueError:
            # Handle the case where the input is not a valid number
            error_message = "Please enter a valid Input."
            return render_template("equation6.html", page_title="coupling Page", error=error_message)

    return render_template("equation6.html", page_title="coupling Page")



def recomandtion(li):
        if is_number(li):
                if  li == 0 :
                    Results="rwl = 0"
                    Risk="cannot be determined"
                    case=1
                elif  li <= 1 :
                    Results="SAFE TASKS"
                    Risk="very Low"
                    case=2

                elif 1< li <= 1.5:
                    Results="UNSAFE TASKS"
                    Risk="Low"
                    case=3
                elif 1.5< li <= 2:
                    Results="UNSAFE "
                    Risk="Moderate"
                    case=4
                elif 2< li <= 3:
                    Results="UNSAFE "
                    Risk="High"
                    case=5
                elif 3 < li :
                    Results="UNSAFE "
                    Risk="Very High"
                    case=6
                else:
                    Results="incorrect"
                    Risk="incorrect"
                    case=7
                return Results,Risk,case
        else:
            Results="incorrect"
            Risk="incorrect"
            case="incorrect"
        return Results,Risk,case
            
    

def calc(user_inputs):
     # Load constant
     #declare intail values
                
                LC = 23

                # Calculate HM
                
                if user_inputs['H'] > 63:
                    HM = 0
                elif user_inputs['H'] < 25:
                    HM = 1
                else:
                     HM = 25 / user_inputs['H']

                # Calculate VM
                
                if user_inputs['V'] > 175:
                    VM = 0
                elif user_inputs['V'] == 0:
                    VM = 0.78
                else:
                     VM = 1 - (0.003 * abs(user_inputs['V'] - 75))

                # Calculate DM
               
                
                     

                if user_inputs['D'] > 175:
                    DM = 0
                elif user_inputs['D'] < 25:
                    DM = 1
                else:
                     DM = 0.82 + (4.5 /  user_inputs['D'])

                # Calculate AM
                
                if user_inputs['A'] > 135:
                    AM = 0
                elif user_inputs['A'] == 0:
                    AM = 1
                else:
                     AM = 1 - (0.0032 * user_inputs['A'])
                print(user_inputs)
                # Placeholder values for FM and CM, replace with actual calculations based on your table
                
                FM = calculate_frequency_multiplier(user_inputs['liftingFrequency'], user_inputs['taskDuration'],user_inputs['V'])
                
                CM = calculate_coupling_multiplier(user_inputs['coupling'], user_inputs['V'])

                # Calculate RWL using the multiplier values and LC
                try :
                    rwl = LC * HM * VM * DM * AM * FM * CM

                    # Calculate Load index

                    load_index = user_inputs['weight'] / rwl if rwl != 0 else 0  # Check to avoid division by zero
                    rwl=round(rwl, 2)
                    load_index=round(load_index, 2)
                except: rwl,load_index="Invaild inputs" ,"Invaild inputs check rwl value"
                # Generate report with all the information, including individual multiplier values
                report = {
                    'RWL': rwl,
                    'HM': HM,
                    'VM': VM,
                    'DM': DM,
                    'AM': AM,
                    'FM': FM,
                    'CM': CM,
                    'LI': load_index
                }
                results,Risk,cases=recomandtion(load_index)
                print(results,Risk)
                print(report)
                # Clear user inputs after calculation
                res={'result':results ,"risk":Risk,"cases":cases}
                return report ,res



@app.route("/weight", methods=['GET', 'POST'])
def weight():
    if request.method == 'POST' and request.form.get('weight') is not None:
        weigh=request.form['weight']
        if weigh.isdigit():
                # Get input from the eighth and final page
                user_inputs['weight'] =float(weigh)
                print(user_inputs)
                report ,res=calc(user_inputs)
                print('pass')
                
                return render_template("result.html", report=report,user_inputs=user_inputs,res=res)
        else:
                error_message = "Please enter a valid Input."
                return render_template("weight.html", page_title="weight Page", error=error_message)

    return render_template("weight.html", page_title="Weight Page")
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route("/download_pdf", methods=['GET', 'POST'])

def download_pdf():
    report ,res=calc(user_inputs)                
    return render_template("pdf.html", report=report,user_inputs=user_inputs,res=res)

if __name__ == "__main__":

    app.run(debug=True)
