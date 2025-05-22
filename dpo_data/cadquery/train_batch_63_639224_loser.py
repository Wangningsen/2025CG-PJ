import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-15,-2),(53,-1)).segment((53,18)).segment((-15,17)).close().assemble().push([(19,9)]).circle(7,mode='s').finalize().extrude(-42).union(w0.sketch().push([(-63.5,-74)]).rect(73,30).push([(19,8)]).circle(81).finalize().extrude(-16))