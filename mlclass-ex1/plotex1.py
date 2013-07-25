#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import ROOT

inData = open('ex1data1.txt')


pts = []
for line in inData:
  data = line.split(',')
  pop = float(data[0])
  profit = float(data[1].rstrip())
  pts.append((pop,profit))


pts.sort()

g = ROOT.TGraph()
for i, pt in enumerate(pts):
  g.SetPoint(i, pt[0], pt[1])

g.SetMarkerSize(1)
g.SetMarkerStyle(23)
g.Draw('ap')
g.Fit('pol1')
raw_input()

