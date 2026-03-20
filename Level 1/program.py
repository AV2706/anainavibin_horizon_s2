import math
def calculate_trip():
    try:
        #Taking input from users
        a1 = float(input("Enter x-coordintes of origin(in meters): "))
        b1 = float(input("Enter y-coordintes of origin(in meters): "))
        a2 = float(input("Enter x-coordintes of destination(in meters): "))
        b2 = float(input("Enter y-coordintes of destination(in meters): "))

        #Calculating distance
        #distance = ((a2-a1)^2 +(b2-b1)^2)^0.5
        distance = math.sqrt((a2-a1)**2 + (b2-b1)**2)
        print(f"\nDistance to destination: {distance:.2f} m")
        #Calculating time
        u = float(input("enter initial velocity(in m/s): "))
        a = float(input("enter acceleration(in m/s^2): "))
        v = float(input("Enter maximum velocity(in m/s): "))

        #error handling for negative acceleration
        if a<=0 and u==0:
            print("Error: Acceleration must be positive when initial velocity is zero.")
            return
        elif a>0:

            #time to reach top speed : v = u+at

            time = (v-u)/a
            #distance covered during acceleration : s = ut + 0.5at^2
            distance_acc = (u*time) + (0.5*a*(time**2))
            if distance_acc >= distance:
                #time to reach destination : s = ut + 0.5at^2
                time_dest = (-u + math.sqrt(u**2 + 2*a*distance)) / a
                print(f"Time to reach the destination: {time_dest:.2f} seconds")
            else:
                #time to cover remaining distance at max speed
                remaining_distance = distance - distance_acc
                #at constant speed , in this case max speed : time = distance/speed
                time_at_maxspeed = remaining_distance / v
                time_dest = time + time_at_maxspeed
                print(f"Time to reach the destination: {time_dest:.2f} seconds")

        else:
            #time to reach destination : t = distance / u
            time_dest = distance / u
            print(f"Time to reach the destination: {time_dest:.2f} seconds")
    except ValueError:
        print("Error: Please enter valid numeric values for required parameters.")
        
if __name__ == "__main__":
    calculate_trip()