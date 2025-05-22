import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-69,0))
r=w0.sketch().push([(-35,0)]).rect(30,44).push([(85,-42)]).circle(15).finalize().extrude(-2).union(w0.sketch().segment((-100,-4),(-93,-4)).arc((-35,-60),(27,-4)).segment((35,-4)).segment((35,4)).segment((27,4)).arc((-35,60),(-93,4)).segment((-100,4)).close().assemble().finalize().extrude(139))