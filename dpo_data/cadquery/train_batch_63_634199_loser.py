import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().push([(84,-93.5)]).rect(22,13).push([(91,-95)]).rect(4,6,mode='s').finalize().extrude(-25).union(w0.sketch().segment((-77,40),(-77,52)).segment((-41,52)).segment((-41,43)).arc((-28,69),(-46,93)).segment((-46,100)).segment((-47,100)).segment((-47,93)).arc((-93,79),(-76,40)).close().assemble().push([(-61,70)]).circle(10,mode='s').finalize().extrude(13)).union(w1.workplane(offset=-83/2).moveTo(73.5,-16.5).box(43,11,83))