from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =====================================
# BURGER MENU
# =====================================

BURGERS = {
    "arugula": {
        "name": "Arugula & Caramelised Onion Burger",
        "price": 1400
    },
    "bacon": {
        "name": "Classic Bacon Cheeseburger",
        "price": 1600
    },
    "greek": {
        "name": "Greek Burger",
        "price": 1600
    },
    "mushroom": {
        "name": "Mushroom Beef Burger",
        "price": 1500
    },
    "salmon": {
        "name": "Salmon Burger",
        "price": 1350
    },
    "hawaiian": {
        "name": "Hawaiian Burger",
        "price": 1850
    },
    "bean": {
        "name": "Bean Burger",
        "price": 1350
    }
}

# =====================================
# RESTAURANT INFORMATION
# =====================================

RESTAURANT_INFO = {
    "restaurant": "Premium Burger House",
    "opening_time": "9:00 AM",
    "closing_time": "7:00 PM",
    "delivery": ["PickMe", "Uber Eats"],
    "payment": "Online bank transfer",
    "whatsapp": "+94757768177"
}

# =====================================
# CHATBOT KNOWLEDGE BASE
# =====================================

FAQS = [

    {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "answer": "Hello! Welcome to Premium Burger House! 👑 How can I help you today?"
    },

    {
        "keywords": ["opening", "open", "closing", "close", "time", "hours"],
        "answer": "We are open every day from 9:00 AM to 7:00 PM."
    },

    {
        "keywords": ["delivery", "deliver", "pickme", "pick me", "uber", "ubereats"],
        "answer": "Yes! We support delivery through PickMe and Uber Eats. Delivery availability depends on your location."
    },

    {
        "keywords": ["payment", "bank", "transfer", "online payment"],
        "answer": "We support online bank-transfer payments. Please contact our team through WhatsApp for verified payment instructions."
    },

    {
        "keywords": ["cheapest", "cheap", "lowest price"],
        "answer": "Our Bean Burger and Salmon Burger start at LKR 1,350. Our Arugula Burger costs LKR 1,400."
    },

    {
        "keywords": ["vegetarian", "vegan", "bean"],
        "answer": "Our Bean Burger is our vegetarian option. Please confirm ingredients and preparation details with our team if you have strict dietary requirements."
    },

    {
        "keywords": ["mushroom"],
        "answer": "Our Mushroom Beef Burger costs LKR 1,500. It includes beef, mushrooms, cheese, onions and mushroom sauce."
    },

    {
        "keywords": ["bacon"],
        "answer": "Our Classic Bacon Cheeseburger costs LKR 1,600. It comes with a beef patty, crispy bacon and cheese."
    },

    {
        "keywords": ["greek"],
        "answer": "Our Greek Burger costs LKR 1,600 and features feta cheese and Greek herbs."
    },

    {
        "keywords": ["salmon", "fish"],
        "answer": "Our Salmon Burger costs LKR 1,350."
    },

    {
        "keywords": ["hawaiian", "pineapple"],
        "answer": "Our Hawaiian Burger costs LKR 1,850."
    },

    {
        "keywords": ["arugula", "onion"],
        "answer": "Our Arugula & Caramelised Onion Burger costs LKR 1,400."
    },

    {
        "keywords": ["size", "large", "double", "regular"],
        "answer": "You can choose Regular, Large or Double burger sizes. Suggested additional prices: Regular +LKR 0, Large +LKR 300 and Double +LKR 500."
    },

    {
        "keywords": ["cheese", "extra", "customize", "customise", "topping"],
        "answer": "Yes! You can customize your burger with extra cheese, beef, chicken, egg, mushrooms, bacon, onions and sauces."
    },

    {
        "keywords": ["menu", "burgers", "prices", "price"],
        "answer": "Our menu: Arugula LKR 1,400 | Bacon Cheeseburger LKR 1,600 | Greek LKR 1,600 | Mushroom Beef LKR 1,500 | Salmon LKR 1,350 | Hawaiian LKR 1,850 | Bean LKR 1,350."
    },

    {
        "keywords": ["order", "ordering", "whatsapp"],
        "answer": "Choose your burger, customize the ingredients, add items to your cart and click Order Through WhatsApp."
    },

    {
        "keywords": ["contact", "phone", "number"],
        "answer": "Contact Premium Burger House through WhatsApp: +94 75 776 8177."
    },

    {
        "keywords": ["fries", "drink", "drinks", "snacks"],
        "answer": "Please check our sides and drinks section for available items."
    },

    {
        "keywords": ["thank", "thanks"],
        "answer": "You're welcome! Thank you for choosing Premium Burger House. 👑"
    }
]

# =====================================
# HOME PAGE
# =====================================

@app.route("/")
def home():
    return render_template("menu.html")


# =====================================
# CHATBOT API
# =====================================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "").lower().strip()

    if not message:
        return jsonify({
            "reply": "Please type your question."
        })

    for faq in FAQS:

        if any(keyword in message for keyword in faq["keywords"]):

            return jsonify({
                "reply": faq["answer"]
            })

    return jsonify({
        "reply": (
            "Thank you for contacting Premium Burger House! 👑 "
            "I can help you with our burger menu, prices, ingredients, "
            "customization, opening hours, delivery and payment. "
            "For additional assistance, contact our team through "
            "WhatsApp at +94 75 776 8177."
        )
    })


# =====================================
# RESTAURANT INFORMATION API
# =====================================

@app.route("/restaurant-info")
def restaurant_info():

    return jsonify({
        "success": True,
        "information": RESTAURANT_INFO,
        "burgers": BURGERS
    })


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True)