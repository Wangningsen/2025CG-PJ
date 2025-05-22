import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().arc((-28,5),(21,-82),(74,4)).segment((100,4)).segment((100,35)).segment((8,35)).segment((8,82)).segment((-28,82)).close().assemble().finalize().extrude(-17).union(w0.sketch().push([(-37.5,-51.5)]).rect(125,55).push([(-37.5,-52)]).rect(11,14,mode='s').finalize().extrude(23))