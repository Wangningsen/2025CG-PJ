import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.sketch().push([(4,1)]).circle(2).push([(66,14)]).circle(34).push([(50,39)]).circle(2,mode='s').finalize().extrude(-58).union(w0.sketch().push([(-53,-20)]).circle(47).push([(44,64)]).circle(3).finalize().extrude(66))