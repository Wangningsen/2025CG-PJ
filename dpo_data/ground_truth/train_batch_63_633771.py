import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
w1=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().segment((-64,27),(-46,-2)).segment((20,38)).segment((10,55)).segment((10,81)).segment((-6,81)).segment((-6,82)).segment((-9,81)).segment((-17,81)).segment((-17,76)).segment((-48,57)).arc((-97,63),(-64,27)).assemble().push([(55,-37)]).circle(45).finalize().extrude(-52).union(w0.sketch().push([(2,50)]).circle(12).circle(2,mode='s').finalize().extrude(-1)).union(w1.workplane(offset=-31/2).moveTo(47,-56).cylinder(31,9))