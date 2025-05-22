import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().arc((-97,44),(-76,-5),(-28,19)).arc((-20,34),(-31,46)).arc((-53,65),(-82,61)).arc((-86,49),(-97,44)).assemble().push([(66.5,-41)]).rect(67,50).finalize().extrude(-67).union(w0.sketch().segment((-31,23),(8,10)).arc((17,4),(28,4)).segment((44,-1)).segment((53,27)).segment((-22,51)).close().assemble().finalize().extrude(43))