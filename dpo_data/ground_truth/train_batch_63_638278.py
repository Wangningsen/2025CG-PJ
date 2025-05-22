import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('ZX',origin=(0,26,0))
r=w0.workplane(offset=-78/2).moveTo(-2.5,54.5).box(75,91,78).union(w0.sketch().segment((-76,-100),(24,-100)).segment((24,-65)).arc((74,-7),(1,14)).segment((-76,14)).close().assemble().push([(-38,-35)]).rect(68,68,mode='s').finalize().extrude(3)).union(w1.sketch().arc((-35,43),(32,49),(-30,75)).segment((-21,75)).segment((-21,43)).close().assemble().push([(2.5,86)]).rect(3,2,mode='s').finalize().extrude(64))