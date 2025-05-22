import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
w1=cq.Workplane('XY',origin=(0,0,-22))
r=w0.workplane(offset=81/2).moveTo(-14,83).cylinder(81,16).union(w1.sketch().push([(12.5,-73.5)]).rect(35,51).push([(18,-83)]).circle(2,mode='s').finalize().extrude(-78))