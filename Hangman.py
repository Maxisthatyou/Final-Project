import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont('comicsans', 40)

images = []
for i in range(7):
    images.append(pygame.image.load(f"hangman{i}.png"))

number = 0
words = [
    'apple', 'banana', 'grape', 'orange', 'peach', 'plum', 'pear', 'melon', 'berry', 'cherry',
    'mango', 'papaya', 'kiwi', 'lemon', 'lime', 'coconut', 'date', 'fig', 'guava', 'apricot',
    'blackberry', 'blueberry', 'cranberry', 'elderberry', 'gooseberry', 'raspberry', 'strawberry',
    'watermelon', 'pomegranate', 'nectarine', 'tangerine', 'persimmon', 'passionfruit', 'dragonfruit',
    'lychee', 'jackfruit', 'durian', 'avocado', 'quince', 'carrot', 'broccoli', 'cabbage', 'cauliflower',
    'lettuce', 'spinach', 'kale', 'celery', 'cucumber', 'zucchini', 'eggplant', 'bellpepper', 'chili',
    'onion', 'garlic', 'ginger', 'radish', 'beetroot', 'potato', 'tomato', 'pumpkin', 'squash', 'yam',
    'computer', 'laptop', 'keyboard', 'monitor', 'printer', 'mouse', 'tablet', 'smartphone', 'headphones',
    'router', 'modem', 'scanner', 'webcam', 'microphone', 'joystick', 'projector', 'speaker', 'screen',
    'desktop', 'network', 'software', 'hardware', 'database', 'internet', 'website', 'browser', 'application',
    'program', 'code', 'algorithm', 'function', 'variable', 'constant', 'loop', 'conditional', 'array',
    'list', 'dictionary', 'tuple', 'string', 'integer', 'float', 'boolean', 'class', 'object', 'method',
    'module', 'library', 'framework', 'syntax', 'debug', 'compile', 'execute', 'integrate', 'automate',
    'optimize', 'develop', 'design', 'test', 'deploy', 'maintain', 'refactor', 'document', 'review',
    'collaborate', 'innovate', 'analyze', 'simulate', 'model', 'visualize', 'predict', 'classify', 'cluster',
    'regress', 'correlate', 'normalize', 'scale', 'standardize', 'transform', 'extract', 'load', 'store',
    'retrieve', 'backup', 'restore', 'encrypt', 'decrypt', 'secure', 'authenticate', 'authorize', 'protect',
    'defend', 'detect', 'monitor', 'report', 'alert', 'respond', 'recover', 'simulate', 'forecast', 'visualize',
    'interpret', 'quantify', 'measure', 'estimate', 'calibrate', 'analyze', 'model', 'optimize', 'simulate',
    'predict', 'visualize', 'verify', 'validate', 'test', 'debug', 'document', 'train', 'evaluate', 'tune',
    'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate', 'manage', 'lead',
    'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore', 'discover',
    'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct', 'assemble', 'manufacture', 'produce', 'develop',
    'test', 'validate', 'verify', 'analyze', 'optimize', 'simulate', 'model', 'predict', 'visualize', 'document',
    'train', 'evaluate', 'tune', 'deploy', 'maintain', 'improve', 'innovate', 'automate', 'integrate', 'collaborate',
    'manage', 'lead', 'coach', 'mentor', 'support', 'advise', 'consult', 'teach', 'learn', 'research', 'explore',
    'discover', 'invent', 'design', 'create', 'build', 'construct'
]

word = random.choice(words).upper()  # Convert the word to uppercase to match with guessed letters
guessed = []

def draw():
    window.fill(WHITE)
    
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))
    
    # Display the hangman image
    window.blit(images[number], (150, 100))
    
    # Display the guessed letters
    guessed_text = FONT.render("Guessed: " + ", ".join(guessed), 1, BLACK)
    window.blit(guessed_text, (400, 300))
    
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    
    word_text = FONT.render(f"The word was: {word}", 1, BLACK)
    window.blit(word_text, (WIDTH/2 - word_text.get_width()/2, HEIGHT/2 - word_text.get_height()/2 + 50))
    
    pygame.display.update()
    pygame.time.delay(3000)

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
                    number += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("YOU WON!")
        break

    if number == 6:
        display_message("YOU LOST!")
        break

pygame.quit()
