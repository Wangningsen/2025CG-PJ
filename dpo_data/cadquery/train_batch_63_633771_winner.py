import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
w1=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().segment((-65,27),(-45,-3)).segment((20,38)).segment((10,55)).segment((10,81)).segment((-6,81)).segment((-7,83)).segment((-11,81)).segment((-17,81)).segment((-17,77)).segment((-47,58)).arc((-97,64),(-65,27)).assemble().push([(55,-37)]).circle(45).finalize().extrude(-52).union(w1.workplane(offset=-31/2).moveTo(47,-56).cylinder(31,9))