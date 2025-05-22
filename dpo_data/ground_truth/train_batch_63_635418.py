import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().segment((-47,26),(-19,26)).segment((-19,27)).arc((-15,31),(-19,35)).segment((-19,62)).segment((-47,62)).close().assemble().push([(30,-43.5)]).rect(36,37).finalize().extrude(-105).union(w0.sketch().push([(-19,31)]).circle(29).push([(-19.5,30.5)]).rect(39,3,mode='s').finalize().extrude(95))