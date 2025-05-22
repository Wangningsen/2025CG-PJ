import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
r=w0.workplane(offset=-119/2).moveTo(37,-39).cylinder(119,61).union(w0.sketch().push([(-37,68)]).circle(3).push([(-36.5,68)]).rect(3,2,mode='s').finalize().extrude(-49)).union(w0.sketch().segment((-98,79),(-25,33)).segment((-13,54)).segment((-43,74)).arc((-46,75),(-49,79)).segment((-85,100)).close().assemble().finalize().extrude(71))