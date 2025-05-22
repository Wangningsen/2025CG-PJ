import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().push([(0,-41)]).circle(49).push([(-3,-83)]).circle(4,mode='s').finalize().extrude(-99).union(w0.sketch().segment((33,83),(44,70)).segment((44,90)).segment((33,90)).close().assemble().finalize().extrude(101)).union(w1.workplane(offset=-93/2).moveTo(0,-2).cylinder(93,7))