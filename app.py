from flask import *
import mlab
from jobs import Jobs,Job_sector
from quiz import *

app = Flask(__name__)
mlab.connect()
@app.route('/personal_types')
def personality_types():
    return render_template('personal_types.html')

@app.route('/job_sector')
def job_descriptions():
  job_sector = Job_sector.objects()
  return render_template('job_lists.html',js=job_sector)
  

@app.route('/job_sector/<js_code>')
def jobs_list(js_code):
  sector = Job_sector.objects(js_code=js_code)
  job_sector = sector[0]['job_sector']
  jobs_list = Jobs.objects(job_sector=job_sector)
  return render_template('job_des.html',j_list=jobs_list,js_code=js_code,job_sector=job_sector)



@app.route('/job_sector/<js_code>/<code>')
def jobs(js_code,code):
  sector = Job_sector.objects(js_code=js_code)
  jobs_list = Jobs.objects(code=code)
  js_code = sector[0]['js_code']
  jobs = jobs_list[0]
  return render_template('detail_des.html',j=jobs)

@app.route("/quiz", methods = ["GET", "POST"])
def quiz():
    question_list = Question.objects()
    person_list = PersonType.objects()
    name = person_list[0].name
   
    if request.method == "GET":
    # print(question_list)
    # for i in range (10):
    #     question1 = question_list[i]
    #     link1 = question1.question[0].link
    #     link2 = question1.question[1].link
    #     return render_template("quiz.html",l1 = link1,l2 = link2)
    # print(question1[0])
      return render_template("quiz.html", question_list = question_list)
    elif request.method == "POST":
      p = request.form['javascript_data']
      print(p)
      return redirect('/result')
      if 0 <= int(p) <= person_list[0].total_points:
        print(person_list[0].name)
        print(person_list[0].des)
        print(person_list[0].suited)
        print("abc")
        return "abc"
        # return render_template("result.html",name = person_list[0].name, des = person_list[0].des, suited = person_list[0].suited )
        # return redirect(url_for('result', name = person_list[0].name, des = person_list[0].des, suited = person_list[0].suited))
      else:
        for i in range (5):
          if person_list[i].total_points < int(p) <= person_list[i+1].total_points:
            print(person_list[i+1].name)
            print(person_list[i+1].des)
            print(person_list[i+1].suited)
            print("ABC")
            return "ABC"
            # return render_template("result.html",name = person_list[i+1].name, des = person_list[i+1].des, suited = person_list[i+1].suited)
            # return redirect(url_for('result', name = person_list[0].name, des = person_list[0].des, suited = person_list[0].suited))


@app.route('/result')
def result():
    print("hello")
    return "abc"  

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/home")
def home1():
  return render_template("home.html")

@app.route("/topics")
def topics():
  return render_template("topics.html")

@app.route("/topic1")
def topic1():
  return render_template("topic1.html")

@app.route("/topic2")
def topic2():
  return render_template("topic2.html")

@app.route("/topic3")
def topic3():
  return render_template("topic3.html")

@app.route("/topic4")
def topic4():
  return render_template("topic4.html")

@app.route("/topic5")
def topic5():
  return render_template("topic5.html")

@app.route("/topic6")
def topic6():
  return render_template("topic6.html")

@app.route("/topic7")
def topic7():
  return render_template("topic7.html")

@app.route("/topic8")
def topic8():
  return render_template("topic8.html")

@app.route("/topic9")
def topic9():
  return render_template("topic9.html")



if __name__ == '__main__':
  app.run(debug=True)