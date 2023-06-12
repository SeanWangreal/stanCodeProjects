"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 2        # Maximum initial horizontal speed for the ball


class Breakoutgraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 live_num=3):
        # Create a graphical window, with some extra space
        self.__window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        self.__window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=self.__window_width, height=self.__window_height, title=title)
        self.__live_num = live_num
        # Create a paddle
        self.__p_w = paddle_width
        self.__p_h = paddle_height
        self.__p_o = paddle_offset
        self.__paddle = GRect(width=self.__p_w, height=self.__p_h)
        self.__paddle.filled = True
        self.__window.add(self.__paddle, (self.__window.width-paddle_width)/2, self.__window.height-self.__p_o)
        # Center a filled ball in the graphical window
        self.__ball_radius = ball_radius
        self.__ball = GOval(width=self.__ball_radius*2, height=self.__ball_radius*2)
        self.__ball.filled = True
        self.__window.add(self.__ball, (self.__window.width-self.__ball.width)/2, (self.__window.height-self.__ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.__record_speed_x = 0
        self.__record_speed_y = 0
        # lose
        self.__loser_w = GLabel('Loser :(')
        self.__loser_w.color = 'Brown'
        self.__loser_w.font = 'Courier-60-bold-italic'
        # win
        self.__winner_w = GLabel('Hey Champ!')
        self.__winner_w.color = 'Orange'
        self.__winner_w.font = 'Courier-55-bold-italic'
        # Initialize our mouse listeners
        self.__checker = True
        # the game start key
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_move)
        self.__again_check = False
        # Draw bricks
        self.__bricks_c = brick_cols
        self.__bricks_r = brick_rows
        self.__brick_s = brick_spacing
        for x in range(brick_cols):
            self.start_x = 0
            if x == 0:
                self.start_y = brick_offset
            else:
                self.start_y += self.__bricks.height + self.__brick_s
            for y in range(brick_rows):
                self.__bricks = GRect(brick_width, brick_height)
                self.__bricks.filled = True
                if x <= 1:
                    self.__bricks.fill_color = 'red'
                elif x <= 3:
                    self.__bricks.fill_color = 'orange'
                elif x <= 5:
                    self.__bricks.fill_color = 'yellow'
                elif x <= 7:
                    self.__bricks.fill_color = 'lightyellow'
                else:
                    self.__bricks.fill_color = 'ivory'
                self.__bricks.color = self.__bricks.fill_color
                self.__window.add(self.__bricks, self.start_x, self.start_y)
                self.start_x += brick_width + brick_spacing
        # score
        self.__point = 0
        self.__score = GLabel('Score: '+str(self.__point))
        self.__score.font = 'Courier-20-bold'
        self.__window.add(self.__score, x=0, y=self.__score.height+10)
        # lives
        self.__lives = GLabel('Lives: '+chr(10084)*self.__live_num)
        self.__lives.font = 'Courier-20-bold'
        self.__window.add(self.__lives, x=0, y=self.__window_height)

    @property
    def brick_c(self):
        return self.__bricks_c

    @property
    def brick_r(self):
        return self.__bricks_r

    @property
    def window(self):
        return self.__window

    @property
    def ball(self):
        return self.__ball

    @property
    def paddle(self):
        return self.__paddle

    @property
    def score(self):
        return self.__score

    @property
    def lives(self):
        return self.__lives

    def paddle_move(self, mouse):
        # paddle follow your mouse
        self.__paddle.x = mouse.x - self.__paddle.width/2
        if self.__paddle.x <= 0:
            self.__paddle.x = 0
        if self.__paddle.x >= self.__window.width-self.__paddle.width:
            self.__paddle.x = self.__window.width-self.__paddle.width

    def game_start(self, mouse):
        # game start for one click
        if self.__checker:
            self.__checker = False
            if self.__point < 10:
                self.__dx = MAX_X_SPEED
                self.__dy = INITIAL_Y_SPEED
            else:
                self.__dx = self.__record_speed_x
                if self.__record_speed_y < 0:
                    self.__dy = -self.__record_speed_y
                else:
                    self.__dy = self.__record_speed_y
            if random.random() > 0.5:
                self.__dx = -self.__dx

    @property
    def x_speed(self):
        return self.__dx

    @property
    def y_speed(self):
        return self.__dy

    @x_speed.setter
    def x_speed(self, new_speed):
        self.__dx = new_speed

    @y_speed.setter
    def y_speed(self, new_speed):
        self.__dy = new_speed

    def reset_ball(self):
        # start again
        self.__window.remove(self.__ball)
        self.__ball = GOval(width=self.__ball_radius*2, height=self.__ball_radius*2)
        self.__ball.filled = True
        self.__window.add(self.__ball, (self.__window.width-self.__ball.width)/2, (self.__window.height-self.__ball.height)/2)
        self.__checker = True
        self.__dx = 0
        self.__dy = 0

    def set_ball_y(self):
        self.__ball.y = self.__paddle.y - self.__ball.height

    def renew_point(self):
        # break one brick renew status of point
        self.__window.remove(self.__score)
        self.__score = GLabel('Score: ' + str(self.__point))
        self.__score.font = 'Courier-20-bold'
        self.__window.add(self.__score, x=0, y=self.__score.height+10)

    def renew_lives(self, new_l):
        # when ball missed renew status of your lives
        self.__window.remove(self.__lives)
        if new_l != 0:
            self.__lives = GLabel('Lives :'+chr(10084)*new_l)
        else:
            self.__lives = GLabel('Lives :' + chr(9760))
        self.__lives.font = 'Courier-20-bold'
        self.__window.add(self.__lives, x=0, y=self.__window_height)

    def loser(self):
        # when lives == 0
        self.__window.add(self.__loser_w, (self.__window_width - self.__loser_w.width)/2,
                          (self.__window_height - self.__loser_w.height)/2)

    def winner(self):
        # when break all bricks
        self.__window.add(self.__winner_w, (self.__window_width - self.__winner_w.width) / 2,
                          (self.__window_height - self.__winner_w.height) / 2)

    def speed_up(self):
        if self.__point == 10:
            if self.__dx > 0:
                self.__dx += 1
            else:
                self.__dx -= 1
            if self.__dy > 0:
                self.__dy += 1
            else:
                self.__dy -= 1
        elif self.__point == 30:
            if self.__dx > 0:
                self.__dx += 1
            else:
                self.__dx -= 1
            if self.__dy > 0:
                self.__dy += 1
            else:
                self.__dy -= 1
        elif self.__point == 50:
            if self.__dx > 0:
                self.__dx += 1
            else:
                self.__dx -= 1
            if self.__dy > 0:
                self.__dy += 1
            else:
                self.__dy -= 1
        elif self.__point == 70:
            if self.__dx > 0:
                self.__dx += 1
            else:
                self.__dx -= 1
            if self.__dy > 0:
                self.__dy += 1
            else:
                self.__dy -= 1
        self.__record_speed_x = self.__dx
        self.__record_speed_y = self.__dy

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, new_point):
        self.__point = new_point




