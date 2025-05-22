import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().push([(-32,-64)]).circle(36).reset().face(w0.sketch().segment((-6,50),(68,50)).segment((68,80)).segment((41,80)).arc((21,94),(-4,99)).segment((10,80)).segment((-6,80)).close().assemble()).push([(32,66)]).circle(11,mode='s').finalize().extrude(27).union(w1.sketch().push([(6,-8)]).circle(14).push([(14,-11)]).circle(2,mode='s').finalize().extrude(-41))