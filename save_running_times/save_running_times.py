# Date: 03-09-2019
# Name: WenLong Wu
# Python programming pratice

# Save running times

# This program saves a sequence of video running times
# to the video_times.txt file.

def main():
    
    videos = int(input("How many videos are in the project? "))

    print("Enter the running times for each video.")

    videos_file = open('video_times.txt', 'w')

    for count in range(1, videos+1):
        
        videos_time = float(input("Video #" + str(count) + ": "))

        videos_file.write(str(videos_time) + '\n')

    videos_file.close()

    print("The times have been saved to video_times.txt.")

# Call the main function
main()
