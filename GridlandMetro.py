# https://www.hackerrank.com/challenges/gridland-metro/problem?isFullScreen=true

def gridlandMetro(n, m, k, track):
    # Write your code here
    spots = n*m
    track.sort(key = lambda track: min(track[1], track[2]))
    total_track_spots = 0
    rows = dict()

    for row, start_index, end_index in track:  
        print(row, start_index, end_index)
        if  start_index > end_index:
           (start_index, end_index) = (end_index, start_index) 
        
        if row not in rows:                
            total_track_spots += end_index - start_index +1 
            rows[row] = end_index           
            print(total_track_spots)         
        else:            
            if start_index > rows[row]:
                total_track_spots += end_index - start_index + 1
                rows[row] = end_index
                print(total_track_spots) 
            elif end_index > rows[row]:
                total_track_spots += end_index - rows[row]
                rows[row] = end_index
                
            print(rows[row]) 
   
    spots -= total_track_spots

    return spots
