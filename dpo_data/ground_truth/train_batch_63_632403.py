import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,60))
w1=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().segment((-87,14),(-74,14)).segment((-74,-6)).segment((-62,-6)).segment((-62,14)).segment((36,14)).segment((36,38)).segment((-1,38)).segment((-2,30)).segment((-62,32)).segment((-62,33)).segment((-74,33)).segment((-74,32)).segment((-87,33)).close().assemble().push([(-68,53)]).rect(12,38).finalize().extrude(7).union(w1.sketch().arc((-35,29),(-99,-23),(-22,-50)).arc((99,10),(-35,29)).assemble().finalize().extrude(-131))