import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
r=w0.sketch().rect(96,44).push([(-37.5,-2.5)]).rect(19,5,mode='s').push([(-17,20)]).circle(2,mode='s').finalize().extrude(-195).union(w0.workplane(offset=5/2).cylinder(5,47))