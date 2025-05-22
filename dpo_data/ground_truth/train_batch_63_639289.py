import cadquery as cq
w0=cq.Workplane('YZ',origin=(74,0,0))
r=w0.workplane(offset=-149/2).moveTo(-35,-84).cylinder(149,16).union(w0.sketch().segment((-55,74),(-45,50)).arc((-46,13),(-21,-13)).segment((-11,-38)).segment((55,-12)).segment((45,13)).arc((46,49),(21,75)).segment((11,100)).close().assemble().push([(0,31)]).rect(26,14,mode='s').finalize().extrude(-101))