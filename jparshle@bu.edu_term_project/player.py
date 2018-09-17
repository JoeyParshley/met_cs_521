
class Player():
    """ 

    Player class

        :params :   name                  - String - name of the player
                :   performance           - List - offensive stats for games

        :returns:   Player object

    """
    def __init__(self, name, performance):
        self.__name = name
        self.__performance = performance

    # tuple to hold possible hit occurences
    hits = ('1b','2b','3b','4b')
    # tuple to hold possible walk, hit by pitch or sacrafice occurences
    walks_hbp_sac = ('bb','hpb','sac')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_performance(self):
        return self.__performance

    def set_performance(performance):
        self.__performance = performance

    def get_plate_appearances(self):
        """
        Definition: Gets the game performance 
            : input - self
            : output - List - perfomance values converted to a list
        """
        return list(filter(None, self.__performance))

    def get_total_hits(self):
        """
        Definition: Gets the hits that were in the game performance 
            : input - self
            : output - List - a list of events that are in the hits array
        """
        pa = self.get_plate_appearances()
        # create a list if event (h) is in the plate appearances list
        # exists in the hit array
        return [ h for h in pa if h in self.hits]

    def get_doubles(self):
        """
        Definition: Gets the doubles that were in the game performance 
            : input - self
            : output - Int - total_2b number of doubles
        """
        total_2b = 0
        hits = self.get_total_hits()
        # if the hits list is empty there are no doubles
        if len(hits) != 0:
            # loop through hits and check for '2b'
            for hit in hits:
                if hit.lower() == '2b':
                    # increment double total
                    total_2b += 1
        return total_2b

    def get_triples(self):
        """
        Definition: Gets the triples that were in the game performance 
            : input - self
            : output - Int - total_3b number of triples
        """
        total_3b = 0
        hits = self.get_total_hits()
        # if the hits list is empty there are no doubles
        if len(hits) != 0:
            # loop through hits and check for '2b'
            for hit in hits:
                if hit.lower() == '3b':
                    # increment triple total
                    total_3b += 1
        return total_3b

    def get_home_runs(self):
        """
        Definition: Gets the homeruns that were in the game performance 
            : input - self
            : output - Int - total_hr number of homeruns
        """
        total_hr = 0
        hits = self.get_total_hits()
        # if the hits list is empty there are no doubles
        if len(hits) != 0:
            # loop through hits and check for 'hr'
            for hit in hits:
                if hit.lower() == 'hr':
                    # increment hr total
                    total_hr += 1
        return total_hr

    def get_total_bases(self):
        """
        Definition: Gets the total bases that were accrued by the player in the 
                    game performance consists of sum of all hits in hits array
            : input - self
            : output - Int - total_bases number of bases
        """
        total_bases = 0
        hits = self.get_total_hits()
        if len(hits) != 0:
            for hit in hits:
                # strip the 'b of the hit'
                hit = int(hit.rstrip('b'))
                # convert to Int
                bases = int(hit)
                # increment total bases
                total_bases += bases

        return total_bases

    def get_walks(self):
        """
        Definition: Gets the total walks that were in the game performance consists
                    of sum of all hits in hits array
            : input - self
            : output - Int - total_walks number of walks
        """
        total_walks = 0
        # get plate appearances
        pa = self.get_plate_appearances()
        # loop through plate appearances and check for 'bb'
        for w in pa:
            if w == "bb":
                # increment hr total
                total_walks += 1

        return total_walks

    def get_hbp(self):
        """
        Definition: Gets the total hit by pitcher events that were in the game 
                    performance consists of sum of all hits in hits array
            : input - self
            : output - Int - total_walks number of walks
        """
        total_hbp = 0
        # get plate appearances
        pa = self.get_plate_appearances()
        # loop through plate appearances and check for 'bb'
        for h in pa:
            if h == "hpb":
                # increment hit by pitch total
                total_hbp += 1

        return total_hbp

    def get_sac(self):
        """
        Definition: Gets the total sacrafice hits events that were in the game 
                    performance consists of sum of all hits in hits array
            : input - self
            : output - Int - total_sac number of sacrafice hits
        """
        total_sac = 0
        # get plate appearances
        pa = self.get_plate_appearances()
        # loop through plate appearances and check for 'sac'
        for h in pa:
            if h == "sac":
                total_sac += 1

        return total_sac

    def get_on_base_by_error(self):
        """
        Definition: Gets the total hit by pitcher events that were in the game 
                    performance consists of sum of all hits in hits array
            : input - self
            : output - Int - total_e number of walks
        """
        total_e = 0
        # get plate appearances
        pa = self.get_plate_appearances()
        # loop through plate appearances and check for 'e'
        for ob in pa:
            # if event startw with 'e' its an error
            if ob[0] == 'e':
                # increment total on base by errors
                total_e += 1

        return total_e

    def get_fc(self):
        """
        Definition: Gets the total hit by pitcher events that were in the game 
                    performance consists of sum of all hits in hits array
            : input - self
            : output - Int - total_walks number of walks
        """
        total_fc = 0
        # get plate appearances
        pa = self.get_plate_appearances()
        # loop through plate appearances and check for 'bb'
        for h in pa:
            if h == "fc":
                total_fc += 1

        return total_fc

    def get_on_base_percentage(self):
        """
        Definition: Gets the on base percentage for the player. determined by 
                    the ratio of the (hits, walks, hit by pitcher and fielders
                    choice) to total at bats and sacrafice hits
            : input - self
            : output - Float - on base percentage
        """
        # create local variables to hold for numerator and denominator
        num = len(
                self.get_total_hits()
                ) + self.get_walks() + self.get_hbp() + self.get_fc()
        denom = self.get_at_bats() + num + self.get_sac()
        # if there are no hits there is no on base percentage
        if denom == 0:
            return 0
        else:
            return num / denom

    def get_ops(self):
        """
        Definition: Gets the on ops determined by adding the on base percentage 
                    and the slugging percentage.
            : input - self
            : output - Float - ops
        """        
        return self.get_on_base_percentage() + self.get_slugging()

    def get_walks_hbp_sac(self):
        """
        Definition: Gets walks, hit by pitcher and sacrafice hit totals.
            : input - self
            : output - List - walks, hbp and sacrafice hits
        """        
        # get plate appearances
        pa = self.get_plate_appearances()
        # return combintation of walks, hpb and sacrafice hits
        return self.get_walks() + self.get_hbp() + self.get_sac()

    def get_at_bats(self):
        """
        Definition: Gets at bats, determined by plate appearances minus walks,
                    hit by pitcher events and scrafice hits.
            : input - self
            : output - Int - at bats
        """ 
        # return the length of the plate appearances -  walks, hbp and sac list      
        return len(self.get_plate_appearances()) - self.get_walks_hbp_sac()

    def get_batting_average(self):
        """
        Definition: Gets the batting average for the player determined by
                    dividing the total hits by at bats
            : input - self
            : output - Float - batting average
        """
        # if there are no at bats the average is 0 
        if self.get_at_bats() == 0:
            return 0
        else:
            return len(self.get_total_hits()) / self.get_at_bats()
        
    def get_slugging(self):
        """
        Definition: Gets the slugging percentage for the player determined by
                    dividing the total bases by at bats
            : input - self
            : output - Float - slugging percentage
        """
        # if there are no at bats the slugging is 0 
        if self.get_at_bats() == 0:
            return 0
        else:
            return self.get_total_bases() / self.get_at_bats()

    def __str__(self):
        s_name = str(self.__name)
        s_performance = str(self.__performance)

        return "Account name = {0},"\
            " performance = {1},".format(s_name, s_performance)
