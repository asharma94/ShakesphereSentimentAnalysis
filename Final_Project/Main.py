import ParsePlay
import Interpolate
import CharacterKMeans
import ScaleScores
import pprint
import SentimentAnalysis
import ScaleTime
import LowPassFilter

def main():
    #charDict = ParsePlay.getAllTopChars(1) # Char Dict contains a bunch of chars w/ names as keys
    charDict = ParsePlay.parsePlay('./shaks200/dream.xml') # Char Dict contains a bunch of chars w/ names as keys

    charDictScaled = ScaleTime.rescaleTime(charDict)
    charScores = SentimentAnalysis.turn_lines_to_score(charDictScaled)
    charScoresInterpolated = Interpolate.interpolate_chars_uniformly(charScores, 100)
    charScoresFiltered = LowPassFilter.lowPassAllChars(charScoresInterpolated)
    pp = pprint.PrettyPrinter()
    pp.pprint(charScoresFiltered)
main()