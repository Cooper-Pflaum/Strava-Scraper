import pickle




class club(object):
    def __init__(self, html, name, athletes, weekly_distances, total_distance, _id):
        club_html = ''
        Name = ''
        Athletes = []
        Weekly_Distances = []
        Total_Distance = 0
        club_id = _id
    
    
    def save_club(self):
        with open('strava_club_data.txt', 'wb') as outp:
            pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)
