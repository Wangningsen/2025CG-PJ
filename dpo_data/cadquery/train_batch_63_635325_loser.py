import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().push([(-42,-41.5)]).rect(104,81).push([(28,17)]).circle(29).finalize().extrude(-119).union(w1.sketch().segment((7,23),(7,71)).segment((65,71)).arc((-33,-2),(94,23)).close().assemble().finalize().extrude(78))