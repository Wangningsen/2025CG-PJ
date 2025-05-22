import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
w1=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().segment((11,-47),(64,-47)).segment((64,20)).segment((32,20)).segment((32,26)).segment((11,26)).segment((11,5)).arc((-16,-20),(11,-44)).close().assemble().finalize().extrude(17).union(w0.sketch().segment((7,-12),(100,-12)).segment((100,47)).segment((79,47)).arc((51,65),(22,47)).segment((7,47)).close().assemble().finalize().extrude(24)).union(w1.sketch().segment((-49,-66),(-17,-66)).arc((34,-95),(29,-37)).segment((29,-25)).segment((-49,-25)).close().assemble().finalize().extrude(-63))