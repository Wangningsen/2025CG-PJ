import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('ZX',origin=(0,0,0))
r=w0.sketch().segment((-56,17),(12,-15)).segment((31,26)).segment((76,22)).segment((84,94)).segment((27,100)).segment((21,39)).segment((-33,65)).close().assemble().finalize().extrude(-63).union(w0.workplane(offset=-53/2).moveTo(-41,7.5).box(86,9,53)).union(w1.sketch().segment((-5,-60),(18,-60)).segment((18,-21)).segment((15,-21)).segment((15,16)).segment((3,16)).segment((3,-21)).segment((-5,-21)).close().assemble().push([(-1.5,-35)]).rect(3,6,mode='s').finalize().extrude(-100))