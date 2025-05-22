import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().push([(-32,-64)]).circle(36).reset().face(w0.sketch().segment((-6,50),(68,50)).segment((68,80)).segment((30,80)).arc((17,97),(-4,99)).segment((9,90)).segment((6,85)).segment((9,80)).segment((-6,80)).close().assemble()).push([(32,65)]).circle(11,mode='s').finalize().extrude(27).union(w1.sketch().push([(5,-8)]).circle(14).push([(13,-12.5)]).rect(2,9,mode='s').finalize().extrude(-41))