import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.workplane(offset=23/2).moveTo(-97,-40).box(6,88,23).union(w0.sketch().push([(49,33)]).circle(51).push([(36,28.5)]).rect(48,41,mode='s').finalize().extrude(45))