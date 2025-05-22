import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.workplane(offset=-52/2).moveTo(-38,-5.5).box(124,125,52).union(w0.sketch().push([(75,43)]).circle(25).circle(5,mode='s').finalize().extrude(64))