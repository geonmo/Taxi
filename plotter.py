from ROOT import *

h1 = TH1F("h1","h1",100,0,100)
h1.Fill(34)
h1.Draw()

