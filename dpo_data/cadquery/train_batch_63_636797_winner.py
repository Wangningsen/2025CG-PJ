import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('XY',origin=(0,0,7))
r=w0.sketch().segment((-100,-39),(-33,-39)).segment((-33,-20)).segment((-46,-20)).arc((-66,-14),(-86,-20)).segment((-97,-20)).segment((-97,-34)).arc((-98,-36),(-100,-39)).assemble().reset().face(w0.sketch().arc((-100,-61),(-99,-64),(-97,-67)).segment((-97,-81)).segment((-85,-81)).arc((-66,-87),(-46,-81)).segment((-33,-81)).segment((-33,-67)).arc((-31,-64),(-30,-61)).close().assemble()).push([(-21,80)]).circle(7).finalize().extrude(12).union(w1.workplane(offset=52/2).moveTo(-8,80).cylinder(52,20))