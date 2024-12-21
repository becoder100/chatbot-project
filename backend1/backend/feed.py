from pymongo import MongoClient

# Connect to MongoDB local instance
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client.chatapp
products_collection = db.products

# Array of product data (add your array here)
product_data = [
  { "Name": "Running Shoes", "Price": 49.99, "Description": "Comfortable running shoes for daily jogs.", "StockCount": 150 },
  { "Name": "Wireless Earbuds", "Price": 79.99, "Description": "High-quality earbuds with noise cancellation.", "StockCount": 75 },
  { "Name": "Gaming Laptop", "Price": 999.99, "Description": "Powerful laptop for gaming enthusiasts.", "StockCount": 25 },
  { "Name": "Smartphone", "Price": 699.99, "Description": "Latest smartphone with advanced features.", "StockCount": 50 },
  { "Name": "Bluetooth Speaker", "Price": 59.99, "Description": "Portable speaker with excellent sound quality.", "StockCount": 120 },
  { "Name": "Yoga Mat", "Price": 19.99, "Description": "Eco-friendly mat for yoga and exercises.", "StockCount": 200 },
  { "Name": "Office Chair", "Price": 129.99, "Description": "Ergonomic chair with lumbar support.", "StockCount": 40 },
  { "Name": "Action Camera", "Price": 199.99, "Description": "Waterproof camera for outdoor adventures.", "StockCount": 30 },
  { "Name": "Electric Kettle", "Price": 29.99, "Description": "Quick boiling kettle with auto-shutoff.", "StockCount": 85 },
  { "Name": "Kitchen Knife Set", "Price": 49.99, "Description": "Stainless steel knives for precision cutting.", "StockCount": 100 },
  { "Name": "Leather Wallet", "Price": 25.99, "Description": "Durable wallet made of genuine leather.", "StockCount": 60 },
  { "Name": "Fitness Tracker", "Price": 89.99, "Description": "Track your health and fitness goals.", "StockCount": 45 },
  { "Name": "Backpack", "Price": 39.99, "Description": "Spacious backpack for school or travel.", "StockCount": 80 },
  { "Name": "Desk Lamp", "Price": 22.99, "Description": "LED lamp with adjustable brightness.", "StockCount": 110 },
  { "Name": "Hair Dryer", "Price": 35.99, "Description": "Compact and powerful hair dryer.", "StockCount": 70 },
  { "Name": "Electric Toothbrush", "Price": 49.99, "Description": "Rechargeable toothbrush with multiple modes.", "StockCount": 55 },
  { "Name": "Men's Watch", "Price": 149.99, "Description": "Stylish watch with leather strap.", "StockCount": 35 },
  { "Name": "Women's Handbag", "Price": 89.99, "Description": "Elegant handbag with ample storage.", "StockCount": 40 },
  { "Name": "Wireless Mouse", "Price": 19.99, "Description": "Ergonomic mouse with fast connectivity.", "StockCount": 150 },
  { "Name": "Portable Charger", "Price": 29.99, "Description": "Fast-charging power bank with dual ports.", "StockCount": 90 },
  { "Name": "Smartwatch", "Price": 129.99, "Description": "Feature-rich smartwatch for daily use.", "StockCount": 50 },
  { "Name": "Noise-Cancelling Headphones", "Price": 199.99, "Description": "Enjoy immersive sound anywhere.", "StockCount": 60 },
  { "Name": "LED Monitor", "Price": 159.99, "Description": "Full HD monitor for work and entertainment.", "StockCount": 20 },
  { "Name": "Digital Camera", "Price": 349.99, "Description": "High-resolution camera for photography.", "StockCount": 25 },
  { "Name": "Portable Blender", "Price": 39.99, "Description": "Make smoothies on the go.", "StockCount": 100 },
  { "Name": "Electric Scooter", "Price": 499.99, "Description": "Eco-friendly scooter for urban commuting.", "StockCount": 15 },
  { "Name": "Air Purifier", "Price": 129.99, "Description": "Breathe clean air with advanced filtration.", "StockCount": 50 },
  { "Name": "Cookware Set", "Price": 79.99, "Description": "Non-stick cookware for everyday cooking.", "StockCount": 70 },
  { "Name": "Wireless Keyboard", "Price": 29.99, "Description": "Comfortable typing with Bluetooth connectivity.", "StockCount": 90 },
  { "Name": "Foam Roller", "Price": 19.99, "Description": "Relieve muscle tension after workouts.", "StockCount": 120 },
  { "Name": "Running Socks", "Price": 9.99, "Description": "Moisture-wicking socks for athletes.", "StockCount": 200 },
  { "Name": "Travel Mug", "Price": 14.99, "Description": "Keep your drinks hot or cold on the go.", "StockCount": 150 },
  { "Name": "Electric Griddle", "Price": 49.99, "Description": "Non-stick griddle for pancakes and more.", "StockCount": 45 },
  { "Name": "Cycling Helmet", "Price": 69.99, "Description": "Stay safe on the road with this helmet.", "StockCount": 60 },
  { "Name": "Wireless Charger", "Price": 24.99, "Description": "Fast wireless charging for smartphones.", "StockCount": 100 },
  { "Name": "Standing Desk", "Price": 299.99, "Description": "Adjustable desk for a healthier workspace.", "StockCount": 20 },
  { "Name": "Smart Thermostat", "Price": 199.99, "Description": "Control your home's temperature remotely.", "StockCount": 30 },
  { "Name": "Coffee Maker", "Price": 59.99, "Description": "Brew fresh coffee every morning.", "StockCount": 50 },
  { "Name": "Vacuum Cleaner", "Price": 129.99, "Description": "Powerful suction for a clean home.", "StockCount": 40 },
  { "Name": "Indoor Plant", "Price": 15.99, "Description": "Add greenery to your living space.", "StockCount": 200 },
  { "Name": "Board Game", "Price": 29.99, "Description": "Fun for family and friends.", "StockCount": 75 },
  { "Name": "Baby Stroller", "Price": 199.99, "Description": "Lightweight and easy to maneuver.", "StockCount": 15 },
  { "Name": "Pet Bed", "Price": 39.99, "Description": "Comfortable bed for your furry friend.", "StockCount": 100 },
  { "Name": "Garden Tools Set", "Price": 49.99, "Description": "Everything you need for gardening.", "StockCount": 85 },
  { "Name": "Yoga Blocks", "Price": 14.99, "Description": "Enhance your yoga practice.", "StockCount": 150 },
  { "Name": "Climbing Gear", "Price": 89.99, "Description": "Durable gear for outdoor climbing.", "StockCount": 20 },
  { "Name": "Winter Jacket", "Price": 129.99, "Description": "Stay warm in extreme cold.", "StockCount": 25 },
  { "Name": "Sneakers", "Price": 59.99, "Description": "Trendy and comfortable footwear.", "StockCount": 100 },
  { "Name": "Camping Tent", "Price": 99.99, "Description": "Waterproof tent for 2-3 people.", "StockCount": 35 },
  { "Name": "Electric Drill", "Price": 69.99, "Description": "Perfect tool for home projects.", "StockCount": 60 },
  { "Name": "Flashlight", "Price": 19.99, "Description": "Bright and durable flashlight.", "StockCount": 150 },
  { "Name": "Book Lamp", "Price": 12.99, "Description": "Clip-on lamp for nighttime reading.", "StockCount": 120 },
  { "Name": "Wristbands", "Price": 5.99, "Description": "Stylish and sweat-absorbent wristbands.", "StockCount": 200 },
  { "Name": "Laptop Stand", "Price": 39.99, "Description": "Adjustable stand for laptops.", "StockCount": 70 },
  { "Name": "Wireless Router", "Price": 89.99, "Description": "High-speed Wi-Fi router for home use.", "StockCount": 35 },
  { "Name": "Smart Bulb", "Price": 19.99, "Description": "Control the light color with your phone.", "StockCount": 100 },
  { "Name": "Air Fryer", "Price": 129.99, "Description": "Cook healthier meals with less oil.", "StockCount": 50 },
  { "Name": "Water Bottle", "Price": 14.99, "Description": "Insulated bottle for hot and cold drinks.", "StockCount": 150 },
  { "Name": "Men's Sunglasses", "Price": 29.99, "Description": "Stylish sunglasses with UV protection.", "StockCount": 80 },
  { "Name": "Women's Scarf", "Price": 19.99, "Description": "Lightweight and elegant scarf.", "StockCount": 120 },
  { "Name": "Phone Case", "Price": 12.99, "Description": "Protect your phone with a stylish case.", "StockCount": 200 },
  { "Name": "Tablet Stand", "Price": 24.99, "Description": "Convenient stand for tablets and e-readers.", "StockCount": 75 },
  { "Name": "LED String Lights", "Price": 16.99, "Description": "Decorative lights for cozy ambiance.", "StockCount": 100 },
  { "Name": "Travel Pillow", "Price": 19.99, "Description": "Comfortable neck support for travel.", "StockCount": 90 },
  { "Name": "Waterproof Jacket", "Price": 79.99, "Description": "Stay dry during heavy rain.", "StockCount": 40 },
  { "Name": "Portable Fan", "Price": 29.99, "Description": "Compact and rechargeable fan.", "StockCount": 110 },
  { "Name": "Mechanical Keyboard", "Price": 99.99, "Description": "Durable keyboard with tactile keys.", "StockCount": 35 },
  { "Name": "Wall Art", "Price": 49.99, "Description": "Beautiful art piece for your home.", "StockCount": 60 },
  { "Name": "Bean Bag Chair", "Price": 79.99, "Description": "Comfortable seating for relaxation.", "StockCount": 30 },
  { "Name": "Desk Organizer", "Price": 19.99, "Description": "Keep your desk tidy and organized.", "StockCount": 120 },
  { "Name": "Baking Tray Set", "Price": 29.99, "Description": "Non-stick trays for baking.", "StockCount": 80 },
  { "Name": "Electric Blanket", "Price": 59.99, "Description": "Stay warm during cold nights.", "StockCount": 50 },
  { "Name": "Foot Massager", "Price": 149.99, "Description": "Relax your feet with a soothing massage.", "StockCount": 25 },
  { "Name": "Couch Cover", "Price": 39.99, "Description": "Protect and refresh your couch.", "StockCount": 60 },
  { "Name": "Safety Goggles", "Price": 9.99, "Description": "Protect your eyes during DIY projects.", "StockCount": 200 },
  { "Name": "Pressure Cooker", "Price": 79.99, "Description": "Cook meals quickly and efficiently.", "StockCount": 40 },
  { "Name": "Weighted Blanket", "Price": 129.99, "Description": "Improve your sleep with added comfort.", "StockCount": 35 },
  { "Name": "Baby Monitor", "Price": 99.99, "Description": "Keep an eye on your baby remotely.", "StockCount": 20 },
  { "Name": "Garden Hose", "Price": 29.99, "Description": "Durable hose for watering plants.", "StockCount": 100 },
  { "Name": "Digital Thermometer", "Price": 14.99, "Description": "Accurate temperature readings in seconds.", "StockCount": 90 },
  { "Name": "Car Phone Holder", "Price": 19.99, "Description": "Securely hold your phone in the car.", "StockCount": 150 },
  { "Name": "Rechargeable Flashlight", "Price": 39.99, "Description": "Bright flashlight with USB charging.", "StockCount": 60 },
  { "Name": "Pet Collar", "Price": 12.99, "Description": "Adjustable collar for your furry friend.", "StockCount": 200 },
  { "Name": "Bike Lock", "Price": 24.99, "Description": "Secure your bike with a strong lock.", "StockCount": 100 },
  { "Name": "Skateboard", "Price": 59.99, "Description": "Durable skateboard for beginners.", "StockCount": 45 },
  { "Name": "Rain Boots", "Price": 39.99, "Description": "Stay dry during rainy days.", "StockCount": 75 },
  { "Name": "Beach Towel", "Price": 19.99, "Description": "Large and soft towel for the beach.", "StockCount": 150 },
  { "Name": "Microwave Oven", "Price": 199.99, "Description": "Cook or heat food quickly.", "StockCount": 25 },
  { "Name": "Mini Projector", "Price": 129.99, "Description": "Portable projector for movies on the go.", "StockCount": 40 },
  { "Name": "Camping Stove", "Price": 49.99, "Description": "Lightweight stove for outdoor cooking.", "StockCount": 80 },
  { "Name": "Hiking Boots", "Price": 89.99, "Description": "Comfortable and durable for long hikes.", "StockCount": 60 },
  { "Name": "Bluetooth Adapter", "Price": 14.99, "Description": "Add Bluetooth functionality to your devices.", "StockCount": 150 },
  { "Name": "Solar Charger", "Price": 59.99, "Description": "Charge your devices with solar power.", "StockCount": 35 },
  { "Name": "Dog Leash", "Price": 19.99, "Description": "Durable leash for daily walks.", "StockCount": 120 },
  { "Name": "Cat Scratcher", "Price": 29.99, "Description": "Protect your furniture and entertain your cat.", "StockCount": 90 },
  { "Name": "Bike Helmet", "Price": 49.99, "Description": "Stay safe on your cycling adventures.", "StockCount": 50 },
  { "Name": "Thermal Flask", "Price": 24.99, "Description": "Keep beverages hot or cold for hours.", "StockCount": 100 },
  { "Name": "Electric Heater", "Price": 129.99, "Description": "Efficient heating for small spaces.", "StockCount": 20 },
  { "Name": "LED Flashlight", "Price": 9.99, "Description": "Compact and powerful flashlight.", "StockCount": 200 },
  { "Name": "Workout Gloves", "Price": 19.99, "Description": "Protect your hands during gym sessions.", "StockCount": 120 },
  { "Name": "Tablet Cover", "Price": 14.99, "Description": "Protect your tablet from scratches.", "StockCount": 100 },
  { "Name": "Smart Home Hub", "Price": 99.99, "Description": "Connect and control your smart devices.", "StockCount": 30 }

]


# Insert data into the products collection
try:
    if product_data:
        result = products_collection.insert_many(product_data)
        print(f"Inserted {len(result.inserted_ids)} products into the collection.")
    else:
        print("No product data found to insert. Please populate the 'product_data' array.")
except Exception as e:
    print(f"An error occurred: {e}")
