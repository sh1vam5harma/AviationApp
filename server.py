from flask import Flask, render_template, request, redirect, url_for, flash
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

#Would it be better to consolidate vocab or have the vocab specific to each lesson?

component_id = 0

#Lessons

lessons = {
    "1":{
        "lesson_id": "1",
        "title": "Airspeed Indicator",
        "components": [
            ["Description", "The Airspeed Indicator shows you your airspeed as indicated in Nautical Miles, or Knots. This is how fast your plane is going relative to the wind. There is more to airspeed, but we will stick to this for now.", "Airspeed.png"],
            ["Never Exceed Speed", "This red line is the Never Exceed Speed, the maximum speed which the airplane can be flown safely. Also annotated as Vne.", "Airspeed_Indicator_VNE.png"], 
            ["Caution Speed", "The Yellow Arc represents the speed which could cause damage if air conditions aren’t stable. Meaning, these are the speeds to be flown in smooth air only. ", "Airspeed_Indicator_Yellow.png"],
            ["Normal Operating Range", "The Green Arc represents the speed which the aircraft can be operated safely. The end of the green arc is also known as Vn0.", "Airspeed_Indicator_Green.png"],
            ["Flap Operating Range", "The bolded white arc represents the airspeeds which flaps can be used safely. ", "Airspeed_Indicator_Flaps.png"],
            ["Stall Speed(Flaps Retracted)", "The end of the green mark represents the stall speed for when flaps are up(not deployed) and gear retracted. The stall speed is when the airplane doesn’t have enough airspeed to maintain lift and keep flying. ", "Airspeed_Indicator_Stall_Normal.png"],
            ["Stall Speed(Flaps Deployed)", "The end of the white arc represents the stall speed for when flaps are deployed. This is less than when flaps are not deployed as flaps increase lift and drag.", "Airspeed_Indicator_Stall_Flaps.png"]
        ],
        "image": "https://pilotinstitute.com/wp-content/uploads/2021/10/airspeed-indicator.png",
        "vocab_ids": [1, 3, 4],
        "video": {"src": "airspeed_animation.mp4", "autoplay": True, "loop": True, "size":[100,100]}
    },
    "2":{
        "lesson_id":" 2",
        "title": "Attitude Indicator",
        "components": [
            ["Description", "The Attitude Indicator shows the plane’s attitude, which means the orientation of the aircraft with respect to the horizon.", "ADI.png"],
            ["Bank Angle", "These white lines indicate Angle of Roll, how much you are rotating about your front-back axis.", "ADI_bank.png"],
            ["Pitch Angle", "These white lines in the center of the indicator show Angle of Pitch, or how much you are pointing your noise up and down.", "ADI_pitch.png"],
            ["Artificial Horizon", "The brown part is simulated land, and the blue part represents simulated sky, with the border being the artificial horizon. This artificial horizon will stay relative to your attitude. Right now this instrument is showing perfect level flight.", "ADI_horizon.png"],
        ],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSZDdAU2QMbXi2B2XtqgHCW_onle0M8bDQw5Ch3A-jKg&s",
        "vocab_ids": [6, 7],
         "video": {"src": "attitude_animation.mov", "autoplay": True, "loop": True, "size":[70, 70]}
    },
    "3":{
        "lesson_id": "3",
        "title": "Altimeter",
        "components": [
            ["Description", "The Barometric Altimeter gives you Pressure Altitude, which measures approximate distance of the plane above sea level. To represent multiple orders of magnitude of altitude, the gauge is set up as a clock, with multiple hands.", "Altimeter.png"],
            ["Reference Pressure", "The reference pressure, which must be calibrated by the pilot per local conditions, is the pressure just above mean sea level.", "Altimeter_pressure.png"],
            ["100' Hand", "Measures your 100 Feet", "Altimeter_100.png"], 
            ["1,000' Hand", "Measures your 1000 Feet", "Altimeter_1k.png"], 
            ["10,000 Hand", "Measures your 10,000 Feet", "Altimeter_10k.png"]
        ],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s",
        "vocab_ids": [9, 10, 11],
        "video": {"src": "altimeter.mov", "autoplay": False, "loop": False, "size":[100,100]}
    },
    "4":{
        "lesson_id": "4",
        "title": "Turn Coordinator",
        "components": [
            ["Description", "The Turn Coordinator gives you a visual of their direction and rate of heading change in a turn. It also monitors roll and yaw.", "Turn.png"],
            ["Plane Silhouette", "This represents your plane. The plane will rotate clockwise and counterclockwise according to your bank angle.", "Turn_plane.png"],
            ["Bank Angle", "Representation of your bank angle.", "Turn_bank.png"],
            ["Inclinometer", "Measures yaw in turn. If your turn is not coordinated, the center ball will deviate left or right.", "Turn_inclinometer.png"]
        ],
        "image": "https://pilotinstitute.com/wp-content/uploads/2022/07/turn-coordinator.png",
        "vocab_ids": [7, 14],
        "video": {"src": "turn_animation.mov", "autoplay": True, "loop": True, "size":[100,100]}
    },
    "5":{
        "lesson_id": "5",
        "title": "Heading Indicator",
        "components": [
            ["Description", "The Heading Indicator displays the aircraft's heading, or the direction of the nose relative to Magnetic North. Each number is your heading value in degrees divided by 10. Each small tick represents 5 degrees and each large tick represents 10.", "Heading.png"],
            ["Lubbard Line", "Line from tail to nose that extends to heading. Basically where your nose is pointing.", "Heading_lubbard.png"],
            ["North", "0 degrees. Note that this is Magnetic North where the magnetic fields lead, which is different from True North, which is the point of rotation for Earth.", "Heading_n.png"],
            ["East", "90 degrees.", "Heading_e.png"],
            ["South", "180 degrees.", "Heading_s.png"],
            ["West", "270 degrees.", "Heading_w.png"],
        ],
        "image": "https://learntoflyblog.com/wp-content/uploads/2016/11/7-31.png",
        "vocab_ids": [8],
         "video": {"src": "heading_animation.mov", "autoplay": True, "loop": True, "size":[60,60]}
    },
    "6":{
        "lesson_id": "6",
        "title": "Vertical Speed Indicator",
        "components": [
            ["Description", "The Vertical Speed Indicator displays the rate of climb or descent in Feet per Minute.", "Vertical.png"],
            ["Zero", "If your pointer is here, that means your vertical speed is 0, and neither climbing nor descending.", "Vertical_zero.png"],
            ["Up", "If your pointer is here, you are climbing, i.e. going up in altitude.", "Vertical_up.png"],
            ["Down", "If your pointer is here, you are descending.", "Vertical_dn.png"]
        ],
        "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp",
        "vocab_ids": [],
        "video": {"src": "vsi.mov", "autoplay": False, "loop": False, "size":[100,100]}
    }  
    
}


