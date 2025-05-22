import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
r=w0.sketch().arc((-65,2),(-66,5),(-63,6)).arc((-98,18),(-65,2)).assemble().push([(-81,11)]).circle(14,mode='s').finalize().extrude(-25).union(w0.sketch().arc((47,89),(-88,-47),(100,-10)).arc((59,32),(47,89)).assemble().finalize().extrude(40))