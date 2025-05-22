import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
w1=cq.Workplane('XY',origin=(0,0,37))
r=w0.workplane(offset=-80/2).moveTo(40,28).cylinder(80,60).union(w0.sketch().segment((-6,-29),(11,-29)).segment((11,-11)).segment((27,-11)).segment((27,26)).segment((11,26)).segment((11,45)).segment((-6,45)).segment((-6,26)).segment((-6,-11)).close().assemble().finalize().extrude(-78)).union(w1.sketch().push([(-76.5,-63)]).rect(47,50).push([(-77,-63)]).rect(8,32,mode='s').finalize().extrude(-27))