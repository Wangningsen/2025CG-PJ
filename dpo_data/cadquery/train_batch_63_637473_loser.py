import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-114/2).moveTo(-13.5,36.5).box(119,127,114).union(w0.sketch().segment((-19,-65),(-9,-100)).segment((73,-85)).segment((66,-47)).close().assemble().push([(27,-69)]).circle(8,mode='s').finalize().extrude(28))