#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_group_1_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_group_1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
motor_group_1 = MotorGroup(motor_group_1_motor_a, motor_group_1_motor_b)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
def calculate_speed():
  return 0
# https://www.vexforum.com/t/how-to-find-the-best-pid-parameters-automatically/106037/4
# Constants for PID control
Kp = 2.0  # Proportional gain
Ki = 0.5  # Integral gain
Kd = 0.1  # Derivative gain

def run_on_button_pressed():
    setpoint = calculate_speed() #Velocity calculated from camera and triangulation
    # Initialize variables
    error = 0.0  # Error between setpoint and measured value
    integral = 0.0  # Integral of error over time
    derivative = 0.0  # Derivative of error over time
    previous_error = 0.0  # Previous error
    # Loop at a fixed time interval (e.g. every 0.1 seconds)
    while True:
        # Measure the current value of the system
        measured_value = motor_group_1.velocity(RPM)
        
        # Calculate the error between the setpoint and measured value
        error = setpoint - measured_value
        
        # Update the integral of the error
        integral = integral + error * 0.1
        
        # Calculate the derivative of the error
        derivative = (error - previous_error) / 0.1
        
        # Save the previous error for next iteration
        previous_error = error
        
        # Calculate the control output using the PID algorithm
        control_output = Kp * error + Ki * integral + Kd * derivative
        
        # Apply the control output to the system
        motor_group_1.spin(REVERSE, control_output, VOLT)
        
        # Wait for the next iteration
        wait(0.1)

controller_1.buttonL1.pressed(run_on_button_pressed)
