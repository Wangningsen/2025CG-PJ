import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().push([(-34,59)]).circle(41).push([(-7.5,-76.5)]).rect(27,47).reset().face(w0.sketch().segment((19,-1),(74,-49)).segment((75,-48)).segment((21,0)).close().assemble()).finalize().extrude(-100)