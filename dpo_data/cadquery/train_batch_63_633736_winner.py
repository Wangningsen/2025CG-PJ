import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,18))
w1=cq.Workplane('ZX',origin=(0,-85,0))
r=w0.sketch().push([(-50,59)]).circle(26).reset().face(w0.sketch().segment((-12,5),(-12,11)).segment((10,11)).segment((10,-10)).arc((56,71),(-12,5)).assemble()).finalize().extrude(-101).union(w0.workplane(offset=-51/2).moveTo(-80,-61).cylinder(51,20)).union(w1.sketch().segment((7,-13),(84,-13)).segment((84,100)).segment((7,100)).segment((7,1)).arc((9,-3),(7,-7)).close().assemble().push([(45,43)]).circle(35,mode='s').finalize().extrude(15))