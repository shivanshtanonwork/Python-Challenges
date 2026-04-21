"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer
  💡 Making things beautiful
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import textwrap

fields = ["name", "profession", "passion", "emoji", "website"]
data = {}

for field in fields:
    data[field] = input(f"Enter your {field} : ").strip()

print("\n Choose your style : ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = input("Enter 1, 2 or 3: ").strip()


def generate_bio(style):
    if style == "1":
        return f"{data['emoji']} {data['name']} | {data['profession']} \n 💡 {data['passion']} \n {data['website']}"
    elif style == "2":
        return f"{data['emoji']} {data['name']}\n {data['profession']} 🔥\n {data['passion']}\n {data['website']} 🔥"
    elif style == "3":
        return f"{data['emoji'] * 3} \n - {data['profession']}\n {data['passion']} \n {data['website']} \n {data['emoji'] * 3}"


bio = generate_bio(style)

print("\n Your stylish bio: \n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to text file ? (y / n):").lower()

if save == "y":
    filename = f"{data['name'].lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File saved")
