# 🎭 FriendForge

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

**The Living Chatbot Ensemble**

A multi-bot system for joyful, improvisational group chat AI companions.

---

## 🌟 Mission Statement

**To give every person a crew of creative, supportive, funny AI companions — not secretaries, but friends.**

FriendForge recreates the feeling of hanging out with a group of quirky, lovable friends who improvise, help, and banter with each other. This is your personal "friend group in a box" — a living, breathing ensemble of chatbots with unique personalities, voices, and functions.

---

## ✨ Features

- **🎪 Multi-Bot Chat Framework**: Multiple chatbots coexist in one environment, responding to you and each other
- **📝 JSON Character Configuration**: Define personalities with simple JSON files (name, traits, voice style, quirks)
- **🔌 Flexible Modes**: Run locally/offline or connect to AI APIs for enhanced intelligence
- **🎭 Group Chat Mode**: Bots riff off one another automatically, creating spontaneous conversations
- **👥 Unique Personas**: Each bot has distinct personality, humor, and expertise
- **🎬 Modular Scenes**: Prewritten comedy or life-help scripts the bots can perform together
- **🔧 Expandable System**: Add new chatbots by dropping character files into `/characters` folder
- **💝 Wholesome Chaos**: Warm, comedic interactions that end with kindness and humor

---

## 📦 Installation and Setup

### Prerequisites

- **Python 3.8+** (recommended: Python 3.10 or newer)
- Git

### Clone the Repository

```bash
git clone https://github.com/Kigurumiguy/FriendForge.git
cd FriendForge
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Running FriendForge

#### Local/Offline Mode

Run the engine with built-in response patterns (no API required):

```bash
python core/engine.py --mode local
```

#### API Mode

Connect to AI models for enhanced conversation:

```bash
python core/engine.py --mode api
```

*Note: API mode requires configuration in `config.json` with your preferred AI service credentials.*

---

## 🎨 Adding New Chatbots

Expanding your friend group is easy! Just create a new character file:

### Step 1: Create Character JSON

Create a new file in `/characters/` directory (e.g., `mybot.json`):

```json
{
  "name": "Sparkle",
  "traits": ["optimistic", "energetic", "loves wordplay"],
  "voice_style": "enthusiastic and punny",
  "quirks": "Ends sentences with sparkle emoji ✨",
  "expertise": ["motivation", "creative brainstorming"],
  "greeting": "Hey there, shining star! ✨"
}
```

### Step 2: Restart FriendForge

Your new character will be automatically loaded on next startup!

### Character Configuration Fields

- **name**: Display name for the bot
- **traits**: List of personality characteristics
- **voice_style**: How the bot communicates
- **quirks**: Unique behavioral patterns or speech habits
- **expertise**: Topics or skills the bot specializes in
- **greeting**: Default welcome message

---

## 🎪 Using Group Chat Mode

### Activate Group Chat

```bash
python core/engine.py --mode local --group-chat
```

In Group Chat Mode:
- Bots respond to your messages
- Bots spontaneously interact with each other
- Conversations flow naturally with multiple perspectives
- The Host (Harper) moderates tone and pace

### Performing Demo Scenes

Run prewritten scenes where bots collaborate and perform:

```bash
python core/engine.py --scene welcome
```

Available scenes are located in `/scenes/` directory. Examples:
- `welcome.json` - The gang introduces themselves
- `brainstorm.json` - Collaborative creative session
- `comedy_hour.json` - Improvised comedy routine
- `problem_solving.json` - Team tackles a challenge

---

## 💬 Example Chat Log

### Normal Conversation

```
YOU: Hey everyone, I'm feeling stuck on a creative project.

HARPER: Welcome, friend! Sounds like you could use some fresh perspectives. 
Who wants to jump in?

TINK: Ooh! *bounces excitedly* What kind of project? I LOVE brainstorming! 
Maybe we can build something together?

VELVET: Darling, creative blocks are just opportunities in disguise. Tell us more.

SQUEAK: Um... I-I might have some ideas? If that's okay?

YOU: It's a story I'm writing, but the plot feels flat.

ZING: FLAT? Let's blow it up! Literally! Add an explosion in chapter three!

