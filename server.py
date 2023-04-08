from flask import Flask, render_template


app = Flask( __name__ )


@app.route( "/play", methods=["GET"] )
def display_play_ground():
    return render_template( "index.html", x = 3) 


@app.route( "/play/<int:x>", methods = ["GET"] )
def play_x(x):
    return render_template("index.html", x = x )


@app.route( "/play/<int:x>/<string:color>", methods = ["GET"] )
def dif_color(x, color):
    return render_template( "index.html", x = x, color = color )



if __name__ == "__main__":
    app.run( debug = True)