#
#  File:
#    contour1.py
#
#  Synopsis:
#    Illustrates converting to a log axis.
#
#  Categories:
#    Contouring
#
#  Author:
#    Fred Clare
#  
#  Date of initial publication:
#    February 2004
#
#  Description:
#    This example shows how to convert a linear axis to a log axis. It
#    also shows how to force PS/PDF output to be portrait.
#
#  Effects illustrated:
#    o  Using scalar field resources to change the range of the Y axis.
#    o  Using transformation resources to log the Y axis.
#    o  Using wkOrientation to force a portrait orientation.
# 
#  Output:
#    This example produces two visualizations:
#      1.)  Contouring with two linear axes.
#      2.)  Contouring with a log Y axis and a linear X axis.
#
#  Notes:
#     

from __future__ import print_function
import Ngl
import numpy

#
# Create some dummy data for the contour plot.
#
N=25
 
T = numpy.zeros((N,N),'f')
 
jspn = numpy.power(numpy.arange(-12,13),2)
ispn = numpy.power(numpy.arange(-12,13),2)

for i in range(0,len(ispn)):
  T[i,:] = (jspn + ispn[i]).astype('f')

T = 100.0 - numpy.sqrt(64 * T)

wks_type = "png"
wks = Ngl.open_wks(wks_type,"contour1")

cnres = Ngl.Resources()
cnres.sfYCStartV    = 10         # Define limits for Y axis.
cnres.sfYCEndV      = 1000
cnres.tiXAxisString = "linear"   # Label for X axis.
cnres.tiYAxisString = "linear"   # Label for Y axis.

contour = Ngl.contour(wks,T,cnres)  # Create and draw contour plot.

cnres.tiYAxisString = "log"    # Label for Y axis.
cnres.trYLog        = True     # Log scaling for Y axis

contour = Ngl.contour(wks,T,cnres)  # Create and draw contour plot.

Ngl.end()

expected_pngs = ['contour1.000001.png', 'contour1.000002.png']
for png in expected_pngs:
    if not os.path.isfile(png):
        print(f'[ERROR] Did not create expected PNG file: {png}')

