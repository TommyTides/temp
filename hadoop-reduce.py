from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageHeightByCountry(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        # skip the first line
        if 'ID,Name' in line:
            return
        words = line.split(',')
        country = words[5]
        height = self.parse_height(words[27])
        if height == -1:
            return
        yield country, height        
    

    def reducer(self, country, heights):
        total_height = 0.0
        num_players = 0.0
        for height in heights:
            total_height += height
            num_players += 1
        
        average_height = total_height / num_players
        
        yield country, average_height
    
    def parse_height(self, height_str):
        try:
            feet, inches = map(int, height_str.split("'"))
            total_inches = feet * 12 + inches
        except:
            total_inches = -1
        return total_inches

if __name__ == '__main__':
    AverageHeightByCountry.run()
