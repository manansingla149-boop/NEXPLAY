
from flask import Flask, render_template

app = Flask(__name__)

games = [
    {
        "name": "Minecraft",
        "category": "Sandbox",
        "description": "Build, explore, and survive in your own world.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1672970/header.jpg"
    },
    {
        "name": "Genshin Impact",
        "category": "Adventure RPG",
        "description": "Explore Teyvat and discover its mysteries.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1286830/header.jpg"
    },
    {
        "name": "Counter-Strike 2",
        "category": "FPS",
        "description": "Team up, sharpen your aim, and compete.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg"
    },
    {
        "name": "Roblox",
        "category": "Online",
        "description": "Discover millions of experiences made by players.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/431960/header.jpg"
    }
]


@app.route("/")
def home():
    return render_template("index.html", games=games)


if __name__ == "__main__":
    app.run(debug=True)
