import flask
from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def home():
  return 'This test website was developed by Kabir Tiwari!'


@app.route('/brainrot')
def brainrot():
  return "Generation Z has been plagued by Brainrot terms like 'skibidi' and 'sigma'. It is getting out of hand."


@app.route('/kabir-tiwari')
def kabir_tiwari():
  return "I am the developer of these sites! You can pay me to get one. $1:00 per site with a domain in your name (ex: oms-student-domains.glitch.me/john-doe), with an extra 25 cents for a domain of your choice."

@app.route('/rishab-reddy-paili')
def rishab_reddy_paili():
  return "I am Rishab. I acutally love brainrot. Some terms that particularly resonate with me are 'Skibidi', 'Sigma', 'Ohio', and 'Gyat'."

@app.route('/tyler-robitaille')
def tyler_robitaille_domain():
    return "Welcome to Tyler Robitaille's domain!"

  


@app.route('/cybertruck')
def cybertruck():
    return '''
    <html>
        <head>
            <title>Cybertruck</title>
            <!-- Importing Orbitron font from Google Fonts -->
            <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
            <style>
            
                /* Setting the background of the entire page to black */
                body {
                    background-color: black;
                    margin: 0; /* Remove default margin */
                    padding: 0; /* Remove default padding */
                }
                
                .cybertruck {
                    background-image: url('https://cdn.glitch.global/12d67a2d-d6ff-4ea4-8b53-c7a037a865bb/cybertruck.jpeg?v=1745847406288');
                    background-size: cover;
                    background-position: center;
                    height: 425px;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 24px;
                    font-family: 'Orbitron', sans-serif; /* Applying Orbitron font */
                    
                }
            </style>
        </head>
        <body>
            <div class="cybertruck">
                Cybertruck
            
            </div>
        </body>
    </html>
    '''


@app.route('/lamborghini')
def lamborghini():
    return '''
    <html>
        <head>
            <title>Lamborghini</title>
            <link href="https://fonts.googleapis.com/css2?family=Major+Mono+Display&display=swap" rel="stylesheet">
            <style>
                body {
                    background-color: black;
                    margin: 0;
                    padding: 0;
                }
                
                .lamborghini {
                    background-image: url('https://cdn.glitch.global/12d67a2d-d6ff-4ea4-8b53-c7a037a865bb/lamborghini.jpeg?v=1745858506677');
                    background-size: cover;
                    background-position: center;
                    height: 425px;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 24px;
                    font-family: 'Major Mono Display', monospace;
                }
            </style>
        </head>
        <body>  
            <div class="lamborghini">
                lamborghini
            </div>
        </body>
    </html>
    ''' 

  
  
  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
