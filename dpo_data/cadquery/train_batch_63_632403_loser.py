import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,67))
w1=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().push([(-73,34)]).rect(28,76).push([(-79,29)]).rect(10,6,mode='s').finalize().extrude(-12).union(w0.workplane(offset=-2/2).moveTo(27,18).cylinder(2,20)).union(w1.sketch().arc((-37,30),(-100,-14),(-30,-56)).arc((100,2),(-37,30)).assemble().finalize().extrude(-132))