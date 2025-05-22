import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
w1=cq.Workplane('XY',origin=(0,0,22))
r=w0.workplane(offset=-42/2).moveTo(-44,87).cylinder(42,13).union(w0.sketch().segment((-21,-83),(-14,-83)).segment((-14,-100)).segment((12,-100)).segment((12,-83)).segment((18,-83)).segment((18,2)).segment((12,2)).segment((12,19)).segment((-14,19)).segment((-14,2)).segment((-21,2)).close().assemble().finalize().extrude(41)).union(w0.workplane(offset=88/2).moveTo(-1.5,-41).box(11,4,88)).union(w1.workplane(offset=35/2).moveTo(-41,-21).cylinder(35,54))