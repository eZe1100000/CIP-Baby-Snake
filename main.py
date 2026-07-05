from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
OBSTACLE_SIZE_X = 40
OBSTACLE_SIZE_Y = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    delay = DELAY
    player = create_player(canvas)
    goal = create_goal(canvas)

    obstacles = []

    # At the beginning of the game the snake will move to the right
    direciton = "Right"
    score = 0

    while True:
        key = canvas.get_last_key_press()
                       
        # Change direction based on key press
        if key == 'LEFT_ARROW':
            direciton = "Left" 
        elif key == 'RIGHT_ARROW':
            direciton = "Right" 
        elif key == 'UP_ARROW':
            direciton = "Up" 
        elif key == 'DOWN_ARROW':
            direciton = "Down" 

        # Move the player in the current direction
        if direciton == 'Right':
            canvas.move(player , SIZE , 0)                
        elif direciton == 'Left':
            canvas.move(player , -SIZE , 0)
        elif direciton == 'Up':
            canvas.move(player , 0 , -SIZE)
        elif direciton == 'Down':
            canvas.move(player , 0 , SIZE)

        # Check if player eats the goal
        if has_reached_goal(canvas , player , goal):
            delay = delay * 0.94 # make the game faster
            time.sleep(delay)
            score += 1
            # add a new obstacle every 5 points
            if score %5 == 0:
                create_obstacle(canvas , player , goal , obstacles)
        else:        
            time.sleep(delay)

        # Check for game over conditions
        if check_out_of_bounds(canvas , player) or has_collided_obstacle(canvas ,player , obstacles):
            break
            
    # Show the final score when the game ends
    create_score_text(canvas , score)
        

def create_player(canvas):
    player = canvas.create_rectangle(
        0, 
        0, 
        SIZE, 
        SIZE,
        "blue"
        )
    return player

def create_goal(canvas):
    goal = canvas.create_rectangle(
        360, 
        360, 
        360 + SIZE, 
        360 + SIZE,
        "pink"
        )
    return goal

def check_out_of_bounds(canvas , obj):
    x = canvas.get_left_x(obj)
    y = canvas.get_top_y(obj)

    # Return True if the player leaves the screen boundaries
    if x >= CANVAS_WIDTH or y >= CANVAS_HEIGHT or x < 0 or y < 0:
        return True
    else:
        return False


def has_reached_goal(canvas, player , goal):
    left_x = canvas.get_left_x(player)
    top_y = canvas.get_top_y(player)

    # Check for overlapping objects at player's position
    objs = canvas.find_overlapping(
        left_x, 
        top_y, 
        left_x + SIZE, 
        top_y + SIZE
    )
    
    if goal in objs:
        move_goal(canvas , goal)
        return True
    return False

def move_goal(canvas , goal):
    # choose the cell number
    max_value = (( CANVAS_WIDTH - SIZE) // 20)

    # find the coordinates of that cell
    random_place_x = random.randint(0 , max_value)* SIZE
    random_place_y = random.randint(0 , max_value)* SIZE

    canvas.moveto(goal, random_place_x, random_place_y)

def create_score_text(canvas , score):
    score_text = canvas.create_text(
    CANVAS_WIDTH/3, 
    CANVAS_HEIGHT/4 * 2, 
    f"SCORE: {score}",
    font = 'Arial', 
    font_size = 20, 
    color ='blue'
)


def create_obstacle(canvas, player , goal , obstacles):
    left_x_player = canvas.get_left_x(player)
    top_y_player = canvas.get_top_y(player)

    left_x_goal = canvas.get_left_x(goal)
    top_y_goal = canvas.get_top_y(goal)

    max_value = (( CANVAS_WIDTH - SIZE) // 20)

    random_x = random.randint(0 , max_value) * SIZE
    random_y = random.randint(0 , max_value) * SIZE

    # Do not create obstacles on top of the player or the goal
    while (random_x, random_y) == (left_x_player, top_y_player) or (random_x, random_y) == (left_x_goal, top_y_goal):
        random_x = random.randint(0 , max_value) * SIZE
        random_y = random.randint(0 , max_value) * SIZE

    obstacle = canvas.create_rectangle(
            random_x, 
            random_y, 
            random_x + OBSTACLE_SIZE_X, 
            random_y + OBSTACLE_SIZE_Y,
            "purple"
            )
    obstacles.append(obstacle)
    

def has_collided_obstacle(canvas , player , obstacles):
    left_x = canvas.get_left_x(player)
    top_y = canvas.get_top_y(player)

    objs = canvas.find_overlapping(
        left_x, 
        top_y, 
        left_x + SIZE, 
        top_y + SIZE
    )

    # Return True if the player hits any obstacle in the list
    for obstacle in obstacles:
        if obstacle in objs:
            return True
    return False


if __name__ == '__main__':
    main()
