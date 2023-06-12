"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import Breakoutgraphics
FRAME_RATE = 9         # 100 frames per second
NUM_LIVES = 10			# Number of attempts


def main():
    graphics = Breakoutgraphics(live_num=NUM_LIVES)
    # Add the animation loop here!
    lives = NUM_LIVES
    while True:
        if lives == 0:
            break
        if graphics.point == graphics.brick_c * graphics.brick_r:
            break
        graphics.ball.move(graphics.x_speed, graphics.y_speed)
        pause(FRAME_RATE)
        if graphics.ball.x <= 0 or \
                graphics.ball.x >= graphics.window.width - graphics.ball.width:
            if graphics.ball.x <= 0:
                graphics.ball.x = 0
            if graphics.ball.x >= graphics.window.width - graphics.ball.width:
                graphics.ball.x = graphics.window.width - graphics.ball.width
            graphics.x_speed = -graphics.x_speed
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            graphics.renew_lives(lives)
            if lives != 0:
                graphics.reset_ball()
        if graphics.ball.y <= 0:
            graphics.y_speed = -graphics.y_speed
        # four points will be detected
        ball_left_up = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_right_up = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        ball_left_down = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        ball_right_down = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                        graphics.ball.y + graphics.ball.height)
        if ball_right_up or ball_right_down or ball_left_up or ball_left_down is not None:
            # ball is falling down
            if ball_right_down is not None and ball_left_down is None:
                if ball_right_down is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_right_up is not None and ball_left_up is None:
                        # two right corners are detected
                        if ball_right_up is not graphics.paddle and ball_right_up is not graphics.score and \
                                ball_right_down is not graphics.paddle and ball_right_down is not graphics.score \
                                and ball_right_up is not graphics.lives and ball_right_down is not graphics.lives:
                            # check obj is brick
                            if ball_right_down is ball_right_up:
                                graphics.window.remove(ball_right_down)
                                graphics.point += 1
                                graphics.speed_up()
                            else:
                                graphics.window.remove(ball_right_down)
                                graphics.window.remove(ball_right_up)
                                graphics.point += 1
                                graphics.speed_up()
                                graphics.point += 1
                                graphics.speed_up()
                            graphics.ball.x = graphics.ball.x - graphics.x_speed
                            graphics.x_speed = -graphics.x_speed
                            graphics.renew_point()
                    elif ball_right_up is None and ball_left_up is None:
                        # one upper right corner is detected
                        if ball_right_down is not graphics.paddle and ball_right_down is not graphics.score and \
                                ball_right_down is not graphics.lives:
                            graphics.window.remove(ball_right_down)
                            graphics.y_speed = -graphics.y_speed
                            graphics.point += 1
                            graphics.speed_up()
                            graphics.renew_point()
            elif ball_left_down is not None and ball_right_down is None:
                if ball_left_down is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_left_up is not None and ball_right_up is None:
                        # two left corners are detected
                        if ball_left_up is not graphics.paddle and ball_left_up is not graphics.score and \
                                ball_left_down is not graphics.paddle and ball_left_down is not graphics.score and \
                                ball_left_up is not graphics.lives and ball_left_down is not graphics.lives:
                            # check obj is brick
                            if ball_left_down is ball_left_up:
                                graphics.window.remove(ball_left_down)
                                graphics.point += 1
                                graphics.speed_up()
                            else:
                                graphics.window.remove(ball_left_down)
                                graphics.window.remove(ball_left_up)
                                graphics.point += 1
                                graphics.speed_up()
                                graphics.point += 1
                                graphics.speed_up()
                            graphics.x_speed = -graphics.x_speed
                            graphics.ball.x = graphics.ball.x + graphics.x_speed
                            graphics.renew_point()
                    elif ball_left_up is None and ball_left_up is None:
                        # one upper left corner is detected
                        if ball_left_down is not graphics.score and ball_left_down is not graphics.paddle and \
                                ball_left_down is not graphics.lives:
                            graphics.window.remove(ball_left_down)
                            graphics.point += 1
                            graphics.speed_up()
                            graphics.y_speed = -graphics.y_speed
                            graphics.renew_point()
            elif ball_right_down and ball_left_down is not None:
                # two lower corners are detected
                if ball_right_down and ball_left_down is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_right_down is not graphics.paddle and ball_left_down is not graphics.paddle and \
                            ball_right_down is not graphics.score and ball_left_down is not graphics.score and \
                            ball_right_down is not graphics.lives and ball_left_down is not graphics.lives:
                        # check obj is brick
                        graphics.y_speed = -graphics.y_speed
                        if ball_left_down is ball_right_down:
                            graphics.window.remove(ball_left_down)
                            graphics.point += 1
                            graphics.speed_up()
                        else:
                            graphics.window.remove(ball_left_down)
                            graphics.window.remove(ball_right_down)
                            graphics.point += 1
                            graphics.speed_up()
                            graphics.point += 1
                            graphics.speed_up()
                        graphics.renew_point()
            # ball is bouncing up
            elif ball_right_up is not None and ball_left_up is None:
                if ball_right_up is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_right_down is not None and ball_left_down is None:
                        # two right corners are detected
                        if ball_right_up is not graphics.paddle and ball_right_down is not graphics.paddle and \
                                ball_right_up is not graphics.score and ball_right_down is not graphics.score and \
                                ball_right_up is not graphics.lives and ball_right_down is not graphics.lives:
                            # check obj is brick
                            if ball_right_up is ball_right_down:
                                graphics.window.remove(ball_right_up)
                                graphics.point += 1
                                graphics.speed_up()
                            else:
                                graphics.window.remove(ball_right_up)
                                graphics.window.remove(ball_right_down)
                                graphics.point += 1
                                graphics.speed_up()
                                graphics.point += 1
                                graphics.speed_up()
                            graphics.ball.x = graphics.ball.x - graphics.x_speed
                            graphics.x_speed = -graphics.x_speed
                            graphics.renew_point()
                    elif ball_right_down is None and ball_left_down is None:
                        # one upper corner is detected
                        if ball_right_up is not graphics.paddle and ball_right_up is not graphics.score and \
                                ball_right_up is not graphics.lives:
                            # check obj is brick
                            graphics.window.remove(ball_right_up)
                            graphics.y_speed = -graphics.y_speed
                            graphics.point += 1
                            graphics.speed_up()
                            graphics.renew_point()
            elif ball_left_up is not None and ball_right_up is None:
                if ball_left_up is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_left_down is not None and ball_right_down is None:
                        # two left corners are detected
                        if ball_left_up is not graphics.paddle and ball_right_down is not graphics.paddle and \
                                ball_left_up is not graphics.score and ball_right_down is not graphics.score and \
                                ball_left_up is not graphics.lives and ball_right_down is not graphics.lives:
                            # check obj is brick
                            if ball_left_up is ball_left_down:
                                graphics.window.remove(ball_left_up)
                                graphics.point += 1
                                graphics.speed_up()
                            else:
                                graphics.window.remove(ball_left_up)
                                graphics.window.remove(ball_left_down)
                                graphics.point += 1
                                graphics.speed_up()
                                graphics.point += 1
                                graphics.speed_up()
                            graphics.x_speed = -graphics.x_speed
                            graphics.ball.x = graphics.ball.x + graphics.x_speed
                            graphics.renew_point()
                    elif ball_left_down is None and ball_right_down is None:
                        # one upper left corners is detected
                        if ball_left_up is not graphics.score and ball_left_up is not graphics.paddle and \
                                ball_left_up is not graphics.lives:
                            # check obj is brick
                            if ball_left_up is not None:
                                graphics.window.remove(ball_left_up)
                                graphics.point += 1
                            graphics.y_speed = -graphics.y_speed
                            graphics.renew_point()
            elif ball_right_up and ball_left_up is not None:
                # two upper corners are detected
                if ball_right_up and ball_left_up is graphics.paddle:
                    graphics.set_ball_y()
                    graphics.y_speed = -graphics.y_speed
                else:
                    if ball_right_up is not graphics.paddle and ball_left_up is not graphics.paddle and\
                            ball_right_up is not graphics.score and ball_left_up is not graphics.score and \
                            ball_right_up is not graphics.lives and ball_left_up is not graphics.lives:
                        # check obj is brick
                        if ball_left_up is ball_right_up:
                            graphics.window.remove(ball_left_up)
                            graphics.point += 1
                            graphics.speed_up()
                        else:
                            graphics.window.remove(ball_left_up)
                            graphics.window.remove(ball_right_up)
                            graphics.point += 1
                            graphics.speed_up()
                            graphics.point += 1
                            graphics.speed_up()
                        graphics.y_speed = -graphics.y_speed
                        graphics.renew_point()
    if lives == 0:
        graphics.loser()
    else:
        graphics.winner()


if __name__ == '__main__':
    main()
