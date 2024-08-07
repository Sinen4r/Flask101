from flask import Flask, render_template,Response
import cv2
app =Flask(__name__)
camera=cv2.VideoCapture(0)

def genrate_frames():
    while True:
        sucess,frame=camera.read()
        if not sucess:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/')
def index():
    return render_template('index2.html')
@app.route('/video')
def video():
    return Response(genrate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)