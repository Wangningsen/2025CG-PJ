import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,25))
w1=cq.Workplane('XY',origin=(0,0,-20))
r=w0.workplane(offset=20/2).moveTo(-47.5,33).box(49,134,20).union(w1.sketch().push([(21,-49)]).circle(51).push([(21,-49)]).rect(58,82,mode='s').finalize().extrude(-25))