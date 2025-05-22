import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-69,0))
r=w0.sketch().push([(-37.5,-10)]).rect(47,70).push([(85,-43)]).circle(15).finalize().extrude(-1).union(w0.sketch().segment((-100,-4),(-93,-4)).arc((-33,-60),(27,-4)).segment((35,-4)).segment((35,4)).segment((27,4)).arc((-33,60),(-93,4)).segment((-100,4)).close().assemble().finalize().extrude(139))