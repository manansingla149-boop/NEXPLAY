
from flask import Flask, render_template, abort

app = Flask(__name__)
@app.route("/profile")
def profile():
    return render_template("profile.html")
guides = {
    "minecraft": {
        "intro": "Explore, gather resources, craft tools, and survive in a world full of possibilities.",
        "sections": [
            {
                "title": "Getting started",
                "tips": [
                    "Collect wood and craft basic tools.",
                    "Build a shelter before your first night.",
                    "Craft a crafting table, furnace, and stone tools."
                ]
            },
            {
                "title": "Survival tips",
                "tips": [
                    "Carry food and keep your health replenished.",
                    "Use torches to light caves and your base.",
                    "Bring spare tools when exploring underground."
                ]
            },
            {
                "title": "Progression",
                "tips": [
                    "Mine iron and diamonds to improve your equipment.",
                    "Enchant your tools and armour when possible.",
                    "Prepare carefully before entering the Nether."
                ]
            }
        ]
    },
    "genshin-impact": {
        "intro": "Explore Teyvat, develop your characters, and build teams that work well together.",
        "sections": [
            {
                "title": "Getting started",
                "tips": [
                    "Follow Archon Quests to unlock regions and features.",
                    "Open Teleport Waypoints to make travelling easier.",
                    "Collect resources while exploring."
                ]
            },
            {
                "title": "Character building",
                "tips": [
                    "Level your main damage dealer and their weapon.",
                    "Upgrade useful talents.",
                    "Choose artefacts that complement each character's abilities."
                ]
            },
            {
                "title": "Combat tips",
                "tips": [
                    "Experiment with elemental reactions.",
                    "Build teams with complementary abilities.",
                    "Upgrade your characters before challenging difficult bosses."
                ]
            }
        ]
    },
    "counter-strike-2": {
        "intro": "Improve your aim, communicate with teammates, and learn how to control each map.",
        "sections": [
            {
                "title": "Aim and movement",
                "tips": [
                    "Practise crosshair placement at head level.",
                    "Learn to stop moving before firing accurately.",
                    "Use aim training and deathmatch to practise."
                ]
            },
            {
                "title": "Teamwork",
                "tips": [
                    "Share enemy positions with clear callouts.",
                    "Trade eliminations with teammates.",
                    "Coordinate utility instead of using everything at once."
                ]
            },
            {
                "title": "Match strategy",
                "tips": [
                    "Learn common map angles and bombsite layouts.",
                    "Manage your economy when buying equipment.",
                    "Review rounds to understand mistakes."
                ]
            }
        ]
    },
    "roblox": {
        "intro": "Discover different experiences, learn their mechanics, and find the playstyles you enjoy.",
        "sections": [
            {
                "title": "Getting started",
                "tips": [
                    "Read the controls and tutorial in each experience.",
                    "Try different genres to discover your favourites.",
                    "Adjust graphics settings if performance is poor."
                ]
            },
            {
                "title": "Improving",
                "tips": [
                    "Practise the mechanics specific to your chosen game.",
                    "Use in-game tutorials and legitimate community guides.",
                    "Play with friends when teamwork is useful."
                ]
            },
            {
                "title": "Account safety",
                "tips": [
                    "Never share your password or verification codes.",
                    "Avoid suspicious free Robux offers.",
                    "Use Roblox's official safety and reporting features."
                ]
            }
        ]
    },
    "valorant": {
        "intro": "Combine precise shooting, agent abilities, and teamwork to win tactical rounds.",
        "sections": [
            {
                "title": "Aim basics",
                "tips": [
                    "Keep your crosshair near likely enemy positions.",
                    "Practise controlled bursts instead of spraying constantly.",
                    "Learn when to walk quietly and when to rotate."
                ]
            },
            {
                "title": "Agent abilities",
                "tips": [
                    "Learn what each of your abilities does.",
                    "Use utility to gather information or control space.",
                    "Coordinate abilities with your teammates."
                ]
            },
            {
                "title": "Winning rounds",
                "tips": [
                    "Communicate enemy locations and your plans.",
                    "Play around the spike timer.",
                    "Adapt your strategy to the enemy team."
                ]
            }
        ]
    },
    "apex-legends": {
        "intro": "Use movement, teamwork, and smart positioning to survive and win fights.",
        "sections": [
            {
                "title": "Movement",
                "tips": [
                    "Practise sliding and moving efficiently across terrain.",
                    "Use cover when crossing open areas.",
                    "Learn the layout of the maps you play."
                ]
            },
            {
                "title": "Combat",
                "tips": [
                    "Choose weapons you can control comfortably.",
                    "Carry ammunition and healing items appropriate to your loadout.",
                    "Break line of sight when you need to recover."
                ]
            },
            {
                "title": "Squad strategy",
                "tips": [
                    "Stay close enough to support your squad.",
                    "Share loot and communicate enemy positions.",
                    "Rotate early when the ring is moving."
                ]
            }
        ]
    },
    "elden-ring": {
        "intro": "Explore the Lands Between, learn enemy patterns, and develop a build that suits you.",
        "sections": [
            {
                "title": "Getting started",
                "tips": [
                    "Explore side areas to find useful equipment and upgrades.",
                    "Activate Sites of Grace to establish checkpoints.",
                    "Return to difficult encounters after gaining experience."
                ]
            },
            {
                "title": "Combat",
                "tips": [
                    "Learn enemy attack patterns before committing to attacks.",
                    "Manage stamina so you can dodge or defend.",
                    "Experiment with different weapons and Ashes of War."
                ]
            },
            {
                "title": "Character progression",
                "tips": [
                    "Upgrade your preferred weapon regularly.",
                    "Invest in attributes that support your chosen build.",
                    "Explore for upgrade materials and useful items."
                ]
            }
        ]
    },
    "stardew-valley": {
        "intro": "Build your farm, make friends, explore the valley, and progress at your own pace.",
        "sections": [
            {
                "title": "Your first season",
                "tips": [
                    "Plant crops that can mature before the season ends.",
                    "Water crops daily unless a sprinkler does the work.",
                    "Keep some money available for seeds and supplies."
                ]
            },
            {
                "title": "Making progress",
                "tips": [
                    "Upgrade tools when you can spare them.",
                    "Explore the mines for ore and useful resources.",
                    "Check the calendar for birthdays and festivals."
                ]
            },
            {
                "title": "Farm planning",
                "tips": [
                    "Save useful materials for crafting and upgrades.",
                    "Place chests near the activities you do most.",
                    "Try fishing, foraging, farming, and relationships."
                ]
            }
        ]
    },
    "terraria": {
        "intro": "Gather materials, build a base, explore underground, and prepare for tougher enemies.",
        "sections": [
            {
                "title": "Early game",
                "tips": [
                    "Gather wood and build a safe starting shelter.",
                    "Craft torches and explore caves carefully.",
                    "Build suitable rooms for NPCs to move in."
                ]
            },
            {
                "title": "Equipment",
                "tips": [
                    "Explore underground for ores and treasure chests.",
                    "Try different weapons to find your preferred combat style.",
                    "Keep useful healing items ready for boss fights."
                ]
            },
            {
                "title": "Exploration",
                "tips": [
                    "Carry platforms, ropes, and torches.",
                    "Prepare an arena before challenging bosses.",
                    "Store rare items somewhere safe."
                ]
            }
        ]
    },
    "cyberpunk-2077": {
        "intro": "Explore Night City, develop your character, and approach missions in your own style.",
        "sections": [
            {
                "title": "Getting started",
                "tips": [
                    "Complete introductory missions to learn the mechanics.",
                    "Explore shops and upgrade your equipment when useful.",
                    "Save your game before challenging missions."
                ]
            },
            {
                "title": "Character builds",
                "tips": [
                    "Choose attributes that support your preferred playstyle.",
                    "Experiment with stealth, hacking, or direct combat.",
                    "Check cyberware requirements before planning upgrades."
                ]
            },
            {
                "title": "Exploration",
                "tips": [
                    "Use the map to find activities and side jobs.",
                    "Read mission objectives before choosing an approach.",
                    "Upgrade equipment as enemies and challenges become harder."
                ]
            }
        ]
    },
    "left-4-dead-2": {
        "intro": "Work as a team, manage supplies, and survive cooperative campaigns together.",
        "sections": [
            {
                "title": "Teamwork",
                "tips": [
                    "Stay close enough to help teammates.",
                    "Warn the team before using explosives or other area effects.",
                    "Help teammates who become separated or incapacitated."
                ]
            },
            {
                "title": "Supplies",
                "tips": [
                    "Share healing supplies when a teammate needs them more.",
                    "Use ammunition carefully during difficult encounters.",
                    "Look for supplies before leaving safe rooms."
                ]
            },
            {
                "title": "Survival strategy",
                "tips": [
                    "Listen for special infected and communicate threats.",
                    "Watch for hazards before rushing ahead.",
                    "Move together toward the next safe room."
                ]
            }
        ]
    },
    "portal-2": {
        "intro": "Solve environmental puzzles by experimenting with portals, momentum, and timing.",
        "sections": [
            {
                "title": "Portal basics",
                "tips": [
                    "Remember that you can travel between connected portals.",
                    "Look for surfaces where portals can be placed.",
                    "Observe the room before trying random solutions."
                ]
            },
            {
                "title": "Puzzle solving",
                "tips": [
                    "Identify switches, cubes, platforms, and barriers.",
                    "Break complex puzzles into smaller steps.",
                    "Try different portal placements when you get stuck."
                ]
            },
            {
                "title": "Advanced mechanics",
                "tips": [
                    "Use momentum to reach distant platforms.",
                    "Pay attention to the direction you enter a portal.",
                    "Experiment with gels and other mechanics as they appear."
                ]
            }
        ]
    }
}

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
        "image": "https://fastcdn.hoyoverse.com/content-v2/hk4e/159746/1a4f7f8a4f7f6c7d8e9a0b1c2d3e4f5a_1234567890123456789.png"
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
        "image": "https://tr.rbxcdn.com/180DAY-6f6b6b6b6b6b6b6b6b6b6b6b6b6b6b6b/420/420/Image/Png/noFilter"
    },
    {
        "slug": "valorant",
        "name": "VALORANT",
        "category": "FPS",
        "description": "Combine precise gunplay with unique agent abilities.",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt2e5d8c6b7a4f3e2d/valorant.jpg"
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

@app.route("/guides/<slug>")
def game_guide(slug):
    game = next(
        (game for game in games if game["slug"] == slug),
        None
    )

    if game is None:
        abort(404)

    guide = guides.get(slug)

    if guide is None:
        abort(404)

    return render_template(
        "guides.html",
        game=game,
        guide=guide
    )


@app.errorhandler(404)
def page_not_found(error):
    return "Page not found — return to NEXPLAY.", 404


if __name__ == "__main__":
    app.run(debug=True)

