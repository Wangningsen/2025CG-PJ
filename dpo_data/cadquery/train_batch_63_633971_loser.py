import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-65,0))
r=w0.workplane(offset=84/2).moveTo(16.5,65).box(167,60,84).union(w0.sketch().push([(-28,-23)]).circle(72).circle(2,mode='s').finalize().extrude(130))