vocabulary = {
    "airspeed": "The speed of an aircraft relative to the air through which it is moving. Note that this is different from ground speed, which is the speed of the aircraft relative to the ground. This can differ due to direction and magnitude of wind.",
    "flaps": "Parts of a wing that when deployed increase lift (upwards force) and drag (opposing force).",
    "stall": "Minimum flight speed at which the aircraft is controllable.",
    "ground": "The speed of an aircraft relative to the ground.",
    "pitch": "The rotation of an aircraft about its lateral axis, causing the nose to move up or down.",
    "attitude": "Orientation of the plane.",
    "bank angle": "Angle of roll.",
    "knots": "Also known as nautical miles, equivalent to 1.15 miles. 1 Knot is equal to 1 minute of latitude",
    "magnetic north": "The direction the north end of a compass points to. Note that this differs from true north, which is the axis about the earth's rotation.",
    "barometric altitude": "Altitude as determined by air pressure relative to Mean Sea Level. Air pressure decreases as altitude increases. Due to weather fluctuations, barometric altitude must be calibrated.",
    "absolute altitude": "How far one is directly above the ground.",
    "mean sea level": "The average height of the entire ocean's surface.",
    "roll": "Rotation of an aircraft about its longitudinal axis, causing one wing to rise while the other falls.",
    "pitch": "Rotation of an aircraft about its lateral axis, causing the nose to move up or down.",
    "yaw": "Rotation of an aircraft about its vertical axis, causing the nose to turn left or right."
}

