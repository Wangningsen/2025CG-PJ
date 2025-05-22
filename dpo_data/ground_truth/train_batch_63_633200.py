import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.sketch().segment((-100,-19),(-19,-19)).segment((-19,6)).segment((22,-78)).segment((100,-40)).segment((55,52)).segment((-19,16)).segment((-19,42)).segment((-100,42)).close().assemble().reset().face(w0.sketch().segment((-46,55),(-42,45)).segment((21,67)).segment((17,78)).close().assemble()).finalize().extrude(-83)