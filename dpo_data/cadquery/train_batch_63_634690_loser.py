import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.sketch().segment((-100,78),(-94,-86)).segment((100,-76)).segment((91,86)).close().assemble().push([(-71.5,-55)]).rect(11,6,mode='s').finalize().extrude(136)