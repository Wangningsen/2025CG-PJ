import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-7,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().push([(-20.5,-86.5)]).rect(69,27).push([(4,39)]).circle(35).finalize().extrude(-36).union(w0.workplane(offset=80/2).moveTo(3.5,37.5).box(103,41,80)).union(w1.sketch().segment((-25,-37),(-8,-37)).arc((38,-74),(83,-37)).segment((100,-37)).segment((100,-14)).segment((83,-14)).arc((38,22),(-8,-14)).segment((-25,-14)).close().assemble().finalize().extrude(-36))