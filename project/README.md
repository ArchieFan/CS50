# Archie's Adventure
#### Video Demo:  https://youtu.be/oJPOb72i9Rc
#### Description:

I made an simple RPG game. Join me as we dive into the world of Archie and his quest to defeat the Ogre.
Playing is easy. I control Archie using space keys on my keyboard. I make him attack the Ogre, and we try to win. If Archie wins, he becomes stronger and can face another challenges.

Now, let's peek behind the scenes. I used a cool tool called Pygame to create this game. It's like telling the computer what to do to make Archie and the Ogre do their thing.

Here's a bit of the code. We have a 'Player' class for Archie and an 'Enemy' class for the Ogre. The code makes the game run smoothly, and it's like magic when you see it in action.

Playing is not just about winning. It's about thinking and getting better. Each time Archie wins, he gets stronger. It's pretty cool!

I put a lot of heart into this, and I'd love to hear what you think. If you have any ideas or just want to say hi, leave a comment. I'm building something fun here, and I'd love for you to be a part of it.

Thanks for hanging out with me today. If you enjoyed Archie's Adventure, and I'll be sharing more updates about the game, and I'd love for you to join the adventure.

- requirements.txt -- listed libraries that my project requires

- test_project.py -- unit tes

- Readme.md -- readme

- project.py -- project itself

<br>
<br>

# Design Choices and Debates:


1. Sprite Class for Player and Enemy:

    -   I chose to use a special class called pygame.sprite.Sprite for both the player (Archie) and the enemy (Ogre). It's like a helper class that makes handling these characters in the game easier. This choice helps keep things neat and organized.

1. Separate Functions for Attack, Level Up, and Messages:

    - I decided to create different groups of instructions (functions) for specific jobs. One group helps with attacking, another with leveling up, and yet another for showing messages on the screen. This way, each job has its own set of instructions, making it simpler to understand and change things later.

1. Constants for Screen and Character Sizes:

    - I used special names (constants) for important numbers, like how big the screen is and how big the characters are. This makes it easier to find and change these numbers if I want to make the game bigger or smaller. It's like giving names to important values so I can remember them easily.

1. Utility Function for Drawing Text:

    - I created a little helper function called draw_text to make writing words on the screen easier. Instead of writing the same instructions over and over, I put them in one place. It's like having a special tool that helps me quickly write text in the game.

1. Game Loop Structure:
    - I set up a loop that keeps going as long as the game is running. This loop is like the heartbeat of the game—it keeps checking if I'm doing something (like pressing a key) and updates the game accordingly. It's a common way to make sure the game feels responsive and interactive.

# How I Decide to Use That:

I made these choices because they make the code easier to read and work with. When I look at the code, I want it to be clear what each part does. Using special classes and functions helps me organize things neatly, like putting toys in different boxes. The constants help me remember important numbers easily, and the loop keeps the game alive and kicking, ready to respond to what I do.

When deciding on these choices, I thought about what would make the game easy to understand and change. I wanted to avoid a messy, confusing code that might make it hard for me or someone else to add new things or fix problems later. So, each choice was like picking the right tool for the job—making sure I have everything I need to create a fun and enjoyable game.
