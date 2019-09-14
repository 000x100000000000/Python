# Date: 04-09-2019
# Name: WenLong Wu
# Python programming pratice

# Read running times

# This program the values in the video_times.txt
# file and calculates their total.

def main():

    print("Here are the running times for each video:")

    video_file = open('video_times.txt', 'r')

    line = video_file.readline()

    count = 0

    total = 0

    while line != '':

        count += 1
        
        video_time = float(line)

        print("Video #" + str(count) + ":", video_time)

        total += video_time

        line = video_file.readline()

    print("The total running time is", total, "seconds.")

# Call the main function
main()

