vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
myVariable = 0

def onauton_autonomous_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    pass

def ondriver_drivercontrol_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    while True:
        wait(5, MSEC)

def onevent_controller_1buttonL1_pressed_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    Output.spin(FORWARD)

def onevent_controller_1buttonL1_released_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    Output.stop()

def when_started1():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    while not brain.battery.capacity() > 25:
        controller_1.screen.print("LOW BATTERY WARNING!!!")
        wait(5, MSEC)

def onevent_controller_1buttonR1_pressed_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    Intake.spin(REVERSE)

def onevent_controller_1buttonR1_released_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    Intake.stop()

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL1.released(onevent_controller_1buttonL1_released_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonR1.released(onevent_controller_1buttonR1_released_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