#Questions
#Types of questions: Multiple Choice, Fill In The Blank, Identify...
questions = {
    "1": {
        "question": "You're flying at 10,000 feet and notice a sudden decrease in indicated speed. Which instrument would you primarily rely on to monitor and respond to this change?",
        "options": [
            {"text": "Airspeed Indicator", "image": "https://pilotinstitute.com/wp-content/uploads/2021/10/airspeed-indicator.png"},
            {"text": "Turn Coordinator", "image": "https://pilotinstitute.com/wp-content/uploads/2022/07/turn-coordinator.png"},
            {"text": "Altimeter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s"},
            {"text": "Vertical Speed Indicator", "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp"}
        ],
        "answer": "Airspeed Indicator",
        "explanation": {
            "Turn Coordinator": "The Turn Coordinator measures the rate of turn of the aircraft, not the airspeed. It wouldn't directly help in monitoring and responding to a decrease in indicated speed.",
            "Altimeter": "The Altimeter provides information about the altitude, not airspeed.",
            "Vertical Speed Indicator": "The Vertical Speed Indicator measures the rate of climb or descent, not airspeed."
        }
    },
    "2": {
        "question": "You're flying from a high-pressure area to a low-pressure area. Which instrument would be most affected by this transition?",
        "options": [
            {"text": "Airspeed Indicator", "image": "https://pilotinstitute.com/wp-content/uploads/2021/10/airspeed-indicator.png"},
            {"text": "Turn Coordinator", "image": "https://pilotinstitute.com/wp-content/uploads/2022/07/turn-coordinator.png"},
            {"text": "Altimeter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s"},
            {"text": "Vertical Speed Indicator", "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp"}
        ],
        "answer": "Altimeter",
        "explanation": {
            "Turn Coordinator": "The Turn Coordinator measures the rate of turn of the aircraft, not directly affected by pressure changes.",
            "Airspeed Indicator": "The Airspeed Indicator measures the speed relative to the surrounding air, so it can be affected by changes in air pressure.",
            "Vertical Speed Indicator": "The Vertical Speed Indicator measures the rate of climb or descent, not directly affected by pressure changes."
        }
    },
    "3": {
        "question": "What instrument provides real-time information about the rate of climb or descent of an aircraft",
        "options": [
            {"text": "Airspeed Indicator", "image": "https://pilotinstitute.com/wp-content/uploads/2021/10/airspeed-indicator.png"},
            {"text": "Heading Indicator", "image": "https://learntoflyblog.com/wp-content/uploads/2016/11/7-31.png"},
            {"text": "Altimeter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s"},
            {"text": "Vertical Speed Indicator", "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp"}
        ],
        "answer": "Vertical Speed Indicator",
        "explanation": {
            "Airspeed Indicator": "The Airspeed Indicator measures the speed relative to the surrounding air, not directly related to changes in altitude during level flight.",
            "Heading Indicator": "The Heading Indicator shows the aircraft's direction, not directly related to changes in altitude during level flight.",
            "Altimeter": "The Altimeter provides information about altitude but is not primarily used to monitor changes in rate of climb or descent.",
        }
    },
    "4": {
        "question": "You're performing a turn, but your instrument indicates a skid. Which instrument would help you correct the coordination of your turn?",
        "options": [
            {"text": "Airspeed Indicator", "image": "https://pilotinstitute.com/wp-content/uploads/2021/10/airspeed-indicator.png"},
            {"text": "Turn Coordinator", "image": "https://pilotinstitute.com/wp-content/uploads/2022/07/turn-coordinator.png"},
            {"text": "Altimeter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s"},
            {"text": "Vertical Speed Indicator", "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp"}
        ],
        "answer": "Turn Coordinator",
        "explanation": {
            "Airspeed Indicator": "The Airspeed Indicator measures the speed relative to the surrounding air, not directly related to turn coordination.",
            "Altimeter": "The Altimeter provides information about altitude, not directly related to turn coordination.",
            "Vertical Speed Indicator": "The Vertical Speed Indicator measures the rate of climb or descent, not directly related to turn coordination.",
        }
    },
    "5": {
        "question": "You're flying in turbulent weather conditions, and your aircraft experiences sudden pitch changes. Which instrument would you primarily rely on to monitor and control your pitch attitude?",
        "options": [
            {"text": "Attitude Indicator", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSZDdAU2QMbXi2B2XtqgHCW_onle0M8bDQw5Ch3A-jKg&s"},
            {"text": "Heading Indicator", "image": "https://learntoflyblog.com/wp-content/uploads/2016/11/7-31.png"},
            {"text": "Altimeter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_YC-l5xcViX5dW5DszeDcISvb5bF0sUGNC7kwwEjzvQ&s"},
            {"text": "Vertical Speed Indicator", "image": "https://www.cfinotebook.net/graphics/avionics-and-instruments/vertical-speed-indicator/vertical-speed-indicator.webp"}
        ],
        "answer": "Attitude Indicator",
        "explanation": {
            "Heading Indicator": "The Heading Indicator shows the aircraft's direction, not directly related to pitch attitude.",
            "Altimeter": "The Altimeter provides information about altitude, not directly related to pitch attitude.",
            "Vertical Speed Indicator": "The Vertical Speed Indicator measures the rate of climb or descent, not directly related to pitch attitude.",
        }
    }
}



correct_answers = 0

def update_correct_answers():
    global correct_answers
    correct_answers += 1

# Route for homepage
 
# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Learn
@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    lesson = lessons.get(str(lesson_id))

    previous_lesson_id = str(lesson_id - 1) if lesson_id > 1 else None
    next_lesson_id = str(lesson_id + 1) if lesson_id < len(lessons) else None
    component=1
    if lesson_id == 1:
        video_file = lesson.get('video', None)
    else:
        video_file = None
    
    return render_template('learn.html', lesson=lesson, vocabulary=vocabulary, previous_lesson_id=previous_lesson_id, next_lesson_id=next_lesson_id, component=component, video=video_file)



@app.route('/quiz_start')
def quiz_start():
    global correct_answers
    correct_answers = 0
    return render_template('quiz_start.html')



# Quiz
@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if request.method == 'POST':
        selected_answer = request.form.get('answer')  
        correct_answer = questions[str(question_id)]['answer']
        next_question_id = str(int(question_id) + 1) if int(question_id) < len(questions) else None
        if selected_answer == correct_answer:
            update_correct_answers()
            return redirect(url_for('quiz_results', result='correct', next_question_id=next_question_id))
        else:
            explanation = questions[str(question_id)].get('explanation', {}).get(selected_answer, '')
            
            return redirect(url_for('quiz_results', result='incorrect', explanation=explanation, next_question_id=next_question_id))
    else:
        question = questions[str(question_id)]
        return render_template('quiz.html', question=question, question_id=question_id)


# Quiz Results
@app.route('/quiz_results')
def quiz_results():
    result = request.args.get('result', '')
    explanation = request.args.get('explanation', '')
    next_question_id = request.args.get('next_question_id')
    return render_template('quiz_results.html', result=result, explanation=explanation, next_question_id=next_question_id)

@app.route('/quiz_end')
def quiz_end():
     return render_template('quiz_end.html', correct_answers=correct_answers)

if __name__ == '__main__':
    app.run(debug=True)