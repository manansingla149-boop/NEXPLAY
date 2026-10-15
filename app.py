
from flask import Flask, render_template, abort

app = Flask(__name__)

games = [
    {
        "slug": "minecraft",
        "name": "Minecraft",
        "category": "Sandbox",
        "description": "Build, explore, craft, and survive in your own world.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1672970/header.jpg"
    },
    {
        "slug": "genshin-impact",
        "name": "Genshin Impact",
        "category": "RPG",
        "description": "Explore Teyvat and uncover the secrets of its world.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1286830/header.jpg"
    },
    {
        "slug": "counter-strike-2",
        "name": "Counter-Strike 2",
        "category": "FPS",
        "description": "Team up, sharpen your aim, and compete.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg"
    },
    {
        "slug": "roblox",
        "name": "Roblox",
        "category": "Online",
        "description": "Discover experiences created by players around the world.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/431960/header.jpg"
    },
    {
        "slug": "valorant",
        "name": "VALORANT",
        "category": "FPS",
        "description": "Combine precise gunplay with unique agent abilities.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1277100/header.jpg"
    },
    {
        "slug": "apex-legends",
        "name": "Apex Legends",
        "category": "FPS",
        "description": "Battle alongside your squad in a fast-paced arena.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1172470/header.jpg"
    },
    {
        "slug": "elden-ring",
        "name": "Elden Ring",
        "category": "RPG",
        "description": "Explore a mysterious world full of challenging adventures.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg"
    },
    {
        "slug": "stardew-valley",
        "name": "Stardew Valley",
        "category": "Simulation",
        "description": "Build a farm, meet villagers, and enjoy country life.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg"
    },
    {
        "slug": "terraria",
        "name": "Terraria",
        "category": "Sandbox",
        "description": "Dig, build, explore, and battle in a colourful world.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg"
    },
    {
        "slug": "cyberpunk-2077",
        "name": "Cyberpunk 2077",
        "category": "RPG",
        "description": "Explore a futuristic open world filled with stories.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg"
    },
    {
        "slug": "left-4-dead-2",
        "name": "Left 4 Dead 2",
        "category": "Action",
        "description": "Work together with friends in a cooperative action game.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/550/header.jpg"
    },
    {
        "slug": "portal-2",
        "name": "Portal 2",
        "category": "Puzzle",
        "description": "Solve clever puzzles using a portal device.",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/620/header.jpg"
    }
]


@app.route("/")
def home():
    categories = sorted({game["category"] for game in games})

    return render_template(
        "index.html",
        games=games,
        categories=categories
    )


@app.route("/game/<slug>")
def game_detail(slug):
    game = next(
        (game for game in games if game["slug"] == slug),
        None
    )

    if game is None:
        abort(404)

    return render_template(
        "game.html",
        game=game,
        games=games
    )


@app.errorhandler(404)
def page_not_found(error):
    return "Page not found — return to NEXPLAY.", 404


if __name__ == "__main__":
    app.run(debug=True)

