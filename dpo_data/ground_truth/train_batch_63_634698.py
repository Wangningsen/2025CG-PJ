import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().push([(30.5,47)]).rect(43,68).push([(30,47)]).rect(20,34,mode='s').finalize().extrude(-99).union(w0.sketch().segment((-82,-16),(-58,-16)).segment((-78,-57)).segment((-45,-74)).arc((-16,-74),(-25,-47)).segment((-10,-16)).segment((25,-16)).segment((25,5)).segment((0,5)).segment((21,47)).segment((-18,66)).segment((-47,5)).segment((-82,5)).close().assemble().finalize().extrude(101)).union(w1.workplane(offset=25/2).moveTo(30.5,47).box(103,68,25))