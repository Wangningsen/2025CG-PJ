import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-86,-1),(58,-100)).segment((86,-60)).segment((-58,39)).close().assemble().reset().face(w0.sketch().segment((9,94),(37,60)).segment((44,66)).segment((17,100)).close().assemble()).finalize().extrude(-22)