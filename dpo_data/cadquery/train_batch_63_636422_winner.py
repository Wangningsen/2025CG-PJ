import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().arc((-96,44),(-77,-5),(-28,19)).arc((-20,36),(-32,47)).arc((-56,66),(-84,60)).arc((-86,49),(-96,44)).assemble().push([(66.5,-41)]).rect(67,50).finalize().extrude(-67).union(w0.sketch().segment((-29,22),(14,8)).arc((18,3),(25,5)).segment((44,-1)).segment((53,27)).segment((-22,51)).close().assemble().finalize().extrude(43))