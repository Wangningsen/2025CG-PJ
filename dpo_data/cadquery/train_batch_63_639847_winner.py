import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-41,-39),(34,-39)).segment((34,-26)).segment((5,-26)).segment((5,-9)).segment((-1,-9)).segment((0,4)).arc((-22,7),(-41,14)).close().assemble().push([(-19,-35)]).circle(2,mode='s').finalize().extrude(-200).union(w0.sketch().push([(21,0)]).rect(40,158).circle(4,mode='s').finalize().extrude(-93))