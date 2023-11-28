import pygame
import pytest
from project import Player, Enemy, attack_enemy, display_attack_message, display_victory_message


def test_attack_enemy():
    player = Player()
    enemy = Enemy()

    damage = attack_enemy(player, enemy)
    # Initial damage should be zero
    assert damage == 0  
    # Simulate time passing
    pygame.time.get_ticks = lambda: 3000  
    damage = attack_enemy(player, enemy)
    assert damage == max(0, player.attack - enemy.defense)
    
    
def test_level_up():
    player = Player()
    player.level_up()

    assert player.level == 2
    assert player.attack == 7
    assert player.defense == 3
    assert player.health == 25
    assert player.experience == 0


def test_display_attack_message():
    player = Player()
    enemy = Enemy()

    damage = attack_enemy(player, enemy)
    result = display_attack_message(None, player, enemy, damage)
    expected_result = f"{player.name} dealt {damage} damage to {enemy.name}!"
    assert result == expected_result
    
def test_display_victory_message():
    enemy = Enemy()

    result = display_victory_message(None, enemy)
    expected_result = f"You defeated {enemy.name}!"
    assert result == expected_result