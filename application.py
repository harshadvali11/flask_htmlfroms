from flask import Flask,render_template,request

AI=Flask(__name__)

@AI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data['name']

    return render_template('htmlforms.html')

if __name__=='__main__':
    AI.run(debug=True)