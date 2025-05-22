import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
w1=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().push([(-21,70)]).circle(30).circle(4,mode='s').finalize().extrude(38).union(w0.sketch().push([(-24,9)]).rect(60,46).reset().face(w0.sketch().segment((-50,-83),(-46,-91)).segment((-10,-77)).segment((19,-100)).segment((54,-68)).segment((19,-30)).segment((-21,-61)).segment((-11,-68)).close().assemble()).finalize().extrude(71)).union(w1.workplane(offset=71/2).moveTo(41.5,52.5).box(25,47,71))