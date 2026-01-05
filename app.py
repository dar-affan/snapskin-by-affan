from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SnapSkin by Affan</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ffecd2, #fcb69f);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .box {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                text-align: center;
                width: 90%;
                max-width: 400px;
            }
            h1 {
                margin-bottom: 10px;
                color: #ff6a00;
            }
            p {
                color: #444;
            }
            .insta {
                margin-top: 20px;
                font-weight: bold;
                color: #e1306c;
            }
            button {
                margin-top: 20px;
                padding: 12px 25px;
                border: none;
                border-radius: 30px;
                background: #ff6a00;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                transform: scale(1.05);
                background: #ff4500;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>SnapSkin by Affan</h1>
            <p>Web App is LIVE 🚀</p>
            <button>Explore Skins</button>
            <div class="insta">Instagram: dar_affaan</div>
        </div>
    </body>
    </html>
    """
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
