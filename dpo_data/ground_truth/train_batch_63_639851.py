import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().arc((-28,6),(22,-82),(74,4)).segment((100,4)).segment((100,35)).segment((8,35)).segment((8,82)).segment((-28,82)).close().assemble().finalize().extrude(-16).union(w0.sketch().push([(-37.5,-51.5)]).rect(125,55).rect(11,15,mode='s').finalize().extrude(23))