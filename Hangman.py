import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont('comicsans', 40)

# Load images
images = []
for i in range(7):
    images.append(pygame.image.load(f"hangman{i}.png"))

# Game variables
hangman_status = 0
words = [
    "astronaut", "bicycle", "cactus", "dinosaur", "elephant", "firework", "giraffe",
    "hammock", "iceberg", "jellyfish", "kaleidoscope", "lighthouse", "marshmallow",
    "nightingale", "octopus", "pyramid", "quicksand", "rainbow", "spaceship", "tornado",
    "umbrella", "volcano", "wizard", "xylophone", "yacht", "zeppelin", "accordion",
    "butterfly", "carousel", "dandelion", "earring", "flamingo", "goblin", "hedgehog",
    "igloo", "jigsaw", "kangaroo", "lantern", "mermaid", "noodle", "ostrich", "parachute",
    "quartz", "rollercoaster", "saxophone", "toadstool", "ukulele", "vampire", "whale",
    "xenon", "yeti", "zeppelin", "alchemy", "balloon", "cauldron", "drumstick", "enchilada",
    "fountain", "guitar", "hurricane", "illusion", "jungle", "koala", "leprechaun", "microscope",
    "nebula", "orchid", "pegasus", "quiver", "robot", "skeleton", "treasure", "unicorn", 
    "vortex", "whirlpool", "xenophobia", "yo-yo", "zebra", "avalanche", "boomerang", "cavern",
    "dragon", "eclipse", "frisbee", "galaxy", "hotdog", "iguanodon", "jester", "kazoo", 
    "llama", "moonbeam", "nymph", "obelisk", "penguin", "quokka", "rainforest", "spacesuit",
    "alchemy", "balloon", "cauldron", "drumstick", "enchilada", "fountain", "guitar", 
    "hurricane", "illusion", "jungle", "koala", "leprechaun", "microscope", "nebula", 
    "orchid", "pegasus", "quiver", "robot", "skeleton", "treasure", "unicorn", "vortex",
    "whirlpool", "xenophobia", "yo-yo", "zebra", "avalanche", "boomerang", "cavern", "dragon",
    "eclipse", "frisbee", "galaxy", "hotdog", "iguanodon", "jester", "kazoo", "llama", 
    "moonbeam", "nymph", "obelisk", "penguin", "quokka", "rainforest", "spacesuit", "bagpipe",
    "carousel", "dandelion", "earring", "flamingo", "goblin", "hedgehog", "igloo", "jigsaw",
    "kangaroo", "lantern", "mermaid", "noodle", "ostrich", "parachute", "quartz", "rollercoaster",
    "saxophone", "toadstool", "ukulele", "vampire", "whale", "xenon", "yeti", "zeppelin",
    "butterfly", "cauldron", "drumstick", "enchilada", "fountain", "guitar", "hurricane",
    "illusion", "jungle", "koala", "leprechaun", "microscope", "nebula", "orchid", "pegasus",
    "quiver", "robot", "skeleton", "treasure", "unicorn", "vortex", "whirlpool", "xenophobia",
    "yo-yo", "zebra", "avalanche", "boomerang", "cavern", "dragon", "eclipse", "frisbee",
    "galaxy", "hotdog", "iguanodon", "jester", "kazoo", "llama", "moonbeam", "nymph", "obelisk",
    "penguin", "quokka", "rainforest", "spacesuit"
]

word = random.choice(words)
guessed = []

def draw():
    win.fill(WHITE)
    
    # Draw word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    
    # Draw hangman image
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    
    # Display the chosen word
    word_text = FONT.render(f"The word was: {word}", 1, BLACK)
    win.blit(word_text, (WIDTH/2 - word_text.get_width()/2, HEIGHT/2 - word_text.get_height()/2 + 50))
    
    pygame.display.update()
    pygame.time.delay(3000)

# Main loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()
            if letter.isalpha() and letter not in guessed:
                guessed.append(letter)
                if letter not in word:
                    hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("YOU WON!")
        break

    if hangman_status == 6:
        display_message("YOU LOST!")
        break

pygame.quit()
