import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().segment((-100,78),(-94,-86)).segment((100,-76)).segment((91,86)).close().assemble().push([(-72.5,-56.5)]).rect(13,9,mode='s').finalize().extrude(-136)