import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,58))
r=w0.sketch().push([(-29.5,75.5)]).rect(73,49).push([(21,-59)]).circle(41).finalize().extrude(-116).union(w0.sketch().push([(31,-11)]).circle(35).push([(7,-35)]).circle(2,mode='s').finalize().extrude(-110))