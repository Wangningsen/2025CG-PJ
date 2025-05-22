import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('XY',origin=(0,0,25))
r=w0.sketch().push([(14,-22.5)]).rect(42,93).push([(14,-23)]).circle(4,mode='s').finalize().extrude(-44).union(w0.workplane(offset=79/2).moveTo(-33.5,48).box(71,42,79)).union(w1.workplane(offset=44/2).moveTo(28,-71).cylinder(44,29))