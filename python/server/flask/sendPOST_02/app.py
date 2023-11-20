
#http://localhost/hello/60 or http://localhost/hello/30


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
def index():
   dict1 = {'phy':50,'che':60,'maths':70}
   dict2 = {'ab':50,'cd':60}
   print("index called")
   print(request)
   # print(request.form)
   if request.method == 'POST':
      received = request.data
      print(received)
      dict1['phy']=30
      return render_template("index.html", result = dict2)

   return render_template("index.html", result = dict1)

if __name__ == '__main__':
   app.run(debug = True)