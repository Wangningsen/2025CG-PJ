import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
r=w0.workplane(offset=-84/2).moveTo(-48,-63).box(104,4,84).union(w0.sketch().push([(39,4)]).circle(61).circle(37,mode='s').finalize().extrude(-37))