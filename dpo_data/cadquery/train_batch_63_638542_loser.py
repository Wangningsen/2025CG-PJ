import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.workplane(offset=-71/2).moveTo(-52,-58).cylinder(71,42).union(w0.sketch().segment((17,90),(26,90)).segment((26,97)).segment((20,97)).arc((38,79),(17,95)).close().assemble().push([(59,-46)]).circle(35).finalize().extrude(-10)).union(w0.workplane(offset=51/2).moveTo(15,44).cylinder(51,12)).union(w1.sketch().segment((-72,-58),(-72,-56)).segment((-71,-56)).segment((-71,-57)).arc((-71,-55),(-72,-58)).assemble().finalize().extrude(-13))