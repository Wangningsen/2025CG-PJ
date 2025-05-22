import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
r=w0.sketch().segment((-48,-22),(48,-22)).segment((48,22)).segment((-14,22)).segment((-13,21)).segment((-17,18)).segment((-20,21)).segment((-18,22)).segment((-48,22)).close().assemble().push([(-33,-2.5)]).rect(10,5,mode='s').finalize().extrude(-195).union(w0.workplane(offset=5/2).cylinder(5,47))