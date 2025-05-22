import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.sketch().arc((-28,1),(21,-82),(76,-2)).segment((83,-3)).segment((84,4)).segment((100,4)).segment((100,35)).segment((8,35)).segment((8,82)).segment((-28,82)).close().assemble().finalize().extrude(-16).union(w0.sketch().push([(-37.5,-51.5)]).rect(125,55).push([(-37,-52)]).circle(9,mode='s').finalize().extrude(24))