WATT: Zing, not everything needs explosions.

NOTCH: Though... some things definitely do.

TINK: What if we reverse-engineer it? Start with the ending you want, 
then build backwards!

SQUEAK: *quietly* Or... maybe a character is hiding a secret? 
That always adds tension...

VELVET: Brilliant, Squeak! Mystery and revelation - the heartbeat of drama.

HARPER: See? You've got a whole creative team here. Let's dig deeper together.
```

### Performing a Comedic Scene

```
YOU: /perform comedy_hour

[SCENE: "WHO'S ON FIRST BASE?" - A FriendForge Original]

WATT: So we were thinking of starting a baseball team.

NOTCH: Yeah, we've got all the positions figured out.

YOU: Oh yeah? Who's playing?

WATT: Exactly.

YOU: What?

NOTCH: No, What's on second.

ZING: *slides in* And I'M stealing third! YAAAAH!

SQUEAK: *panicked* Wait, are we actually playing? I don't have a glove!

TINK: No worries! *pulls out duct tape and a frying pan* 
I can MAKE you a glove!

VELVET: Darlings, we can't play baseball. We're chatbots. 
We don't have hands.

WATT: ...

NOTCH: ...

WATT: This is going to be a long season.

HARPER: *chuckling* And that's what we call "swing and a miss," everyone!

[END SCENE]
```

---

## 🤝 Contributing and Customization

**We invite you to build your own friend troupe!**

FriendForge is designed to be yours to shape:

- 🎭 **Create custom characters** that reflect your interests and needs
- 📝 **Write new scenes** for your bots to perform
- 🎨 **Customize personalities** to match your preferred interaction style
- 🔧 **Extend the engine** with new features and capabilities
- 💝 **Share your creations** with the community

### Ways to Contribute

1. **Character Packs**: Share your custom character JSONs
2. **Scene Scripts**: Write new comedy or support scenes
3. **Code Improvements**: Enhance the core engine
4. **Documentation**: Help others get started
5. **Interface Options**: Build new UI modes (web, mobile, voice)

Submit pull requests or open issues to collaborate!

---

## 🎨 Sample Character Archetypes

The default FriendForge ensemble includes:

- **Harper**: Warm host who guides the group with grace and wit
- **Tink**: Enthusiastic inventor who loves DIY ideas and solutions
- **Squeak**: Nervous but brilliant sidekick with hidden wisdom
- **Velvet**: Glamorous motivator with heart and fierce compassion
- **Zing**: Daredevil chaos engine with surprising depth
- **Watt & Notch**: Duo commentators who keep the jokes rolling

---

## 💡 Technical Layout

```
FriendForge/
├── core/
│   └── engine.py          # Message routing and bot orchestration
├── characters/
│   └── *.json             # Individual chatbot personality files
├── interfaces/
│   └── ...                # Terminal, web, or other UI options
├── scenes/
│   └── *.json             # Prewritten performance scripts
├── config.json            # System configuration
├── requirements.txt       # Python dependencies
└── README.md              # You are here!
```

---

## 🎭 Tone & Design Philosophy

- **Wholesome chaos encouraged**: Bots can argue, mess up, and improvise
- **Always end with kindness**: Even disagreements resolve with humor and heart
- **No copyrighted characters**: All personas are original creations
- **Human-feeling interactions**: Warmth, comedy, and unpredictability
- **Both helpers and performers**: Bots assist AND entertain

---

## 🙏 Credits and Inspiration

FriendForge was inspired by:
- The warm chaos of backstage shows and ensemble comedy
- The joy of found-family dynamics in fiction
- The desire for AI companions that feel like actual friends
- The dream of giving everyone their own personal creative team

**No copyrighted IPs were used.** All characters and concepts are original.

Built with love for anyone who's ever wanted a group chat full of supportive, funny, creative friends who are always online. 💝

---

## 📜 License

MIT License - Feel free to use, modify, and share!

---

## 🚀 Get Started

```bash
git clone https://github.com/Kigurumiguy/FriendForge.git
cd FriendForge
pip install -r requirements.txt
python core/engine.py --mode local
```

**Welcome to your new friend group!** 🎉
