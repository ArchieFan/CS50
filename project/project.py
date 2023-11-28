import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAYER_SIZE = 100
ENEMY_SIZE = 100

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "Archie"
        self.level = 1
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE * 2))
        self.image.fill((0, 0, 0))
        # Draw a white circle for the head
        pygame.draw.circle(self.image, WHITE, (PLAYER_SIZE // 2, PLAYER_SIZE // 2), PLAYER_SIZE // 2) 
         # Draw a white rectangle for the body
        pygame.draw.rect(self.image, BLUE, (0, PLAYER_SIZE, PLAYER_SIZE , PLAYER_SIZE)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2)
        self.health = 20
        self.attack = 5
        self.defense = 2
        self.experience = 0
        self.last_attack_time = 0

    def attack_enemy(self, enemy):
        return attack_enemy(self, enemy)

    def level_up(self):
        level_up(self)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "Ogre"
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE * 2 ))
        self.image.fill((0, 0, 0))
        # Draw a green circle for the head
        pygame.draw.circle(self.image, GREEN, (ENEMY_SIZE // 2, ENEMY_SIZE // 2), ENEMY_SIZE // 2)  
        # Draw a red rectangle for the body
        pygame.draw.rect(self.image, RED, (0, ENEMY_SIZE, ENEMY_SIZE, ENEMY_SIZE))  
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH - 300, SCREEN_HEIGHT // 2 - ENEMY_SIZE // 2)
        self.health = 30
        self.attack = 3
        self.defense = 1


def attack_enemy(player, enemy):
    current_time = pygame.time.get_ticks()
    if current_time - player.last_attack_time > 2000:  # 2000 milliseconds (2 seconds) delay
        damage = max(0, player.attack - enemy.defense)
        enemy.health -= damage
        player.last_attack_time = current_time
        return damage
    return 0

def level_up(player):
    player.level += 1
    player.attack += 2
    player.defense += 1
    player.health += 5
    player.experience = 0


def draw_text(screen, text, position, font_size=25, color=WHITE):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_attack_message(screen, attacker, target, damage):
    message = f"{attacker.name} dealt {damage} damage to {target.name}!"
    if screen :
        draw_text(screen, message, (50, 30))
        pygame.display.flip()
        # Display the attack message for 1 second
        pygame.time.wait(1000)  
    else :
        return message

def display_victory_message(screen, enemy):
    message = f"You defeated {enemy.name}!"
    if screen :
        draw_text(screen, message , (50, 60))
        pygame.display.flip()
        # Display the victory message for 2 seconds
        pygame.time.wait(2000)  
    else :
        return message
 
 
def display_levelup_message(screen, player): 
    message = f"{player.name} leveled up!"
    if screen :  
        player.experience += 5
        player.level_up()
        draw_text(screen, message , (50, 90))
        pygame.display.flip()
        # Display the level-up message for 2 seconds
        pygame.time.wait(2000)  
    else :
        return message

def display_enemy_attack_message(screen, player, enemy, damage):
    message = f"{enemy.name} dealt {damage} damage to {player.name}."
    if screen :
        draw_text(screen, message , (SCREEN_WIDTH - 300, 30))
        pygame.display.flip()
         # Display the enemy's attack message for 1 second
        pygame.time.wait(1000) 
    else :
        return message

def battle(player, enemy, screen, clock):
    while player.health > 0 and enemy.health > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()           
        if keys[pygame.K_SPACE]:
            damage = attack_enemy(player, enemy)
            if damage > 0:
                display_attack_message(screen, player, enemy, damage )

                if enemy.health <= 0:
                    display_victory_message(screen, enemy)
                    display_levelup_message(screen, player)
                    break

                enemy_damage = max(0, enemy.attack - player.defense)
                player.health -= enemy_damage
                display_enemy_attack_message(screen, player, enemy, enemy_damage)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player
        screen.blit(player.image, player.rect.topleft)
        draw_text(screen, f"{player.name}: {player.health} HP (Level: {player.level}) ", (50, 10))

        # Draw the enemy
        screen.blit(enemy.image, enemy.rect.topleft)
        draw_text(screen, f"{enemy.name}: {enemy.health} HP", (SCREEN_WIDTH - 300, 10))

        pygame.display.flip()
        # Cap the frame rate to 60 FPS
        clock.tick(60)  

# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set the title of the window
    pygame.display.set_caption("Archie's Adventure")  
    clock = pygame.time.Clock()
    player = Player()

    while True:
        enemy = Enemy()

        # battle loop
        battle(player, enemy, screen, clock)

if __name__ == "__main__":
    main()
