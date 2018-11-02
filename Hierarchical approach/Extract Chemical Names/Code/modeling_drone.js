//model drone --> no decision variables, just test if


//variables

float destination_position_y = 10.0;
float sample_time = 1;

float a22 = -0.625;
float a24 = 0.0


float init_pos_y = 2.0;
float init_vel_y = 0.0;

dvar float+ state_position_y;
dvar float+ state_velocity_y;
dvar float+ control_acceleration_y;


//expressions

subject to {
  control_acceleration_y == a22 * (destination_position_y - state_position_y);
  
}
