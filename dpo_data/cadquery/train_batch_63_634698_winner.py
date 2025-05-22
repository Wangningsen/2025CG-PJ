import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().push([(30.5,47.5)]).rect(43,67).push([(30,47)]).rect(20,34,mode='s').finalize().extrude(-99).union(w0.sketch().segment((-82,-16),(-57,-16)).segment((-78,-57)).segment((-48,-71)).arc((-19,-77),(-25,-47)).segment((-10,-16)).segment((25,-16)).segment((25,5)).segment((0,5)).segment((21,47)).segment((-20,67)).segment((-47,5)).segment((-82,5)).close().assemble().finalize().extrude(101)).union(w1.workplane(offset=68/2).moveTo(31.5,31.5).box(25,101,68))