import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.workplane(offset=20/2).moveTo(55,38).cylinder(20,9).union(w0.sketch().push([(-52,4)]).circle(48).circle(19,mode='s').push([(82,-34)]).circle(18).finalize().extrude(71))