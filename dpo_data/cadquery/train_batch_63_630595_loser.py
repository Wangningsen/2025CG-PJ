import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
r=w0.sketch().push([(-46.5,-23)]).rect(107,4).push([(57,0)]).circle(43).finalize().extrude(-112).union(w0.sketch().push([(-47,-23)]).circle(18).reset().face(w0.sketch().segment((-60,-26),(-42,-31)).segment((-33,-7)).segment((-51,0)).close().assemble(),mode='s').finalize().extrude(4))