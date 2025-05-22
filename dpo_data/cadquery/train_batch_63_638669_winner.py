import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
w1=cq.Workplane('YZ',origin=(46,0,0))
r=w0.sketch().arc((55,91),(5,56),(62,80)).segment((62,79)).arc((64,70),(63,61)).segment((64,61)).segment((64,79)).segment((62,79)).segment((62,80)).arc((58,86),(59,93)).segment((58,98)).arc((57,98),(55,99)).close().assemble().push([(33,69)]).circle(18,mode='s').finalize().extrude(-97).union(w0.sketch().segment((-94,-77),(-91,-100)).segment((-76,-97)).segment((-76,-63)).segment((-94,-63)).close().assemble().finalize().extrude(21)).union(w1.workplane(offset=-85/2).moveTo(57,-63).cylinder(85,37))