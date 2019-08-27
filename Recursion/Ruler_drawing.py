"""The main function, draw ruler, manages the construction of the entire ruler. Its arguments specify the total number of inches 
in the ruler and the major tick length.

The utility function, draw line, draws a single tick with a specified number of dashes 
(and an optional string label, that is printed after the tick).

The interesting work is done by the recursive draw interval function. This function draws the sequence of minor ticks within some interval, based upon the
length of the interval’s central tick."""

def draw_line(tick_length, tick_label=''):          #Draw tick interval based upon a central tick length.
    line = '-' * tick_length                        
    if tick_label:
        line += ' ' + tick_label                    # When whole numbers the number is printed bdesides the tick
    print(line)


def draw_interval(centre_length):                   #Draw intervals based on the centre_length
    if centre_length > 0:
        draw_interval(centre_length - 1)            # Draws top tick of the centre length
        draw_line(centre_length)                    # Draws the centre tick
        draw_interval(centre_length - 1)            # Draws Bottom tick


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')                    #Draw inch zero line
    for i in range(1, 1+num_inches):                
        draw_interval(major_length - 1)             # Draw interior ticks   
        draw_line(major_length, str(i))             # Draw the i times tick and label

draw_ruler(3, 3)