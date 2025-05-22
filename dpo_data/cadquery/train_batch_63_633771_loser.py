import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
w1=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().segment((-63,27),(-46,-3)).segment((20,38)).segment((10,56)).segment((10,81)).segment((-1,81)).segment((-2,83)).segment((-5,81)).segment((-23,81)).segment((-23,72)).segment((-46,59)).arc((-97,64),(-63,27)).assemble().push([(55,-37)]).circle(45).finalize().extrude(-52).union(w1.workplane(offset=-32/2).moveTo(47,-56).cylinder(32,9))