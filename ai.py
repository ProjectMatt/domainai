import random
import os

# Define properties for generating names
adjectives = [
    "Lucky", "Mega", "Royal", "Golden", "Silver", "Fun", "Win", "Bet", "Spin", "Gold",
    "Brilliant", "Magic", "Mystic", "Elite", "Prime", "Ultra", "Super", "Victory", "Grand",
    "Supreme", "Star", "Radiant", "Shiny", "Dazzling", "Bright", "Gleaming", "Sparkling",
    "Thrilling", "Exciting", "Dynamic", "Vivid", "Rich", "Glorious", "Splendid", "Luxury",
    "Fancy", "Opulent", "Wealthy", "Affluent", "Prosperous", "Fortunate", "Lavish", "Sumptuous",
    "Regal", "Noble", "Majestic", "Imperial", "Sovereign", "Monarch", "Ruler", "Crown", "Royal",
    "Prestige", "Prestigious", "Renowned", "Famous", "Celebrated", "Acclaimed", "Honored",
    "Esteemed", "Distinguished", "Eminent", "Illustrious", "Notable", "Noted", "Famed",
    "Glamorous", "Charming", "Enchanting", "Captivating", "Bewitching", "Alluring", "Fetching",
    "Elegant", "Stylish", "Chic", "Polished", "Sleek", "Neat", "Swanky", "Classy", "Posh",
    "Deluxe", "Premium", "Exclusive", "Select", "Elite", "Special", "Unique", "Rare", "Exotic"
]
nouns = [
    "Fortune", "Jackpot", "Winner", "Prize", "Vegas", "Casino", "Bounty", "Treasure", "Wealth",
    "Riches", "Reward", "Bonus", "Loot", "Payout", "Dividend", "Gain", "Profit", "Windfall",
    "Fortuity", "Chance", "Destiny", "Fate", "Lottery", "Sweepstakes", "Raffle", "Draw",
    "Potluck", "Stake", "Bet", "Wager", "Gamble", "Risk", "Venture", "Speculation", "Adventure",
    "Quest", "Journey", "Expedition", "Exploration", "Odyssey", "Voyage", "Excursion", "Tour",
    "Saga", "Tale", "Legend", "Myth", "Fable", "Story", "Narrative", "Chronicle", "Account",
    "Epic", "Adventure", "Thrill", "Experience", "Happening", "Event", "Occasion", "Affair",
    "Enterprise", "Undertaking", "Operation", "Mission", "Campaign", "Pursuit", "Quest",
    "Search", "Hunt", "Chase", "Race", "Competition", "Contest", "Match", "Tournament", "Game",
    "Play", "Sport", "Recreation", "Leisure", "Amusement", "Entertainment", "Pleasure", "Joy",
    "Delight", "Enjoyment", "Satisfaction", "Gratification", "Fulfillment", "Bliss", "Euphoria"
]
base_words = adjectives + nouns

# Function to generate a list of potential casino names
def generate_casino_names(count=10):
    names = []
    for _ in range(count):
        # Combine words from both lists for a richer set of potential names
        word1 = random.choice(base_words)
        word2 = random.choice(base_words)
        name = f"{word1}{word2}.com"
        if len(name) <= 20:  # Adjust length constraint as needed
            names.append(name)
    return names

# Simulated function to check domain availability
def check_domain_availability(domain):
    # Placeholder for domain availability check logic
    return random.choice([True, False])

# Main function to generate names and check their domain availability
def main():
    generated_names = generate_casino_names()
    available_domains = [name for name in generated_names if check_domain_availability(name)]

    # Save the available domain names to a text file
    with open("available_casino_domains.txt", "w") as file:
        for domain in available_domains:
            file.write(f"{domain}\n")
    
    print(f"Available domains saved to available_casino_domains.txt: {available_domains}")

# Run the main function
if __name__ == "__main__":
    main()
