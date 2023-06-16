def virar_ate_linha_R(cor):
    i = 0
    while True:
        i += 1
        d = ((-1)**i)
        angulo_limite = d * i * 15

        robot.reset()

        while abs(robot.angle()) < abs(angulo_limite):
            robot.drive(0, 20 * d)
            wait(10)
            if color_sensor_floor.color() != cor:
                robot.turn(2.5*d)
                return      