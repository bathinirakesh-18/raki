from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [{
  "id":1,
  "title":"Data Engineer",
  "location":"Bangaluru",
  "salary":"Rs.10,00,000"
},
{
  "id":2,
  "title":"Data Scientist",
  "location":"Chennai",
  "salary":"Rs.15,00,000"
},
{
  "id":3,
  "title":"Frontend Developer",
  "location":"Mumbai"
},
{
  "id":4,
  "title":"Backend Developer",
  "location":"Hyderabad",
  "salary":"$120,000"
}]
@app.route('/')
def incredible():
  return render_template('home.html',jobs=JOBS,company_name="Rake$h")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug=True)


# 